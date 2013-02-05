---
layout: post
title: "Click Tracking without MailChimp"
date: 2013-01-31 21:23
comments: true
categories: ['JavaScript', 'Amazon', 'S3', 'SES']
---

Here is a standard notification message that users at [Difio](http://www.dif.io)
receive. It is plain text, no HTML crap, short and URLs are clean and
descriptive. As the project lead developer I wanted to track when people click on
these links and visit the website but also keep existing functionality.

!["Email with links"](/images/email_w_links.png "Email with links")

Standard approach
------------------

A pretty common approach when sending huge volumes of email is to use an external
service, such as MailChimp. This is one of many email
marketing services which comes with a lot of features. The most important to me
was analytics and reports.

The downside is that MailChimp (and I guess others) use HTML formatted emails
extensively. I don't like that and I'm sure my users will not like it as well. 
They are all developers. Not to mention that MailChimp is much more expensive
than [Amazon SES](http://aws.amazon.com/ses/) which I use currently.
No MailChimp for me!


Another common approach, used by Feedburner by the way,
is to use shortened URLs which redirect to the original ones and measure clicks
in between. I also didn't like this for two reasons: 1) the shortened URLs look
ugly and they are not at all descriptive and 2) I need to generate them automatically
and maintain all the mappings. Why bother ?


How I did it? 
--------------

So I needed something which will do a redirect to a predefined URL, measure how many
redirects were there (essentially clicks on the link) and look nice. The solution is
very simple, if you have not recognized it by now from the picture above. 

I opted for a custom redirect engine, which will add tracking information to the
destination URL so I can track it in Google Analytics.

Previous URLs were of the form `http://www.dif.io/updates/haml-3.1.2/haml-3.2.0.rc.3/11765/`.
I've added the humble `/daily/?` prefix before the URL path so it becomes
`http://www.dif.io/daily/?/updates/haml-3.1.2/haml-3.2.0.rc.3/11765/`


Now `/updates/haml-3.1.2/haml-3.2.0.rc.3/11765/` becomes a query string parameter which
the `/daily/index.html` page uses as its destination. Before doing the redirect
a script adds tracking parameters so that Google Analytics will properly
report this visit. Here is the code: 

{% codeblock lang:html %}
<html>
<head>
<script type="text/javascript">
// (c) 2013 - Alexander Todorov, http://atodorov.org
// Published under GNU GPLv3

var uri = window.location.toString();
var question = uri.indexOf("?");
var param = uri.substring(question + 1, uri.length)
if (question > 0) {
    window.location.href = param + '?utm_source=email&utm_medium=email&utm_campaign=Daily_Notification';
}
</script>
</head>
<body></body>
</html>
{% endcodeblock %}

Previously Google Analytics was reporting these visits as direct hits while now it lists them under
campaigns like so:

!["Difio Analytics"](/images/analytics_difio_campaigns.png "Difio Analytics")


Because all visitors of [Difio](http://www.dif.io) use JavaScript enabled browsers
I combined this approach with another one, to
[remove query string with JavaScript](/blog/2013/01/28/remove-query-string-with-javascript-and-html5/)
and present clean URLs to the visitor.


Why JavaScript?
---------------

You may be asking why the hell I am using JavaScript and not Apache's wonderful mod_rewrite module? 
This is because the destination URLs are hosted in [Amazon S3](http://aws.amazon.com/s3/) and I'm
planning to integrate with [Amazon CloudFront](http://aws.amazon.com/cloudfront/). Both of them
don't support .htaccess rules nor anything else similar to mod_rewrite.




As always I'd love to hear your thoughts and feedback. Please use the comment form below.






