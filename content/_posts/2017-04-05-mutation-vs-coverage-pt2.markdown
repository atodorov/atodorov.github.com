Title: Mutation Testing vs. Coverage, Pt. 2
Headline: which one is better
date: 2017-04-05 09:18
comments: true
Tags: QA, fedora.planet
og_image: images/ninja_turtles.jpg
twitter_image: images/ninja_turtles.jpg

In a [previous post]({filename}2016-12-27-mutation-vs-coverage.markdown) I
have shown an example of real world bugs which we were not able to detect
despite having 100% mutation and test coverage. I am going to show you another
example here.

This example comes from one of my training courses. The task is to write a
class which represents a bank account with methods to deposit, withdraw and
transfer money. The solution looks like this

    :::python bank.py
    class BankAccount(object):
        def __init__(self, name, balance):
            self.name = name
            self._balance = balance
            self._history = []
    
        def deposit(self, amount):
            if amount <= 0:
                raise ValueError('Deposit amount must be positive!')
    
            self._balance += amount
    
        def withdraw(self, amount):
            if amount <= 0:
                raise ValueError('Withdraw amount must be positive!')
    
            if amount <= self._balance:
                self._balance -= amount
                return True
            else:
                self._history.append("Withdraw for %d failed" % amount)
    
            return False
    
        def transfer_to(self, other_account, how_much):
            self.withdraw(how_much)
            other_account.deposit(how_much)


Notice that if withdrawal is not possible then the function returns `False`. The tests
look like this

    :::python test.py
    import unittest
    from solution import BankAccount
    
    
    class TestBankAccount(unittest.TestCase):
        def setUp(self):
            self.account = BankAccount("Rado", 0)
    
        def test_deposit_positive_amount(self):
            self.account.deposit(1)
            self.assertEqual(self.account._balance, 1)
    
        def test_deposit_negative_amount(self):
            with self.assertRaises(ValueError):
                self.account.deposit(-100)
    
        def test_deposit_zero_amount(self):
            with self.assertRaises(ValueError):
                self.account.deposit(0)
    
        def test_withdraw_positive_amount(self):
            self.account.deposit(100)
    
            result = self.account.withdraw(1)
            self.assertTrue(result)
            self.assertEqual(self.account._balance, 99)
    
        def test_withdraw_maximum_amount(self):
            self.account.deposit(100)
    
            result = self.account.withdraw(100)
            self.assertTrue(result)
            self.assertEqual(self.account._balance, 0)
    
        def test_withdraw_from_empty_account(self):
            result = self.account.withdraw(50)
    
            self.assertIsNotNone(result)
            self.assertFalse(result)
            assert "Withdraw for 50 failed" in self.account._history
    
        def test_withdraw_non_positive_amount(self):
            with self.assertRaises(ValueError):
                self.account.withdraw(0)
    
            with self.assertRaises(ValueError):
                self.account.withdraw(-1)
    
        def test_transfer_negative_amount(self):
            account_1 = BankAccount('For testing', 100)
            account_2 = BankAccount('In dollars', 10)
    
            with self.assertRaises(ValueError):
                account_1.transfer_to(account_2, -50)
    
            self.assertEqual(account_1._balance, 100)
            self.assertEqual(account_2._balance, 10)
    
    
        def test_transfer_positive_amount(self):
            account_1 = BankAccount('For testing', 100)
            account_2 = BankAccount('In dollars', 10)
    
            account_1.transfer_to(account_2, 50)
    
            self.assertEqual(account_1._balance, 50)
            self.assertEqual(account_2._balance, 60)
    
    
    if __name__ == '__main__':
        unittest.main()




Try the following commands to verify that you have 100% coverage

    coverage run test.py
    coverage report
    
    cosmic-ray run --test-runner nose --baseline 10 example.json bank.py -- test.py`
    cosmic-ray report example.json


Can you tell where the bug is ? How about I try to transfer more money than is
available from one account to the other

    :::python
    def test_transfer_more_than_available_balance(self):
        account_1 = BankAccount('For testing', 100)
        account_2 = BankAccount('In dollars', 10)
    
        # transfer more than available
        account_1.transfer_to(account_2, 150)
    
        self.assertEqual(account_1._balance, 100)
        self.assertEqual(account_2._balance, 10)

If you execute the above test it will fail

    FAIL: test_transfer_more_than_available_balance (__main__.TestBankAccount)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "./test.py", line 79, in test_transfer_more_than_available_balance
        self.assertEqual(account_2._balance, 10)
    AssertionError: 160 != 10
    
    ----------------------------------------------------------------------

The problem is that when `self.withdraw(how_much)` fails `transfer_to()` ignores
the result and tries to deposit the money into the other account! A better
implementation would be

    :::python
    def transfer_to(self, other_account, how_much):
        if self.withdraw(how_much):
            other_account.deposit(how_much)
        else:
            raise Exception('Transfer failed!')


In my earlier article the bugs were caused by external environment
and tools/metrics like code coverage and mutation score are not affected by it.
In fact the jinja-ab example falls into the category of data coverage testing.

The current example on the other hand is ignoring the return value of the `withdraw()`
function and that's why it fails when we add the appropriate test.

**NOTE:** some mutation test tools support the *removing/modifying return value*
mutation. Cosmic Ray doesn't support this at the moment (I should add it). Even if it did
that would not help us find the bug because we would kill the mutation using
the `test_withdraw...()` test methods, which already assert on the return value!

Thanks for reading and happy testing!
