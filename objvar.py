#!/usr/bin/python2
#Filename is objvar.py

class Person:
   '''Repressents a person'''
    population = 0

    def __init__(self,name):
        '''Initializes the person's data'''
        self.name = name 
        print '(Initializing %s)'% self.name
    #when the person has created ,he/she
    #add to the population
    Person.population += 1

    def __del__(self):
    '''I am dying '''
    print '%s ,say goodbye'% self.name
    Person.population -= 1

    if Person.population == 0:
        print 'I am the last one '
    else :
        print 'there is still %d people there'% Person.population
    def sayHi(self):
    '''Greating by the person'''
    print 'Hi,my name is %s' % self.name
    def howmany(self):
    if Person.population == 1:
        print 'I am the only person there'
    else:
        print 'We have %s person there'% Person.population


swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howmany()

kalam = Person('Kalam')
kalam.sayHi()
kalam.howmany()

swaroop.sayHi()
swaroop.howmany()


