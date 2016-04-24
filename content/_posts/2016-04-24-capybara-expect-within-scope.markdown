Title: Capybara's within() Altering expect(page) Scope
date: 2016-04-24 23:50
comments: true
categories: QA, Ruby
og_image: images/capybara-20clipart-hamster3.png
twitter_image: images/capybara-20clipart-hamster3.png

**
When making assertions inside a `within` block the assertion scope
is limited to the element selected by the *within()* function, although
it looks like you are asserting on the entire page!
**

    :::ruby
    scenario 'Pressing Escape closes autocomplete popup' do
      within('#new-broadcast') do
        find('#broadcast_field').set('Hello ')
          start_typing_name('#broadcast_field', '@Bret')
          # will fail below
          expect(page).to have_selector('.ui-autocomplete')
          send_keys('#broadcast_field', :escape)
      end
      expect(page).to have_no_selector('.ui-autocomplete')
    end

The above code failed the first `expect()` and it took me some time before
I figured it out. Capybara's test suite itself gives you the answer

    :::ruby
    it "should assert content in the given scope" do
      @session.within(:css, "#for_foo") do
        expect(@session).not_to have_content('First Name')
      end
      expect(@session).to have_content('First Name')
    end


So know your frameworks and happy testing.
