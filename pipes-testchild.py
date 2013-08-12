#!/usr/bin/python2
#filename is pipes-testchild.py
import os ,time, sys
mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('child %d of %d got arg : %s\n'%
        (mypid,parentpid,sys.argv[1]))

for i in range(2):
    time.sleep(3)
    input = raw_input()
    time.sleep(3)
    reply = 'child %d got : [%s]' % (mypid, input)
    print  reply
    sys.stdout.flush()

