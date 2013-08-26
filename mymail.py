#!/usr/bin/python2

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.sina.com'
POP3SRV = 'pop.sina.com'

origHdrs = ['From : hacphoenix@sina.com',
        'To : hacphoenix@sina.com',
        'Subject : test msg']
origBody = ['xxx','yyy','zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),
    '\r\n'.join(origBody)])
sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('hacphoenix@sina.com','hacphoenix@sina.com',origMsg)
sendSvr.quit()
assert len(errs) == 0,errs
sleep(10)#wait for mail to be delivered

recvSvr = POP3(POP3SRV)
recvSvr.user('hacphoenix')
recvSvr.pass_('tmac16120')
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody # assert identical

