from temp import Temp

tanks = {'a':Temp('alleria'), 'b':Temp('Billy'), 'c':Temp('Carliy')}
tank_alive = len(tanks)

print 
while tank_alive:
    for tank_name in sorted(tanks.keys()):
        print tank_name, tanks[tank_name]

    first = raw_input('who fires--->?').lower()
    second = raw_input('who fires at --->?').lower()

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
        if first_tank == second_tank:
            print '*' * 30
            print 
            print 'you can not fire yourself'
            print
            print '*' * 30
            continue
    except KeyError:
        print 'No such tank'
        continue

    if not first_tank.alive or not second_tank.alive:
        print 'one of the tank is dead'

    print '*' * 30

    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        tank_alive -= 1

    print '*' * 30

for tank in tanks.values():
    print tank.name ,'is the winner!'
    break
