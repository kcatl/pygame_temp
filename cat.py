#!/usr/bin/python2
#Filename is cat.py

import sys
import time

def readfile(filename):
    '''print a file to standard out'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
    f.close()
#scripts starts here
if len(sys.argv) < 2:
    print 'No action specified'
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version : 1.0'
    elif option == 'help':
        print '''\
                this is a help line for cat.py
                '''
    else:
        print 'Unknown option'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)

