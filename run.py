import time
import threading

print('Welcome to Escape The Building!')
name = ''
while name == '':
    name = input('type yor name here:').strip()
time.sleep(1)
print(f'welcome {name} to this adventure!')
time.sleep(3)
print(f'''
{name} is a tourist in London. 
Right now your at a tour in a 
museum,at the top floor.
''')
time.sleep(5)
print('BOOOM')
time.sleep(2)
print('BOOOM')
time.sleep(2)
print('What was that, the hole building is shaking.')
time.sleep(2)
print('We hear from the tourguides radio that two bombs has exploded.')
print('And it caused fire, You got 10 secounds to escape!') 
time.sleep(3)


def countdown():
    global timer 
    timer = 10
    for x in range(10):
        timer -= 1
        time.sleep(1)
    print('BOOM! the third bomb exploded!')


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

while timer > 0:
    def intro():
        print('''
        You have to make a decision, either take the elevator
        to the south exit or the stairs to the north exit.
        ''')
        print('Make a decision: type stairs or elevator')
        choice = input()
        ans = 'incorrect'
        while(ans == 'incorrect'):
            if choice.lower() == 'stairs':
                option_stairs()
                ans = 'correct'
            elif choice.lower() == 'elevator':
                option_elevator()
                ans == 'correct'
            else:
                print('Type stairs or elevator please!')
                choice = input()
    
    def option_stairs():
        print('''
        You run down the stairs but you only reach half a floor down
        because you see the fire in the end of the stairs.''')
        time.sleep(3)

        print('''
        You see a distinguisher a distinguisher on the wall
        but also a door to a fire lather. Would you rather
        distiguish or use the lather?''')

        time.sleep(2)
        print('Type: distinguish or lather')
        choice = input()
        ans = 'incorrect'
        while(ans == 'incorrect'):
            if choice == 'distinguish':
                print('Awesome you made it!')
                option_distinguish_lather()
                ans == 'correct'
            elif choice == 'lather':
                print('To much smoke in the lather!')
                dead()
                ans == 'correct'
            else:
                print('Type distinguish or lather please!')
                choice = input()

    def option_elevator():
        print('You press the buttom to the elevator.')
        time.sleep(3)
        print('Yes, it is working')
        time.sleep(3)
        print('but what now?, it stopped!')
        print('You manage to get out from the elevator')
        print('You are now at the third floor.')
        print('''
        You see a fire lather and a hole in the ground.
        Do you rather take the lather or jump down the hole? ''')
        print('Type: lather or hole?')
        choice = input()
        ans = 'incorrect'
        while(ans == 'incorrect'):
            if choice == 'lather':
                option_distinguish_lather()
                ans == 'correct'
            elif choice == 'hole':
                option_hole()
                ans == 'correct'
            else:
                print('Type lather or hole please!')
                choice = input()

    def option_distinguish_lather():
        print('''
        You come to a room on the northside but the stairs 
        down to the bottomfloor is blocked.''')
        
        print('''
        You need to either jump out from the window
        or jump down from a hole in the ground that you suppose 
        leads to the first floor.''')
        time.sleep(1)
        print('Type: window or hole?')
        choice = input()
        ans = 'incorrect'
        while(ans == 'incorrect'):
            if choice == 'window':
                print('The ground is made of concrete.')
                dead()
                ans == 'correct'
            elif choice == 'hole':
                survive()
                ans == 'correct'
            else:
                print('Type window or hole please!')
                choice = input()

    def option_hole():
        print('''
        The hole lead you down to the secound floor 
        Now you see a pole that takes you down to floor one and a package 
        of dynamite.''')
        print('''
        Do you rather use the dynamite to explode the wall
        or glide down the pole?''')
        time.sleep(1)
        print('Type: dynamite or pole?')
        choice = input()
        ans = 'incorrect'
        while(ans == 'incorrect'):
            if choice == 'dynamite':
                tnt_countdown(t)
                time.sleep(1)
                print('The wall exploded and you can jump out!')
                print('The ground is soft so you can survive the jump.')
                survive()
                ans == 'correct'
            elif choice == 'pole':
                print('There is a fire where you ended up.')
                dead()
                ans == 'correct'
            else:
                print('Type lather or hole please!')
                choice = input()

    def dead():
        print('You died!')

    def survive():
        print('congratulations you made it!')

    def tnt_countdown(t):
        import time
        print('Waiting for the dynamite to explode!!!')
        while t >= 0:
            print(t, end='...')
            time.sleep(1)
            t -= 1
        print('BOOOM! \n \n \n \n \n')

    t = 3

    intro()
    if timer == 0:
        break
        