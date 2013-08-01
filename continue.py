#!/usr/bin/python2

#Filename is continue.py

while True :
    s = raw_input('please input something : ')
    if s == 'quit':
        break
    if len(s) < 3 :
        continue
    print 'input number is suffcient length'

