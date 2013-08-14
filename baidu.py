#!/usr/bin/python2
import urllib
url = 'http://www.baidu.com'
content = urllib.urlopen(url).read()
file = open('baidu.html','w')
file.write(content)
file.close()

