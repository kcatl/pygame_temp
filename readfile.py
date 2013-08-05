#!/usr/bin/python2
#filename is python2


'readfile.py ------> read and display the file content '

#get filename 


fname  = raw_input('please input your file name : ')
print 

#attempt to open file for reading 

try :
    fobj = open(fname ,'r')
except IOError,e :
    print '*** file open error ***',e 
else :
    #display contents to the screen
    for eachline in fobj :
        print eachline,

    fobj.close()

