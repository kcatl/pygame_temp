#!/usr/bin/python2
#Filename is backup_ver1.py

import os
import time

#1. The files and directories to be backed up are specified in a list
source = ['/home/alleria/python_dir']
#2. The backup files must be stored in the main backup directory
target_dir = '/home/alleria/'
#3. The files are  backed up in the zip file
target = target_dir+time.strftime('%Y%m%d%H%M%S')+'.tar'
#4. We use the zip command ( in Unix/Linux) to put the files in a zip file
zip_command = "tar -cf '%s'%s" %(target,' '.join(source))
#Run backup 

if os.system(zip_command) == 0:
    print 'Successful backup to ',target
else :
    print 'Backup failed'
