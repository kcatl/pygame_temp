#!/usr/bin/python2
#Filename is backup_ver2.py

import os 
import time

source = ['/home/alleria/python_dir']
target_dir = '/home/alleria/bak/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory'

target = today + os.sep + now + '.tar'
zip_command = "tar -cf '%s'%s"%(target,''.join(source))
if os.system(zip_command) == 0:
	print 'Successfully backup to ',target 
else:
	print 'Backup failed'

	
