Title: Beware of Double Stubs in RSpec
date: 2016-03-31 12:08
comments: true
og_image: /images/double-dip.jpg
Tags: fedora.planet, Ruby, QA

I've been re-factoring some RSpec tests and encountered a method which has been
stubbed-out 2 times in a row. This of course led to problems when I tried to delete
some of the code, which I deemed unnecessary. Using
[Treehouse's burger example](http://blog.teamtreehouse.com/an-introduction-to-rspec)
I've recreated my use-case. Comments are in the code below:

    :::ruby burger_spec.rb
    class Burger
      attr_reader :options
    
      def initialize(options={})
        @options = options
      end
    
      def apply_ketchup(number=0)
        @ketchup = @options[:ketchup]
        # the number is passed from the tests below to make it easier to
        # monitor execution of this method.
        printf "Ketchup applied %d times\n", number
      end
    
      def apply_mayo_and_ketchup(number=0)
        @options[:mayo] = true
        apply_ketchup(number)
      end
    
      def has_ketchup_on_it?
        @ketchup
      end
    end
    
    describe Burger do
      describe "#apply_mayo_and_ketchup" do
        context "with ketchup and single stubs" do
          let(:burger) { Burger.new(:ketchup => true) }
    
          it "1: sets the mayo flag to true, ketchup is nil" do
            # this line stubs-out the apply_ketchup method
            # and @ketchup will remain nil b/c the original
            # method is not executed at all
            expect(burger).to receive(:apply_ketchup)
            burger.apply_mayo_and_ketchup(1)
    
            expect(burger.options[:mayo]).to eq(true)
            expect(burger.has_ketchup_on_it?).to be(nil)
          end
    
          it "2: sets the mayo and ketchup flags to true" do
            # this line stubs-out the apply_ketchup method
            # but in the end calls the non-stubbed out version as well
            # so that has_ketchup_on_it? will return true !
            expect(burger).to receive(:apply_ketchup).and_call_original
            burger.apply_mayo_and_ketchup(2)
    
            expect(burger.options[:mayo]).to eq(true)
            expect(burger.has_ketchup_on_it?).to eq(true)
          end
        end
    
        context "with ketchup and double stubs" do
          let(:burger) { Burger.new(:ketchup => true) }
          before {
            # this line creates a stub for the apply_ketchup method
            allow(burger).to receive(:apply_ketchup)
          }
    
          it "3: sets the mayo flag to true, ketchup is nil" do
            # this line creates a second stub for the fake apply_ketchup method
            # @ketchup will remain nil b/c the original method which sets its value
            # isn't actually executed. we may as well comment out this line and
            # this will not affect the test at all
            expect(burger).to receive(:apply_ketchup)
            burger.apply_mayo_and_ketchup(3)
    
            expect(burger.options[:mayo]).to eq(true)
            expect(burger.has_ketchup_on_it?).to be(nil)
          end
    
          it "4: sets the mayo and ketchup flags to true" do
            # this line creates a second stub for the fake apply_ketchup method.
            # .and_call_original will traverse up the stubs and call the original
            # method. If we don't want to assert that the method has been called
            # or we don't care about its parameters, but only the end result
            # that system state has been changed then this line is redundant!
            # Don't stub & call the original, just call the original method, right?
            # Commenting out this line will cause a failure due to the first stub
            # in before() above. The first stub will execute and @ketchup will remain
            # nil! To set things straight also comment out the allow() line in
            # before()!
            expect(burger).to receive(:apply_ketchup).and_call_original
            burger.apply_mayo_and_ketchup(4)
    
            expect(burger.options[:mayo]).to eq(true)
            expect(burger.has_ketchup_on_it?).to eq(true)
          end
        end
      end
    end

When I see a `.and_call_original` method
after a stub I immediately delete it because in most of the cases this isn't
necessary. Why stub out something just to call it again later ? See my comments
above. Also the `expect to receive && do action`
sequence is a bit counter intuitive. I prefer the `do action & assert results`
sequence instead.


The problem here comes from the fact that RSpec has very flexible syntax for
creating stubs which makes it very easy to abuse them, especially when you
have no idea what you're doing. If you write tests with RSpec please make a
note of this and try to avoid this mistake.

If you'd like to learn more about stubs see
[Bad Stub Design in DNF]({filename}2015-11-23-bad-stub-design-in-dnf.markdown).
