#!/usr/bin/python2
#filename is teststreams.py


def interact():
    print 'hello stream world'
    while 1:
        try:
            reply = raw_input('Enter an number--->')
        except EOFError:
            break
        else:
            num = int(reply)
            print "%d squared number is %d"%(num,num ** 2)
    print 'Bye!'

if __name__ == '__main__':
    interact()

