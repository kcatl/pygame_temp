class C1(C1,C3):
    def __init__(self,who):
        self.name = who
I1 = C1('bob')
I2 = C1('mel')
print I1.name


