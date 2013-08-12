#!/usr/bin/python2
#filename is testexit_thread.py

import thread

exitstat = 0

def child():
    global exitstat
    exitstat = exitstat + 1
    threadid = thread.get_ident()
    print 'Hello from child',threadid,exitstat
    thread.exit()
    print 'Never reached'

def parent():
    while 1:
        thread.start_new_thread(child, ())
        if raw_input() == 'q':break

parent()


