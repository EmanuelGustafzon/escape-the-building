import time
from colorama import Fore


def welcome():
    print(Fore.YELLOW + 'Escape the Building')
    print(Fore.BLUE)
    name = ''
    while name == '':
        name = input('type yor name here:').strip()
    time.sleep(1)
    print(f'\nwelcome {name} to this adventure \n')
    time.sleep(3)
    print(f'{name} is a tourist in London.') 
    print('Right now your at a tour in a') 
    print('museum at the top floor. \n')
    time.sleep(2)
    print('Two bombs has exploded in the museum.')
    time.sleep(2)
    print('\nIt caused fire and you have to escape.\n')
    time.sleep(3)
    start_game()


def start_game():
    print('You have to make a decision, either take the elevator')
    print('to the south exit or the stairs to the north exit.\n')
    time.sleep(3)
    print('Make a decision: type stairs or elevator\n')
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
            print('\nType stairs or elevator please!\n')
            choice = input()


def option_stairs():
    time.sleep(2)
    print('\nYou run down the stairs but you only reach half a floor down')
    time.sleep(2)
    print('because you see the fire in the end of the stairs.\n')
    time.sleep(3)
    print('You see a distinguisher on the wall')
    print('but also a door to a fire lather \n')
    time.sleep(1)
    print('would you rather distiguish or use the lather? \n')
    time.sleep(1)
    print('Type: distinguish or lather\n')
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
            print('\nType distinguish or lather please!\n')
            choice = input()


def option_elevator():  
    time.sleep(1)
    print('\nYou press the buttom to the elevator.\n')
    time.sleep(2)
    print('Yes, the elevator is working\n')
    time.sleep(3)
    print('but what now?, it stopped!\n')
    time.sleep(2)
    print('You manage to get out from the elevator\n')
    time.sleep(2)
    print('You are now at the third floor.\n')
    time.sleep(2)
    print('You see a fire lather and a hole in the ground.')
    print('Do you rather take the lather or jump down the hole?\n')
    time.sleep(1)
    print('Type: lather or hole?\n')
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
            print('\nType lather or hole please!\n')
            choice = input()


def option_distinguish():
    time.sleep(2)
    print('\nThe stairs down to the bottomfloor is blocked.\n')
    time.sleep(2)
    print('You need to either jump out from the window or')
    print('try to remove the rocks blocking the stairs.\n')
    time.sleep(1)
    print('Type: window or remove?')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'window':
            print('The ground is made of concrete.')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'remove':
            option_remove()
            ans = 'correct'
        else:
            print('\nType window or hole please!\n')
            choice = input()


def option_remove():
    time.sleep(2)
    print('\nYou cloud remove the rocks!\n')
    time.sleep(2)
    print('BUT.. there is code to get out from the door!')
    print('The code is the same as the year Python was released!\n')
    time.sleep(1)
    print('Type the right code!')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.strip() == '1991':
            ambulance()
            ans = 'correct'
        else:
            print('\nType the right code!\n')
            choice = input()


def option_hole():
    time.sleep(1)
    print('\nThe hole lead you down to the secound floor \n')
    time.sleep(2)
    print('Now you see a pole that takes you down to floor one')
    print('and a package of dynamite.\n')
    time.sleep(4)
    print('Do you rather use the dynamite to explode the wall')
    print('or glide down the pole? \n')
    time.sleep(3)
    print('Type: dynamite or pole?')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'dynamite':
            tnt_countdown(t)
            time.sleep(1)
            print('\nThe wall exploded and you can jump out!\n')
            time.sleep(2)
            print('The ground is soft so you can survive the jump.')
            ambulance()
            ans = 'correct'
        elif choice.lower().strip() == 'pole':
            time.sleep(2)
            print('\nThere is a fire where you ended up.\n')
            dead()
            ans = 'correct'
        else:
            print('\nType dynamite or pole please!\n')
            choice = input()


def ambulance():
    time.sleep(3)
    print('\nYou have been breathing in quite a lot of smoke')
    time.sleep(2)
    print('\nWould you like to call an ambulance? \n')
    time.sleep(2)
    print('Make a decision: type call or skip\n')
    choice = input()
    ans = 'incorrect'   
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'call':
            numbers = [9, 1, 1]
            for number in numbers:
                print(number)
                time.sleep(0.5)
            call_ambulance()
            ans = 'correct'
        elif choice.lower().strip() == 'skip':
            dead()
            ans = 'correct'
        else:
            print('\nType call or skip please!\n')
            choice = input()


def call_ambulance():
    time.sleep(3)
    print('\nHi and welcome to the SOS central! To help you')
    print('we need your location!\n')
    time.sleep(2)
    print('Give out your location, type the city you are at!\n')
    choice = input()
    ans = 'incorrect'   
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'london':
            survive()
            ans = 'correct'
        else:
            print('\nRemember your location next time!\n')
            dead()

    
def dead():
    print(Fore.RED + '\nYou died!\n')
    welcome()
    

def survive():
    print(Fore.GREEN + '\nCongratulations you made it! \n')
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
