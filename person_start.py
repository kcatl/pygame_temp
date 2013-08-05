#!/usr/bin/python2
#filename is person_start.py


class person:
    def __init__(self,name,age,pay = 0,job = None):
        self.name = name 
        self.age = age
        self.pay = pay 
        self.job = job
if  __name__ == '__main__':
    bob = person('Bob Smith',42,300000,'sweng')
    sue = person('Sue Smith',43,400000,'music')
    print bob.name ,sue.pay
     

    print bob.name.split()[-1]
    sue.pay *= 1.10
    print sue.pay


