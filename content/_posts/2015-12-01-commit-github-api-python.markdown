Title: Commit a file with the GitHub API and Python
date: 2015-12-01 12:44
comments: true
Tags: fedora.planet, Python, Django

How do you commit changes to a file using the GitHub API ?
I've found
[this post](http://www.levibotelho.com/development/commit-a-file-with-the-github-api/)
by Levi Botelho which explains the necessary steps but without any code.
So I've used it and created a
[Python example](https://github.com/atodorov/api-commit-test).

I've rearranged the steps so that all write operations follow after a certain
section in the code and also added an intermediate section which creates the
updated content based on what is available in the repository.

I'm just appending
versions of Markdown to the `.travis.yml` (I will explain why in my next post)
and this is hard-coded for the sake of example. All content related operations
are also based on the GitHub API because I want to be independent of the source
code being around when I push this script to a hosting provider.

I've tested this script against itself. In the
[commits log](https://github.com/atodorov/api-commit-test/commits/master)
you can find the *Automatic update to Markdown-X.Y* messages. These are
from the script. Also notice the *Merge remote-tracking branch 'origin/master'*
messages, these appeared when I pulled to my local copy. I believe the
reason for this is that I have some dangling trees and/or commits from
the time I was still experimenting with a broken script. I've tested on another
clean repository and [there are](https://github.com/atodorov/bztest/commits/master)
no such merges.


**IMPORTANT**

For this to work you need to properly authenticate with GitHub. I've crated
a new token at <https://github.com/settings/tokens> with the *public_repo*
permission and that works for me.

