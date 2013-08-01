#!/usr/bin/python2
#Filename is raising.py

class ShortInputException(Exception):
    '''A user defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something --->')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
    #other work can continue asusal here
except EOFError:
    print '\n Why did you do a EOF error on me '
except ShortInputException,x:
    print 'ShortInputException:The input of the length %d,\
            was expecting at least %d'%(x.length,x.atleast)
else:
    print 'No exception was raised'

