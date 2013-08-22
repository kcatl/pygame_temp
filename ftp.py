#!/usr/bin/python2

from ftplib import FTP
f = FTP('noads.biz')
f.login('www.optionver.tk','tmac16120')
f.dir()
f.quit()

