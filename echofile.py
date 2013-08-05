#!/usr/bin/python2
#filename is echofile.py

try:
    filename = raw_input('please input the filename : ')
    f = open(filename,'r')
    for line in f:
        print line,
    f.close()
except IOError,e:
    print 'file open error: ',e
