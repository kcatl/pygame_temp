#!/usr/bin/python2

import nntplib
import socket

HOST = 'noads.biz'
GRNM = 'www.optionver.tk'
USER = 'www.optionver.tk'
PASS = 'tmac16120'

def main():

    try:
        n = nntplib.NNTP(HOST)
#,uesr = USER ,password = PASS
    except socket.gaierror,e:
        print 'Error : can not reach the host "%s" ' % HOST
        print '    ("%s")' % eval(str(e))[1]
        return
    except nntplib.NNTPPermanentError,e:
        print 'Error : access denied on host "%s"'% HOST
        print ' ("%s")'% str(e)
        return
    print '***Connected to the host "%s"' % HOST

    try:
        rsp,ct,fst,lst,grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError,e:
        print 'Error : cannot load group "%s"'% GRNM
        print '  ("%s") '% str(e)
        print 'Server may require authentication'
        print 'Uncomment /edit  login line above'
        n.quit()
        return
    except nntplib.NNTPTemporaryError,e:
        print 'Error : group "%s" unaviable'% GRNM
        print ' ("%s")' % str(e)
        n.quit()
        return
    print '*** Found newgroup "%s"' % GRNM


    rng = '%s -%s'%(fst,lst)
    rsp,frm = n.xhdr('from',rng)
    rsp,sub = n.xhdr('subject',rng)
    rsp,dat = n.xhdr('date',rng)
    print '''*** Found last aticle (#%s):

    From : %s
    Subject: %s
    Date : %s
    ''' % (
            lst,frm[0][1],sub[0][1],dat[0][1])
    rsp,anum,mid,data = n.body(lst)
    displayFirst20(data)
    n.quit()



def displayFirst20(data):
    print '*** First (<=20) meaningful lines : \n'
    count = 0
    lines = (line.rstrip() for line  in data)
    lastBlank = True
    for line in lines :
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not lower.startswith('>>>')) or \
                lower.startswith('|') or \
                lower.startswith('in article') or \
                lower.endwith('writes:') or \
                lower.endwith('writes:') :
                    continue
    if not lastBlank or (lastBlank and line):
        print '    %s' % line
        if line:
            count += 1
            lastBlank = False
        else:
            lastBlank = True
    if  count == 20:
        break

if __name__ == '__main__':
    main()


