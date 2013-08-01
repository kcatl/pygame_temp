#!/usr/bin/python2
#Filename is picking.py

import cPickle as p
shoplistfile = 'shoplist.data'
#the name of the file 

shoplist = ['apple','mango','carrot']


#write to the file

f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist
#remove the shoplist

#read shoplist from storage

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist

