#!/usr/bin/python2
#filename is moreplus.py


import sys
def getreply():
    '''
    read a reply from a user ,even if
    stdin redirected to a file or pipe
    '''
    if sys.stdin.isatty():
        return raw_input('?')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch('?')
            key = msvcrt.getche()
            msvcrt.putch('\n')
            return key
        elif sys.platform[:5] == 'linux':
            print '?',
            console = open('/dev/tty')
            line = console.readline()[:-1]
            return line
        else:
            print '[pause]'
            import time
            time.sleep(5)
            return 'y'

def more(text,numlines = 10):
    '''
    split multilines string to stdout
    '''

    lines = text.split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk : print line 
        if lines and getreply() not in ['y','Y'] :break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())

