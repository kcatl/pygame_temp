class Temp(object):
    
    def __init__(self,name):
        self.name = name
        self.shells = 5
        self.armor = 5
        self.alive = True

    def __str__(self):


        if self.alive :
            return "%s (%i shells, %i armor) " % (self.name, self.shells, self.armor)
        else:
            return "%s is dead" % self.name

    def fire_at(self, enemy):

        if self.shells >= 1:
            self.shells -= 1
            print self.name ,'is fire at ',enemy.name 
            enemy.hit()

        else:
            print 'you do not have any shells to fire'

    def hit(self):

            self.armor -= 1
            print self.name, 'is hitted '
            if self.armor <= 0:
                self.explode()



    def explode(self):
        self.alive = False
        print self.name ,'is exploded'


