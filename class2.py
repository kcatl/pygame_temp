class firstclass:
    def setdata(self,value):
        self.data = value
    def display(self):
        self.data
x = firstclass()
y = firstclass()
x.setdata('hello')
y.setdata(3.14)
x.display()
y.display()
