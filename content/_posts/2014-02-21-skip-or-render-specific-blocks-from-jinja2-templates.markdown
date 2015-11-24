---
layout: post
Title: Skip or Render Specific Blocks from Jinja2 Templates
date: 2014-02-21 00:08
comments: true
categories: ['Python', 'Django', 'Fedora']
---

I wasn't able to find detailed information on how to skip rendering
or only render specific blocks from Jinja2 templates so here's my solution.
Hopefully you find it useful too.

With below template I want to be able to render **only** *kernel_options* block
as a single line and then render the rest of the template **excluding** *kernel_options*.

{% codeblock lang:jinja base.j2 %}
{% raw %}
{% block kernel_options %}
console=tty0
    {% block debug %}
        debug=1
    {% endblock %}
{% endblock kernel_options %}

{% if OS_MAJOR == 5 %}
key --skip
{% endif %}

%packages
@base
{% if OS_MAJOR > 5 %}
%end
{% endif %}
{% endraw %}
{% endcodeblock %}


To render a particular block you have to use the low level Jinja API
*[template.blocks](http://jinja.pocoo.org/docs/api/#jinja2.Template.blocks)*.
This will return a dict of block rendering functions which need a *Context* to work with.

The second part is trickier. To remove a block we have to create an extension
which will filter it out. The provided *SkipBlockExtension* class does
exactly this.


Last but not least - if you'd like to use both together you have to disable
caching in the *Environment* (so you get a fresh template every time), render
your blocks first, configure *env.skip_blocks* and render the entire template
without the specified blocks.


{% codeblock lang:python jinja2-render %}
#!/usr/bin/env python

import os
import sys
from jinja2.ext import Extension
from jinja2 import Environment, FileSystemLoader


class SkipBlockExtension(Extension):
    def __init__(self, environment):
        super(SkipBlockExtension, self).__init__(environment)
        environment.extend(skip_blocks=[])

    def filter_stream(self, stream):
        block_level = 0
        skip_level = 0
        in_endblock = False

        for token in stream:
            if (token.type == 'block_begin'):
                if (stream.current.value == 'block'):
                    block_level += 1
                    if (stream.look().value in self.environment.skip_blocks):
                        skip_level = block_level

            if (token.value == 'endblock' ):
                in_endblock = True

            if skip_level == 0:
                yield token

            if (token.type == 'block_end'):
                if in_endblock:
                    in_endblock = False
                    block_level -= 1

                    if skip_level == block_level+1:
                        skip_level = 0


if __name__ == "__main__":
    context = {'OS_MAJOR' : 5, 'ARCH' : 'x86_64'}

    abs_path  = os.path.abspath(sys.argv[1])
    dir_name  = os.path.dirname(abs_path)
    base_name = os.path.basename(abs_path)

    env = Environment(
                loader = FileSystemLoader(dir_name),
                extensions = [SkipBlockExtension],
                cache_size = 0, # disable cache b/c we do 2 get_template()
            )

    # first render only the block we want
    template = env.get_template(base_name)
    lines = []
    for line in template.blocks['kernel_options'](template.new_context(context)):
        lines.append(line.strip())
    print "Boot Args:", " ".join(lines)
    print "---------------------------"

    # now instruct SkipBlockExtension which blocks we don't want
    # and get a new instance of the template with these blocks removed
    env.skip_blocks.append('kernel_options')
    template = env.get_template(base_name)
    print template.render(context)
    print "---------------------------"
{% endcodeblock %}


The above code results in the following output:

    $ ./jinja2-render ./base.j2 
    Boot Args: console=tty0 debug=1 
    ---------------------------
    
    key --skip
    
    %packages
    @base
    ---------------------------


Teaser: this is part of my effort to replace SNAKE with a client side
kickstart template engine for
[Beaker](/blog/2013/11/19/open-source-quality-assurance-infrastructure-for-fedora-qa/)
so stay tuned!
