#!/usr/bin/python2
#filename is ueuetest.py

numconsumers = 2 
numproducers = 4
nummessages = 4
import thread ,Queue ,time
safeprint = thread.allocate_lock()
dataQueue = Queue.Queue()

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('producer %d:%d' % (idnum , msgnum))

def consumer(idnum):
    while 1:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block = False)
        except Queue.Empty:
            pass
        else:
            safeprint.acquire()
            print 'consumer',idnum, 'got ==>',data
            safeprint.release()

if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers -1) * nummessages ) + 1)

