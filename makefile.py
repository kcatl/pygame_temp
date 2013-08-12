#!/usr/bin/env python2
#filename is makefile.py

'maketextfile.py -----creat a text file with python'
import os 
ls = os.linesep

#get filename 
fname = 'fname.txt'
while True:
    if os.path.exists(fname):
        print 'ERROR : "%s" already exist'% fname
    else:
        break
#get file content lines
all = []
print '\nEnter lines("." by itself to quit).\n'

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)
#while lines to file with a proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'Done!'

