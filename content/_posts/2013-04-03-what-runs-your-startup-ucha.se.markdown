---
layout: post
Title: What Runs Your Start-up - Ucha.se
date: 2013-04-03 10:57
comments: true
Tags: 'what runs', 'start-up', 'PHP', 'MySQL', 'jQuery', 'Nginx'
---

<img src="/images/startup/uchase.jpg" alt="Ucha.se logo" style="float:left;margin-right:10px;"/>


[Ucha.se](http://ucha.se/) makes learning fun. It is an online platform,
on which pupils and students learn and prepare for school. Pupils learn faster,
improve their results and get inspired. The platform allows students to watch
videos, take tests, ask questions and share comments. Learning is represented
with gamification components like drawings, playful narration, dashboards with
the best students, etc. It is available on the web and is extending to mobile.
Ucha.se is well recognized by the parents and teachers in Bulgaria.
In November 2012 Ucha.se was awarded as the best website in Bulgaria in the
field of Education and Science.

Nikolay Zheynov is leading the IT team which maintains and expands the web platform.
He shared with me some of the internals.

Main Technologies
----------------

Main technologies used are PHP, MySQL, Nginx, jQuery and jQueryUI.


Server-side development is done with PHP 5. The main reason for choosing PHP is
that the IT team working on the platform had long experience with the language.
Ucha.se has developed their own PHP framework which is constantly expanding.
This allows flexible programming and easier application maintenance.
Nginx is the web server of choice.

MySQL 5 is used for the database because PHP + MySQL is like bread and butter.
While the site usage was growing the team had to optimize their DB layer and switched
from MyISAM storage engine to InnoDB.

On the client-side standard web technologies are used - HTML5, CSS3 and JavaScript.
The main goal when doing the website design was to match expectation from different
user groups - pupils, teachers, parents and students.
jQuery and jQueryUI are widely used on the client side.


Why Not Something Else?
-----------------------

{% blockquote Nikolay Zheynov %}
True to our agile approach to incrementally enhance the product and the technology
that goes along with it, we strongly believe in the scaling on demand practices.
Ucha.se's own framework reflects exactly to that. It allows us to meet our growing
user demands and provides at the same time, the dev-team with enough flexibility to
quickly react on new business opportunities and technological (r)evolutions.
{% endblockquote %}

Want More Info?
---------------

If you’d like to hear more from *Ucha.se* please comment below.
I will ask them to follow this thread and reply to your questions.
