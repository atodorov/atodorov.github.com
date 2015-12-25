Title: Capture Terminal Output From Other Processes
date: 2015-12-25 12:03
comments: true
Tags: fedora.planet, QA

I've been working on a test case to verify that Anaconda will print its EULA
notice at the end of a text mode installation. The problem is how do you capture
all the text which is printed to the terminal from processes outside your control ?
The answer is surprisingly simple - using strace! 

    %post --nochroot
    PID=`ps aux | grep "/usr/bin/python /sbin/anaconda" | grep -v "grep" | tr -s ' ' | cut -f2 -d' '`
    STRACE_LOG="/mnt/sysimage/root/anaconda.strace"
    
    # see https://fedoraproject.org/wiki/Features/SELinuxDenyPtrace
    setsebool deny_ptrace 0
    
    # EULA notice is printed after post-scripts are run
    strace -e read,write -s16384 -q -x -o $STRACE_LOG -p $PID -f >/dev/null 2>&1 &


strace is tracing only read and write events (we really only need write) and
extending the maximum string size printed in the log file. For a simple grep
this is sufficient. If you need to pretty-print the strace output have a look
at the [ttylog](http://search.cpan.org/~bbb/ttylog/ttylog) utility.
