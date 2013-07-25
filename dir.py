#!/bin/python
import subprocess
import os
if os.path.isdir("/tmp"):
  print "/tmp is a directory"
else:
  print "/tmp is not  a directory"
subprocess.call(["ls","."])
subprocess.call(["date"])
uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname,uname_arg])
def pyfunc():
  print "hello,world"
pyfunc()
