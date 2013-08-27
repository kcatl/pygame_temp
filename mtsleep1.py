#!/usr/bin/python2

from time import sleep, ctime
import thread

def loop0():
    print 'start loop0 at :' ,ctime()
    sleep(4)
    print 'loop0 end at :' ,ctime()

def loop1():
    print 'start loop1 at :',ctime()
    sleep(2)
    print 'end loop1 at :',ctime()

def main():
    print 'starting at time :',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all Done at time : ',ctime()

if __name__ == '__main__':
    main()

