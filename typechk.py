#!/usr/bin/python2
#filename is typechk.py

def displayNumType(num):
    print num ,'is'
    if isinstance(num, (int,long,float,complex)):
        print 'a number of the type : ',type(num).__name__
    else:
        print 'not a number at all !!! '
displayNumType(-69)

displayNumType(9999999999999999999999999999999999)

displayNumType(98.6)

displayNumType(-5.2 + 2.3j)

displayNumType('xxx')
