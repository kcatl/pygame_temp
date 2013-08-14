#!/usr/bin/python2
#filename is stack.py

stack = []

def pushit():
    stack.append(raw_input('Enter a new string :').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print "Removed [",stack.pop(),"]"
def viewstack():
    print stack
CMDs = {'u':pushit ,'o':popit,'v':viewstack}

def showmenu():
    pr = '''
p(U)sh
p(O)ll
(V)iew
(Q)uit

Enter your choice:'''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndentationError):
                choice = 'q'

            print '\n YOU PICKED : [%s]'%choice

            if choice not in 'uovq':
                print 'Invalid option ,please try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

