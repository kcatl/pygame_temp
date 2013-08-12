#!/usr/bin/python2
#filename is thread_count.py

import thread , time

def counter(myId,count):
    for i in range(count):
#        time.sleep(1)
        print '[%s] ==> %s' % (myId, i)
        
for i in range(10):
    thread.start_new(counter,(i, 3))

time.sleep(4)

print 'Main thread exiting.'
