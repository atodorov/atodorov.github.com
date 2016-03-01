Title: Puppet for Complete Beginners
date: 2016-03-01 15:08
comments: true
Tags: fedora.planet

I guess everyone knows what [Puppet](https://puppetlabs.com/) is but probably not
everyone knows how to write Puppet modules. This article outlines what I've
learned while adding a new module to an existing Puppet configuration without
having any previous knowledge beforehand and not reading the official
documentation (which I should have done).

Existing setup
---------------

The existing setup is a single git repository, which holds all of the Puppet
configuration for all hosts and environments. The main directory inside the
repo is `puppet/modules`. I wanted to add a few Python scripts which automate
tasks inside [YouTrack](https://www.jetbrains.com/youtrack/).

What to do next
---------------

First step in understanding Puppet was to figure out what do I need to do ?

* Have my scripts inside the repository;
* Provide configuration file for credentials;
* Configure cron jobs;
* Install all of this on one of the existing systems.

My directory layout looks like this

    ./puppet/modules/youtrack/
                            ./files/archive
                            ./manifests/init.pp
                            ./templates/youtrack.conf.erb

`files/` is where all the scripts go. They can be accessed from here later on.
`manifests/init.pp` is the definition of this module - what gets installed where
and so on. `templates/` is where templates go. These are usually config files
which use a placeholder for their values.

My `files/archive` is a simple executable Python script, which queries YouTrack
for old issues and archives them. It looks for a `youtrack.conf` file at a
pre-defined location (the location on the host system) or at environment variables
for testing purposes.

`templates/youtrack.conf.erb` looks like this

    [main]
    url  = <%= scope.lookupvar('common::vars::youtrack_url') %>
    user = <%= scope.lookupvar('common::vars::youtrack_user') %>
    pass = <%= scope.lookupvar('common::vars::youtrack_pass') %>


`manifests/init.pp` looks like this

    class youtrack {
      $youtrack_files =
        '/opt/devops/puppet/modules/youtrack/files'
    
      file { '/opt/youtrack.conf':
        content => template('youtrack/youtrack.conf.erb'),
      }
    
      cron { 'Archive issues older than 2 weeks':
        ensure      => present,
        command     => "cd ${youtrack_files} && ${youtrack_files}/archive",
        environment => [ 'MAILTO=devops@example.com' ],
        user        => 'root',
        minute      => 0,
        hour        => 8,
      }
    }

Once Puppet applies this configuration on the host system it will

* Install the configuration template under `/opt/youtrack.conf`
replacing the placeholder variables with actual values. Notice the
argument to `template()` - it's of the form module_name/file_name;
* Add a cron job entry for my Python script.

**NOTE:** The host system is the Puppet master so I don't really need to
install my Python scripts into another location. I could if I wanted to but
this isn't necessary. Cron is executing the script from inside the git
checkout.

Bundle it all together
----------------------

Our module is done. Now we need to instruct Puppet that we want to use it.
I have a `puppet/modules/role/manifests/pmaster.pp` which defines what modules
get used on the Puppet master machine. `pmaster` matches the hostname of the
system (that's how it's been configured to work). The module looks like this

    class role::pmaster {
      include youtrack
    
      ...
    }

There is also a `puppet/modules/common/manifests/vars-static.pp` file which
defines all the variables used in the templates. Simply add the necessary ones
at the bottom:

    @@ -197,4 +197,9 @@
    +
    +  # YouTrack automation
    +  $youtrack_url  = 'http://example.com'
    +  $youtrack_user = 'changeMe'
    +  $youtrack_pass = 'changeMe'
    }

**NOTE:** in reality this file is just a placeholder. The real values are not
stored in git but are configured manually on systems which need them. On the
Puppet master there are separate `XXX-vars.pp` files for different environments
like devel, staging and production.


