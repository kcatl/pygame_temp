#!/usr/bin/python2
#filename is fork-exec.py

import os
parm = 0

while 1:
    parm = parm + 1
    pid = os.fork()
    if pid == 0:
        os.execlp('python2','python2','hello.py','str(parm)')
        assert False ,'error starting program'
    else:
        print 'Child is ',pid 
        if raw_input() == 'q':break


