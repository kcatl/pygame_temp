#!/usr/bin/python2
#Filename is try_except.py

import sys

try:
    s = raw_input('Enter something ----> ')
except EOFError:
    print '\nWhy did you do a EOF on me ?'
    sys.exit()#exit the program
except :
    print '\nSome error /exception occured'
    #here we did not exit the program
print 'Done'
