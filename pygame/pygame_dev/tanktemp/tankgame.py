from tank import Tank

tanks = {"a":Tank('alleria'), "b":Tank('billy'), "c":Tank('Carrl')}
alive_tanks = len(tanks)

while alive_tanks > 1:
    print 
    for tank_name in sorted( tanks.keys() ):
        print tank_name, tanks[tank_name]

    first = raw_input('who fires?').lower()
    second = raw_input('Who at ?').lower()

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError:
        print 'there is no such tank!'
        continue

    if not first_tank.alive or not second_tank.alive:
        print 'One of the tank is dead!'
        continue

    print 
    print "*" * 30

    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1

    print '*' * 30

    for tank in tanks.values():
        if tank.alive:
            print tank.name,'is the winner!'
            break

    
