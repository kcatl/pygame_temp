#!/usr/bin/python2
#Filename is backup_ver4.py

import os 
import time


#1.the files and directories to be backed up are sepcified to the list 

source = ['/home/alleria/python_dir']

#2. the backup must be stored in a main backup directory

target_dir = '/home/alleria/'

#3. the files are backup into a tar file

#4. the current time is the name of the tar archive
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

#Take a comment from the user to create the name of the tar file

comment = raw_input('Enter a comment ---> ')
if len(comment) == 0:
    target = today + os.sep + now + '.tar'
else:
    target = today + os.sep + now +'_' + \
            comment.replace('','_') + '.tar'
#Notice the backslash

#Create the subdirectory if it isn't already there

if not os.path.exists(today):
    os.mkdir(today)
    print "Successfully created directory",today


#We use the tar command (in Unix/Linux) to put the files in the tar file

zip_command = "zip -qr '%s'%s"%(target,''.join(source))

#Runbackup

if os.system(zip_command) == 0:
    print "Successfully backup"
else:
    print "Backup failed"
