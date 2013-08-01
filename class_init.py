#!/usr/bin/python2
#Filename is class_init.py

class person:
    def __init__(self,name):
        self.name = name 
    def sayhi(self):
        print 'hello,my name is ',self.name

p = person('John')
p.sayhi()


