#!/usr/bin/python2
#filename is maketextfile.py

'maketextfile.py ----> create text file '

import os 
ls = os.linesep

#get line 
while True:
    
    fname = raw_input('please input your filename : ')
    if os.path.exists(fname):
        print "Error : '%s' already exists " % fname 
    else:
        if fname == '':
            print 'you did not input anything here '
        else :
            break


#get file content (text) lines

all = []

print "\nEnter lines('.' by itself to quit ).\n"

#loop until user terminates input 

while True:
    entry = raw_input('>' )
    if entry == '':
        break
    else :
        all.append(entry)

#write line to file with proper line-ending 

fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'Done!'


