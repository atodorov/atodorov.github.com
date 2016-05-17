Title: Changing Rails consider_all_requests_local in RSpec fails
Headline: or how to properly test custom error pages
date: 2016-04-27 15:30
comments: true
tags: QA, Ruby
og_image: images/ruby-rails.jpg
twitter_image: images/ruby-rails.jpg

As many others I've been trying to change
`Rails.application.config.consider_all_requests_local` and
`Rails.application.config.action_dispatch.show_exceptions` inside my
RSpec tests in order to test custom error pages in a Rails app. However this
doesn't work. My code looked like this

    :::ruby
    feature 'Exceptions' do
      before do
        Rails.application.config.action_dispatch.show_exceptions = true
        Rails.application.config.consider_all_requests_local = false
      end

This works only if I execute `exceptions_spec.rb` alone. However when something
else executes before that it fails. The config values are
correctly updated but that doesn't seem to have effect.

The answer and solution comes from
[Henrik N](http://thepugautomatic.com/2014/08/404-with-rails-4/#comment-1714338343).

> action_dispatch.show_exceptions gets copied and cached in
> Rails.application.env_config, so even if you change
> Rails.application.config.action_dispatch.show_exceptions in this
> before block the value isn't what you expect when it's used in
> ActionDispatch::DebugExceptions.

In fact `DebugExceptions` uses `env['action_dispatch.show_exceptions']`. The
correct code should look like this

    :::ruby
    before do
      method = Rails.application.method(:env_config)
      expect(Rails.application).to receive(:env_config).with(no_args) do
        method.call.merge(
          'action_dispatch.show_exceptions' => true,
          'action_dispatch.show_detailed_exceptions' => false,
          'consider_all_requests_local' => false
        )
      end
    end

This allows the test to work regardless of the order of execution
of spec files. I don't know why but I also had to leave
`show_detailed_exceptions` otherwise I wasn't getting the desired results.
