#!/usr/bin/python2
while True:
    reply = raw_input('Please input some thing : ')
    if reply == 'stop': break
    try :
        num = int(reply)
    except :
        print "Bad ! " * 8
    else :
        print int(reply) ** 2 
print "Bye !"
