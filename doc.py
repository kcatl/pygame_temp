#!/usr/bin/python2
#filename is doc.py

#split and interactively page a string or file of the text:

def more(text,numlines = 15):
    lines = text.split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk : print line
    else:
        if lines and raw_input('More') not in ['y','Y'] : break

if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(),10)

