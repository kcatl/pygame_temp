#!/usr/bin/python2
#filename is class3.py


class cla1():
    '''this is a __doc__ line for class3.py'''
    version = 0.1

    def __init__(self,nm = 'hello world'):
        self.nm = nm
        print 'created a class named cla1 ',nm

    def showname(self):
        '''display the attribute and the classname '''
        print 'your name is ',self.name
        print 'myname is ',self.__class__.__name__
    def showver(self):
        print 'your class version is : ',self.version
    def addme2me(self,x):
        return x + x
