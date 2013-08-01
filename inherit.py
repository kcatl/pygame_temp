#!/usr/bin/python2
#Filename = inherit.py

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name = name 
        self.name = age
        print '(Initialized SchoolMemer :%s)'% self.name

    def tell(self):
        '''tell my details'''
        print 'Name :"%s" Age:"%s"'%(self.name,self.age)
class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher: %s)'% self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary :"%d"'% self.salary
class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print '(Initialized student: %s)'%self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: %s'%self.marks
t = Teacher('Mrs.Green',40,3000)
s = Student('john',20,75)

print #print a blank line

members = [t,s]

for member in members :
    member.tell() # works both for teachers and students
    
