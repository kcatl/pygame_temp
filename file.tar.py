import os 
tar_command = "tar -cf /home/alleria/python_dir/file.tar /home/alleria/python_dir/file.py"
if os.system(tar_command) == 0:
    print "Successfully backup"
else :
    print "Failed to backup "
