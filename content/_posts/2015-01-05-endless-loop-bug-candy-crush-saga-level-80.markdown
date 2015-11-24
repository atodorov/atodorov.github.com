---
layout: post
Title: Endless Loop Bug in Candy Crush Saga Level 80
date: 2015-01-05 15:44
comments: true
categories: ['QA']
---

Happy new year everyone. During the holidays I've discovered several interesting
bugs which will be revealed in this blog. Starting today with a bug in the popular
game *Candy Crush Saga*.

In level 80 one teleport is still open but the chocolates are blocking the rest.
The game has ended but candies keep flowing through the teleport and the level doesn't exit.
My guess is that the game logic is missing a check whether or not it will go into an endless loop.

<iframe width="560" height="315" src="//www.youtube.com/embed/haBepFwyaxY" frameborder="0" allowfullscreen></iframe>

This bug seems to be generic for the entire game. It pops up also on
level 137 in the Owl part of the game (recorded by somebody else):

<iframe width="420" height="315" src="//www.youtube.com/embed/6q1_LIdamqw" frameborder="0" allowfullscreen></iframe>

