class C1(C2,C3):
    def setname(self,who):
        self.name = who
I1 = C1()
I2 = C1()
I1.setname('Bob')
I2.setname('mel')
print I1.name
