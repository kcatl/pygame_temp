#!/usr/bin/python2
# Filename is docstring1.py

def func(x):
    '''hello world
    this is a doc string '''
    print x 
print func.__doc__
func(2)
