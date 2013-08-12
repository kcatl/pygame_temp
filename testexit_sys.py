#!/usr/bin/python2
#filename is testexit_sys.py

def later():
    import sys
    print 'Bye sys world'
    sys.exit(44)
    print 'Never reached '

if __name__ == '__main__':
    later()

