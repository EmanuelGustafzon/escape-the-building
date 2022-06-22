import time


def welcome(): 
    print('Welcome to Escape The Building \n')
    name = ''
    while name == '':
        name = input('type yor name here:').strip()
    time.sleep(1)
    print(f'welcome {name} to this adventure! \n')
    time.sleep(3)
    print(f'{name} is a tourist in London.') 
    print('Right now your at a tour in a') 
    print('museum at the top floor. \n')
    print('Two bombs has exploded in the museum.')
    print('It caused fire and you have to escape \n')
    time.sleep(3)
    start_game()


def start_game():
    print('You have to make a decision, either take the elevator')
    print('to the south exit or the stairs to the north exit. \n')
    print('Make a decision: type stairs or elevator')
    choice = input()
    ans = 'incorrect'   
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'stairs':
            option_stairs()
            ans = 'correct'
        elif choice.lower().strip() == 'elevator':
            option_elevator()
            ans = 'correct'
        else:
            print('Type stairs or elevator please!')
            choice = input()


def option_stairs():
    print('You run down the stairs but you only reach half a floor down')
    print('because you see the fire in the end of the stairs. \n')
    time.sleep(3)
    print('You see a distinguisher on the wall')
    print('but also a door to a fire lather \n')
    print('would you rather distiguish or use the lather? \n')
    print('Type: distinguish or lather')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'distinguish':
            print('Awesome you distinguished the fire! \n')
            option_distinguish()
            ans = 'correct'
        elif choice.lower().strip() == 'lather':
            print('To much smoke in the lather!')
            dead()
            ans = 'correct'
        else:
            print('Type distinguish or lather please!')
            choice = input()


def option_elevator():  
    print('You press the buttom to the elevator. \n')
    time.sleep(3)
    print('Yes, the elevator is working \n')
    time.sleep(3)
    print('but what now?, it stopped! \n')
    time.sleep(1)
    print('You manage to get out from the elevator \n')
    print('You are now at the third floor. /n')
    print('You see a fire lather and a hole in the ground.')
    print('Do you rather take the lather or jump down the hole? \n')
    print('Type: lather or hole?')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'lather':
            print('You ended up in a room on fire')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'hole':
            option_hole()
            ans = 'correct'
        else:
            print('Type lather or hole please!')
            choice = input()


def option_distinguish():
    time.sleep(2)
    print(' The stairs down to the bottomfloor is blocked. \n')
    print('You need to either jump out from the window')
    print('or jump down from a hole in the ground that')
    print('you suppose leads to the first floor. \n')
    time.sleep(1)
    print('Type: window or hole?')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'window':
            print('The ground is made of concrete.')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'hole':
            ambulance()
            ans = 'correct'
        else:
            print('Type window or hole please!')
            choice = input()


def option_hole():
    time.sleep(2)
    print('The hole lead you down to the secound floor \n')
    print('Now you see a pole that takes you down to floor one')
    print('and a package of dynamite. \n')
    print('Do you rather use the dynamite to explode the wall')
    print('or glide down the pole? \n')
    time.sleep(1)
    print('Type: dynamite or pole?')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'dynamite':
            tnt_countdown(t)
            time.sleep(1)
            print('The wall exploded and you can jump out!')
            print('The ground is soft so you can survive the jump.')
            ambulance()
            ans = 'correct'
        elif choice.lower().strip() == 'pole':
            print('There is a fire where you ended up.')
            dead()
            ans = 'correct'
        else:
            print('Type dynamite or pole please!')
            choice = input()


def ambulance():
    time.sleep(2)
    print('You have been breathing in quite a lot of smoke')
    print('would you like to call an ambulance? \n')
    print('Make a decision: type call or skip')
    choice = input()
    ans = 'incorrect'   
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'call':
            call_ambulance()
            ans = 'correct'
        elif choice.lower().strip() == 'skip':
            dead()
            ans = 'correct'
        else:
            print('Type call or skip please!')
            choice = input()


def call_ambulance():
    time.sleep(3)
    print('Hi and welcome to the SOS central! To help you')
    print('we need your location! \n')
    print('Give out your location, type the city you are at! \n')
    choice = input()
    ans = 'incorrect'   
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'london':
            survive()
            ans = 'correct'
        else:
            print('Remember your location next time! \n')
            dead()

    
def dead():
    print('You died! \n')
    welcome()
    

def survive():
    print('congratulations you made it! \n')
    welcome()


def tnt_countdown(t):
    import time
    print('Waiting for the dynamite to explode!!!')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('BOOOM! \n \n \n \n \n')


t = 3

welcome()
