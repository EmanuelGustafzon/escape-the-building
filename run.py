import time
from os import system, name
from colorama import Fore
import pyfiglet
import emoji


def clear():
    """
    This function clears the terminal or screen when called.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def welcome():
    """
    The user gets instructions and can choose a character name.
    At first the text is yellow for the heading and introduction
    and then the color is set to blue and continues throughout the game.
    """
    clear()
    result = pyfiglet.figlet_format("Escape The Building", font="digital")
    print(Fore.YELLOW + result)
    print('Instruction')
    print('This is a text based adventure game. You will be guided through')
    print('a story and along with it you will have to take different')
    print('decisions and answer questions. The story depends on')
    print('your decisions and answers. Some of the steps you take')
    print('will lead to death so be careful and best of luck!')
    print('\nIf you would like to quit the game for any reason, simply')
    print('wait until the computer gives you the option to type and')
    print('and type: quit.\n')

    print(Fore.BLUE)
    global name
    name = ''
    while name == '':
        name = input('Choose a character name here:').strip()
    time.sleep(1)
    print(f'\nWelcome {name} to this adventure. \n')
    time.sleep(2)
    print('Type: r to start the game.')
    choice = input()
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'r':
            start_game()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType r you want to start the game!\n')
            choice = input()


def start_game():
    """
    The story begins here and the user will take the first decision.
    """
    clear()
    print(f'\n{name} is a tourist in London.')
    print('Right now you are on a tour in')
    print('a museum on the top floor. \n')
    time.sleep(4)
    print(emoji.emojize('Two bombs have exploded in the museum.'))
    print(emoji.emojize(':collision:'))
    time.sleep(1)
    print(emoji.emojize(':collision:'))
    time.sleep(4)
    print('\nIt caused a fire and you have to escape.\n')
    time.sleep(3)
    print('You have to make a decision, either take the elevator')
    print('to the north exit or the stairs to the south exit.\n')
    time.sleep(4)
    choice = input('Make a decision! Type stairs or elevator here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'stairs':
            option_stairs()
            ans = 'correct'
        elif choice.lower().strip() == 'elevator':
            option_elevator()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType stairs or elevator please!\n')
            choice = input()


def option_stairs():
    """
    The user begins with choosing stairs or elevator. If stairs
    is choosen the user will end up here.
    """
    time.sleep(3)
    print('\nYou run down the stairs but you only reach the third floor')
    time.sleep(2)
    print('because there is a fire on the second floor.\n')
    time.sleep(4)
    print('You see a fire distinguisher on the wall')
    print('but also a door to a fire ladder. \n')
    time.sleep(2)
    print('Would you rather distinguish the fire or use the ladder? \n')
    time.sleep(1)
    choice = input('Type distinguish or ladder here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'distinguish':
            print('\nAwesome you distinguished the fire!\n')
            option_distinguish()
            ans = 'correct'
        elif choice.lower().strip() == 'ladder':
            print('\nTo much smoke in the ladder!')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType distinguish or ladder please!\n')
            choice = input()


def option_elevator():
    """
    The user begins with choosing stairs or elevator. If elevator
    is choosen the user will end up here.
    """
    time.sleep(1)
    print('\nYou press the buttom to the elevator.\n')
    time.sleep(2)
    print('Yes, the elevator is working.\n')
    time.sleep(3)
    print('but what now?, it stopped!\n')
    time.sleep(3)
    print('You manage to get out from the elevator\n')
    time.sleep(2)
    print('You are now at the third floor.\n')
    time.sleep(3)
    print('You see a fire ladder and a hole in the ground.')
    print('Do you rather take the ladder or jump down the hole?\n')
    time.sleep(1)
    choice = input('Type: ladder or hole here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'ladder':
            print('\nYou ended up in a room on fire')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'hole':
            option_hole()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType ladder or hole please!\n')
            choice = input()


def option_distinguish():
    """
    If the user choose stairs and then distiguish the
    user will end up here.
    """
    time.sleep(2)
    print('The stairs down to the bottom floor are blocked.\n')
    time.sleep(3)
    print('You need to either jump out of the window or')
    print('try to remove the rocks blocking the stairs.\n')
    time.sleep(1)
    choice = input('Type window or remove here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'window':
            print('\nThe ground is made of concrete.')
            dead()
            ans = 'correct'
        elif choice.lower().strip() == 'remove':
            option_remove()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType window or remove please!\n')
            choice = input()


def option_remove():
    """
    If the user choose stairs - distingush and then remove
    the user will end up here. This is a tricky question
    for the user becuase the user needs to search up when
    python was released to be able to open the door.
    """
    time.sleep(3)
    print('\nYou could remove the rocks!\n')
    print('You are now at the south exit.\n')
    time.sleep(3)
    print('BUT.. there is a code to get out from the door!')
    print('The code is the same as the year Python was released!\n')
    time.sleep(2)
    choice = input('Type the right code here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.strip() == '1991':
            print('\nThat is right!\n')
            ambulance()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType the right code!\n')
            choice = input()


def option_hole():
    """
    If the user choose elevator and then hole
    the user end up here. The user needs to
    use dynamite to get out from the building.
    If user press dynamite, the tnt_countdown
    function is called.
    """
    time.sleep(2)
    print('\nThe hole lead you down to the secound floor \n')
    time.sleep(3)
    print('Now you see a pole that leads down to the north exit,')
    print('but also a package of dynamite.\n')
    time.sleep(4)
    print('Do you rather use the dynamite to explode the wall')
    print('or glide down the pole? \n')
    time.sleep(1)
    choice = input('Type: dynamite or pole here:')
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
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType dynamite or pole please!\n')
            choice = input()


def ambulance():
    """
    When the user gets out from the building
    an ambulance is needed. The user can choose
    to call.
    """
    time.sleep(3)
    print('\nYou have been breathing in quite a lot of smoke')
    time.sleep(2)
    print('\nWould you like to call an ambulance? \n')
    time.sleep(2)
    choice = input('Type call or skip here:')
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
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType call or skip please!\n')
            choice = input()


def call_ambulance():
    """
    This is the last step of the game, the
    final question. The ambulance wants the
    user's location. This reffers to the
    beginning of the game and is London.
    """
    time.sleep(3)
    print('\nHi and welcome to the SOS central! To help you')
    print('we need your location!\n')
    time.sleep(2)
    choice = input('Give out your location. Type the city you are at, here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'london':
            survive()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nRemember your location next time! Read more carefully.\n')
            dead()


def dead():
    """
    The user gets informed that the game
    is over.
    """
    print(Fore.RED + f'\nYou died {name}!\n')
    print(emoji.emojize(':skull:'))
    time.sleep(3)
    restart()


def survive():
    """
    The user gets informed that the game is completed.
    """
    print(Fore.GREEN + f'\nCongratulations you made it {name}! \n')
    print(emoji.emojize(':confetti_ball:'))
    time.sleep(3)
    restart()


def restart():
    """
    After the game is completed or if the user
    died and it is gameover the user get the
    option to restart the game.
    """
    print(Fore.BLUE)
    print('Type: r, to restart the game.\n')
    print('Type: quit, to choose a new character name')
    print('and read the game instructions.\n')
    choice = input('Type r or quit here:')
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if choice.lower().strip() == 'r':
            start_game()
            ans = 'correct'
        elif choice.lower().strip() == 'quit':
            welcome()
            ans = 'correct'
        else:
            print('\nType: r or quit please!\n')
            choice = input()


def tnt_countdown(t):
    """
    This is the countdown function
    for the dynamite explosion in
    the function called hole().
    """
    import time
    print('Waiting for the dynamite to explode!!!')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('BOOOM! \n \n \n \n \n')


t = 3

welcome()