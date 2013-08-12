#!/usr/bin/python2
#filename is match.py

import os 
def atEachDir(matchlist,dirname,fileshere):
    for filename in fileshere:
        if filename.endswith('.py'):
            pathname = os.path.join(dirname,filename)
            if 'Tkinter' in open(pathname).readlines():
                matchlist.append(pathname)

matches = []
os.path.walk('/home/alleria',atEachDir,matches)
matches


