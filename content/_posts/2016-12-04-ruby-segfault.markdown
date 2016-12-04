Title: Overridden let() causes segfault with RSpec
Headline: easy to happen with shared examples
date: 2016-12-04 22:48
comments: true
Tags: Ruby, QA, fedora.planet
og_image: images/segfault.jpg
twitter_image: images/segfault.jpg

Last week [Anton](https://github.com/syndbg) asked me to take a look at one of
his RSpec test suites. He was able to consistently reproduce a segfault which
looked like this:

    /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:113: [BUG] vm_call_cfunc - cfp consistency error
    ruby 2.3.2p217 (2016-11-15 revision 56796) [x86_64-linux]
    
    -- Control frame information -----------------------------------------------
    c:0013 p:---- s:0048 e:000047 CFUNC  :map
    c:0012 p:0011 s:0045 e:000044 BLOCK  /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:113
    c:0011 p:0035 s:0043 e:000042 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/configuration.rb:1835
    c:0010 p:0011 s:0040 e:000039 BLOCK  /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:112
    c:0009 p:0018 s:0037 e:000036 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/reporter.rb:77
    c:0008 p:0022 s:0033 e:000032 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:111
    c:0007 p:0025 s:0028 e:000027 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:87
    c:0006 p:0085 s:0023 e:000022 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:71
    c:0005 p:0026 s:0016 e:000015 METHOD /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/lib/rspec/core/runner.rb:45
    c:0004 p:0025 s:0012 e:000011 TOP    /home/atodorov/.rbenv/versions/2.3.2/lib/ruby/gems/2.3.0/gems/rspec-core-3.5.4/exe/rspec:4 [FINISH]
    c:0003 p:---- s:0010 e:000009 CFUNC  :load
    c:0002 p:0136 s:0006 E:001e10 EVAL   /home/atodorov/.rbenv/versions/2.3.2/bin/rspec:22 [FINISH]
    c:0001 p:0000 s:0002 E:0000a0 (none) [FINISH]

Googling for `vm_call_cfunc - cfp consistency error` yields
[Ruby #10460](https://bugs.ruby-lang.org/issues/10460). Comments on the bug and
particularly this one point towards the error:

    > Ruby is trying to be nice about reporting the error; but in the end,
    > your code is still broken if it overflows stack.

Somewhere in the test suite was a piece of code that was overflowing the stack.
It was somewhere along the lines of

    :::ruby
    describe '#active_client_for_user' do
      context 'matching an existing user' do
        it_behaves_like 'manager authentication' do
          include_examples 'active client for user with existing user'
        end
      end
    end

Considering the examples in the bug I started looking for patterns where a variable
was defined and later redefined, possibly circling back to the previous definition.
Expanding the shared examples by hand transformed the code into

    #!ruby
    describe '#active_client_for_user' do
      context 'matching an existing user' do
        let(:user) { create(:user, :manager) }
        let!(:api_user_authentication) { create(:user_authentication, user: user) }
        let(:user) { api_user_authentication.user }
    
        context 'with an `active_assigned_client`' do
          ... skip ...
        end
    
        ... skip ...
      end
    end


Line 5. overrode line 3. When line 4. was executed first because of lazy execution
and the call execution path became: 4-5-4-5-4-5 ... **NOTE:** I think we need a
warning about that in RuboCop, see
[RuboCop #3769](https://github.com/bbatsov/rubocop/issues/3769).
The fix however is a no brainer:

    :::diff
    -  let(:user) { create(:user, :manager) }
    -  let!(:api_user_authentication) { create(:user_authentication, user: user) }
    +  let(:manager) { create(:user, :manager) }
    +  let!(:api_user_authentication) { create(:user_authentication, user: manager) }

Thanks for reading and happy testing.
