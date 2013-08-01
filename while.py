#!/usr/bin/python2
#file name is while.py

number = 23
running = True

while running :
    guess = int(raw_input('Enter your integer: '))

    if guess == number :
        print 'Congratulations, you guessed it '
        running = False
        #this cause the while loop stop
    elif guess >  number :
        print 'No, it is a bit bigger than that'
    else :
        print 'No, it is a bit little than that'
else:
    print 'Done'

