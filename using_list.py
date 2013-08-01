#!/usr/bin/python2
#Filename is using_list.py

#This is my shopping list

shoplist = ['apple','mango','carrot','banana']
print 'I have ',len(shoplist),'items to purchase'
print 'These items'
for item in shoplist:
    print item
print '\nI have to buy rice'
shoplist.append('rice')
print 'my shoplist now is ',shoplist


print 'I will sort my shoplist'
shoplist.sort()
print 'the first item I will buy is ',shoplist[0]
olditem = shoplist[0]
del shoplist[0]

print 'I bought the ',olditem
print 'my shoplist now is ',shoplist
