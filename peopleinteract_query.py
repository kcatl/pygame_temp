#!/usr/bin/python2
#filename is peopleinteract_query.py

#interactive queries

import shelve
filenames = ('name','age','job','pay')
maxfield = max(len(f) for f in filenames)
db = shelve.open('class-shelve')

while True:
    key = raw_input('\nKey? => ')
    if not key:break
    try:
        record = db[key]
    except:
        print 'No such key "%s" !'%key
    else:
        for field in filenames:
            print field.ljust(maxfield),'===>',getattr(record,field)

