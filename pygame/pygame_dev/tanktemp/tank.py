class Tank(object):
    def __init__(self,name):
        self.name = name
        self.alive = True
        self.shells = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i shells, %i armor)" %  (self.name, self.shells, self.armor)
        else:
            return "%s is dead!" % self.name

    def fire_at(self, enemy):
        if self.shells >= 1:
            self.shells-= 1
            print self.name, 'fire at ' ,enemy.name
            enemy.hit()
        else:
            print self.name, 'has no shells'

    def hit(self):
        self.armor-= 20
        print self.name , 'is hit!'
        if self.armor<= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print self.name,'is exploded!'


