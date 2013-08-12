#!/usr/bin/python2
#filename is thread-count-mutex.py

import thread ,time

def counter(myId ,count):
    for i in range(count):
        mutex.acquire()
#        time.sleep(1)
        print '[%s] ---> %s' %(myId ,i)
        mutex.release()

mutex = thread.allocate_lock()
for i  in range(10):
    thread.start_new_thread(counter, (1,3))

time.sleep(6)
print 'Main thread exiting '

