Title: Controlling Interactive Terminal Programs
date: 2016-01-14 16:03
comments: true
Tags: fedora.planet, QA

Building on my previous experience about
[capturing terminal output from other processes]({filename}2015-12-25-capture-terminal-output-from-other-processes.markdown)
I wanted to create an automated test case for the initial-setup-text service
which would control `stdin`. Something like
[Dogtail](https://fedorahosted.org/dogtail/) but for text mode applications.

What you have to do is attach `gdb` to the process. Then you can `write` to
any file descriptor that is already opened. **WARNING:** writing directly to
stdin didn't quite work! Because (I assume) stdin is a tty the text was shown on
the console but the return character wasn't interpreted and the application wasn't
accepting the input string. What I had to do is replace the tty with a pipe and
it worked. However the input is not duplicated on the console this way!

Another drawback is that I couldn't use `strace` to log the output in combination
with `gdb`. Once a process is under trace you can't trace it a second time! For this
simple test I was able to live with this by not inspecting the actual text printed
by initial-setup. Instead I'm validating the state of the system after setup is
complete. I've tried to `read` from `stdout` in gdb but that didn't work either.
If there's a way to make this happen I can convert this script to a mini-framework.

Another unknown is interacting with `passwd`. Probably for security reasons
it doesn't allow to mess around with its stdin but I didn't investigate deeper.


I've used the
[fdmanage.py](https://github.com/ticpu/tools/blob/master/fdmanage.py)
script which does most of the work for me. I've removed the extra bits
that I didn't need, added the `write()` method and removed the original call to
`fcntl` which puts gdb.stdout into non-blocking mode (that didn't work for me).

    :::python initial_setup_driver.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    # fdmanage.py is a program to manage file descriptors of running programs
    # by using GDB to modify the running program.
    # https://github.com/ticpu/tools/blob/master/fdmanage.py
    # Copyright (C) 2015 Jérôme Poulin <jeromepoulin@gmail.com>
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
    #
    # Copyright (c) 2016 Alexander Todorov <atodorov@redhat.com>
    
    from __future__ import unicode_literals
    
    import os
    import sys
    import select
    import subprocess
    
    
    class Gdb(object):
        def __init__(self, pid, verbose=False):
            pid = str(pid)
    
            self.gdb = subprocess.Popen(
                ["gdb", "-q", "-p", pid],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                close_fds=True,
            )
            self.pid = pid
            self.verbose = verbose
    
        def __enter__(self):
            return self
    
        def __exit__(self, exc_type, exc_val, exc_tb):
            del exc_type, exc_val, exc_tb
    
            self.send_command("detach")
            self.send_command("quit")
            self.gdb.stdin.close()
            self.gdb.wait()
    
            if self.verbose:
                print(self.gdb.stdout.read())
                print("\nProgram terminated.")
    
        def send_command(self, command):
            self.gdb.stdin.write(command.encode("utf8") + b"\n")
            self.gdb.stdin.flush()
    
        def send_command_expect(self, command):
            self.send_command(command)
            while True:
                try:
                    data = self.gdb.stdout.readline().decode("utf8")
                    if self.verbose:
                        print(data)
                    if " = " in data:
                        return data.split("=", 1)[-1].strip()
                except IOError:
                    select.select([self.gdb.stdout], [], [], 0.1)
    
        def close_fd(self, fd):
            self.send_command("call close(%d)" % int(fd))
    
        def dup2(self, old_fd, new_fd):
            self.send_command("call dup2(%d, %d)" % (int(old_fd), int(new_fd)))
    
        def open_file(self, path, mode=66):
            fd = self.send_command_expect('call open("%s", %d)' % (path, mode))
    
            return fd
    
        def write(self, fd, txt):
            self.send_command('call write(%d, "%s", %d)' % (fd, txt, len(txt)-1))
    
    if __name__ == "__main__":
        import time
        import tempfile
    
        # these are specific to initial-setup-text
        steps = [
            "1\\n", # License information
            "2\\n", # Accept license
            "c\\n", # Continue back to the main hub
    
            "3\\n",  # Timezone settings
            "8\\n",  # Europe
            "43\\n", # Sofia
    
    # passwd doesn't allow us to overwrite its file descriptors
    # either aborts or simply doesn't work
    #        "4\\n",      # Root password
    #        "redhat\\n",
    #        "redhat\\n",
    #        "no\\n",     # password is weak
    #        "123\\n",
    #        "123\\n",
    #        "no\\n",     # password is too short
    #        "Th1s-Is-a-Str0ng-Password!\\n",
    #        "Th1s-Is-a-Str0ng-Password!\\n",
    
            "c\\n", # Continue to exit
        ]
    
        if len(sys.argv) != 2:
            print "USAGE: %s <PID>" % __file__
            sys.exit(1)
    
        tmp_dir = tempfile.mkdtemp()
        pipe = os.path.join(tmp_dir, "pipe")
        os.mkfifo(pipe)
    
        with Gdb(sys.argv[1], True) as gdb:
            fd = gdb.open_file(pipe, 2) # O_RDWR
            gdb.dup2(fd, 0) # replace STDIN with a PIPE
            gdb.close_fd(fd)
    
            # set a breakpoint before continuing
            break_point_num = gdb.send_command_expect("break read")
    
            # now execute the process step-by-step
            i = 0
            len_steps = len(steps)
            for txt in steps:
                gdb.write(0, txt)
                time.sleep(1)
                i += 1
                if i == len_steps - 1:
                    gdb.send_command("delete %s" % break_point_num)
                gdb.send_command("continue")
                time.sleep(1)
    
        # clean up
        os.unlink(pipe)
        os.rmdir(tmp_dir)
