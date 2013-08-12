#!/usr/bin/python2
#filename is fork1.py

import os

def child():
    print 'hello from child', os.getpid()
    os._exit(0) #else back to parent loop

def parent():
    while 1:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print 'hello from parent',os.getpid(), newpid
        if raw_input() == 'q' : break

parent()

