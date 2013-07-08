---
layout: post
title: "Tip: Setting Secure ENV variables on Red Hat OpenShift"
date: 2013-07-08 21:39
comments: true
categories: ['tips', 'OpenShift', 'cloud']
---

OpenShift is
[still missing](https://www.openshift.com/content/custom-environment-variables)
the client side tools to set environment variables without exposing the values
in source code but there is a way to do it. Here is how.


First ssh into your application and navigate to the `$OPENSHIFT_DATA_DIR`.
Create a file to define your environment. 

{% codeblock lang:bash %}
$ rhc ssh -a difio
Password: ***

[difio-otb.rhcloud.com 51d32a854382ecf7a9000116]\> cd $OPENSHIFT_DATA_DIR
[difio-otb.rhcloud.com data]\> vi myenv.sh
[difio-otb.rhcloud.com data]\> cat myenv.sh
#!/bin/bash
export MYENV="hello"

[difio-otb.rhcloud.com data]\> chmod a+x myenv.sh 
[difio-otb.rhcloud.com data]\> exit
Connection to difio-otb.rhcloud.com closed.
{% endcodeblock %}

Now modify your code and git push to OpenShift. Then ssh into the app once
again to verify that your configuration is still in place. 

{% codeblock lang:bash %}
[atodorov@redbull difio]$ rhc ssh -a difio
Password: ***

[difio-otb.rhcloud.com 51d32a854382ecf7a9000116]\> cd $OPENSHIFT_DATA_DIR
[difio-otb.rhcloud.com data]\> ls -l
total 4
-rwxr-xr-x. 1 51d32a854382ecf7a9000116 51d32a854382ecf7a9000116 34  8 jul 14,33 myenv.sh
[difio-otb.rhcloud.com data]\> 

{% endcodeblock %}


Use the defined variables as you wish.
