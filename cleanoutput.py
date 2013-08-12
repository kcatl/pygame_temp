#!/usr/bin/python2
#filename is cleanoutput.py

import os
from PP3E.PyTools.find import find
for filename in find('*.txt'):
    print filename
    if raw_input('View>?') == 'y':
        os.open(filename).read()
    elif raw_input('Delete??') == 'y':
        os.remove(filename)

