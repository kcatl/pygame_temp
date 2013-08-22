#!/usr/bin/python2

import ftplib
import os
import socket

HOST = 'noads.biz'
DIRN = 'php/'
FILE = 'index.php'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print 'Error : Can not reach "%s" ' % HOST
        return
    print '....Connected to the host "%s"'% HOST

    try:
        f.login('www.optionver.tk','tmac16120')
    except ftplib.error_perm:
        print 'Error : Can not login as optionver'
        f.quit()
        return
    print '....LOgged in as optionver'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'Error : Can not CD into the dir "%s" ' % DIRN
        f.quit()
        return
    print '....Changed to the dir "%s"'% DIRN

    try:
        f.retrbinary('RETR %s' % FILE,
                open('ftpfile','wb').write)
    except ftplib.error_perm:
        print 'Error Can not read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '....download the file "%s"'% FILE 
    f.quit()
    return
    
if __name__ == '__main__':
    main()

