Title: What's the bug in this pseudo-code
Headline: by Rails Girls Vratsa
date: 2017-06-26 13:30
comments: true
Tags: fedora.planet, QA, Ruby
og_image: images/bug_rails_girls_vratsa.jpg
twitter_image: images/bug_rails_girls_vratsa.jpg

![Rails Girls Vratsa sticker](/images/bug_rails_girls_vratsa.jpg "Rails Girls Vratsa sticker")

This is one of the stickers for the second edition of Rails Girls Vratsa which
was held yesterday. Let's explore some of the bug proposals submitted by the Bulgarian QA group:

> 
> 1. sad() == true is ugly
> 2. sad() is not very nice, better make it if(isSad())
> 3. use sadStop(), and even better - stopSad()
> 4. there is an extra space character in beAwesome( )
> 5. the last curly bracket needs to be on a new line
> 
> Lyudmil Latinov

My friend Lu describes what I would call style issues. The style he refers to
is mostly Java oriented, especially with naming things. In Ruby we would probably
go with `sad?` instead of `isSad`. Style is important and there are many tools
to help us with that this will not cause a functional problem! While I'm at it let me say
the curly brackets are not the problem either. They are not valid in Ruby this is
a pseudo-code and they also fall in the style category.

The next interesting proposal comes from Tsveta Krasteva. She examines the possibility
of `sad()` returning an object or nil instead of boolean value. Her first question was
will the if statement still work, and the answer is yes. In Ruby everything is an object
and every object can be compared to `true` and `false`. See
[Alan Skorkin's](http://www.skorks.com/2009/09/true-false-and-nil-objects-in-ruby/) blog
post on the subject.

Then Tsveta says the answer is to use `sad().stop()` with the warning that it may return
nil. In this context the `sad()` method returns on object indicating that the person
is feeling sad. If the method returns nil then the person is feeling OK.

    :::ruby example by Tsveta
    class Csad
      def stop()
        print("stop\n");
      end
    end
    
    def sad()
      print("sad\n");
      Csad.new();
    end
    
    def beAwesome()
      print("beAwesome\n");
    end
    
    # notice == true was removed
    if(sad())
      print("Yes, I am sad\n");
      sad.stop();
      beAwesome( );
    end


While this is coming closer to a functioning solution something about it is bugging me.
In the if statement the developer has typed more characters than required (`== true`).
This sounds to me unlikely but is possible with less experienced developers.
The other issue is that we are using an object (of `class Csad`) to represent an internal
state in the system under test. There is one method to return the state (`sad()`) and
another one to alter the state (`Csad.stop()`). The two methods don't operate on
the same object! Not a very strong OOP design. On top of that we have to call the
method twice, first time in the if statement, the second time in the body of the
if statement, which may have unwanted side effects. It is best to assign the return
value to some variable instead.

IMO if we are to use this OOP approach the code should look something like:

    :::
    class Person
      def sad?()
      end
    
      def stopBeingSad()
      end
    
      def beAwesome()
      end
    end
    
    p = Person.new
    if p.sad?
        p.stopBeingSad
        p.beAwesome
    end


Let me return back to assuming we don't use classes here.
The first *obvious* mistake is the space in `sad stop();` first spotted by Peter Sabev*.
His proposal, backed by others is to use `sad.stop()`. However they
didn't use my hint asking what is the return value of `sad()` ?


If `sad()` returns boolean then we'll get
`undefined method 'stop' for true:TrueClass (NoMethodError)`!
Same thing if `sad()` returns nil, although we skip the if block in this case.

In Ruby we are allowed to skip parentheses when calling a method, like I've shown
above. If we ignore this fact for a second, then `sad?.stop()` will mean execute the
method named `stop()` which is a member of the `sad?` variable, which is of type method!
Again, methods don't have an attribute named `stop`!

The last two paragraphs are the semantic/functional mistake I see in this code. The only way
for it to work is to use an OOP variant which is further away from what the existing
clues give us.

**Note:** The variant `sad? stop` is syntactically correct. This means call the function `sad?`
with parameter `stop`, which depending on the outer scope of this program may or may not
be correct (e.g. `stop` is defined, `sad?` accepts optional parameters, `sad?` maintains
global state).

Thanks for reading and happy testing!
