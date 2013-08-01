#!/usr/bin/python2
#Filename is using_file.py

poem = '''\
program amming is fun
when the work is done
if you want to make your work also fun:
    use Python!
'''
f = file('poem.txt','w')#open for 'w'riting
f.write(poem)
f.close()
f = file('poem.txt')
#if no mode is specified ,'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:#Zero length indicates EOF
        break
    print line,
    #Notice comma to avoid automaic newline add to by python
f.close()
#close the file


