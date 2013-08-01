#!/usr/bin/python2
#Filename is docstring.py

def printMax(x,y):
   '''Print the maximum of the two numbers.
    The two numbers must be integers'''

    x = int(x)
    y = int(y)

    if x > y :
        print x ,'is the maximum one '
    else:
        print y ,'is the maximum one '
printMax(3,5)
print printMax.__doc__
