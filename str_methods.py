#!/usr/bin/python2
#Filename is str_methods.py

name = 'Swaroop'
if name.startswith('Swa'):
    print 'yes,the string start with "Swa"'
if 'a' in name:
    print 'yes ,it contains the string "a"'
if name.find('war') != -1:
    print 'yes ,it contains the string "war"'
delimiter = '__*__'
mylist = ['Brizal','Russia','India']
print delimiter.join('mylist')

