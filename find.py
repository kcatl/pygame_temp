#!/usr/bin/python2
#filename is find.py

import fnmatch , os

def find(pattern,startdir = os.curdir):
    matches = []
    os.path.walk(startdir, findvistor, (matches ,pattern))
    matches.sort()
    return matches
def findvistor((matches,pattern),thisdir,nameshere):
    for name in nameshere:
        if fnmatch.fnmatch(name,pattern):
            fullpath = os.path.join(thisdir,name)
            matches.append(fullpath)

if __name__ == '__main__':
    import sys
    namepattern,startdir = sys.argv[1],sys.argv[2]
    for name in find(namepattern, startdir):
        print name

