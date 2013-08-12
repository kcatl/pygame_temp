#!/usr/bin/python2
#filename is exit.py

import sys

try :
    sys.exit()
except SystemExit:
    print 'Ignoring exit'

