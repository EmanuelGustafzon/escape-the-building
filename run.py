import time


def intro():
    print('intoducing text')
    time.sleep(1)
    print('stairs or elevator')
    choice = input()
    if choice == 'stairs':
        option_stairs()
    elif choice == 'elevator':
        option_elevator()
    else:
        print('Type stairs or elevator please!')
        intro()


def option_stairs():
    print('intoducing text stairs')
    time.sleep(1)
    print('distinguish or lather')
    choice = input()
    if choice == 'distinguish':
        option_distinguish_lather()
    elif choice == 'lather':
        dead()
    else:
        print('Type distinguish or lather please!')
        option_stairs()


def option_elevator():
    print('intoducing text elevator')
    time.sleep(1)
    print('lather or hole?')
    choice = input()
    if choice == 'lather':
        option_distinguish_lather()
    elif choice == 'hole':
        option_hole()
    else:
        print('Type lather or hole please!')
        option_elevator()


def option_distinguish_lather():
    print('introduction distinguish')
    time.sleep(1)
    print('window or hole?')
    choice = input()
    if choice == 'window':
        dead()
    elif choice == 'hole':
        survive()
    else:
        print('Type lather or hole please!')
        option_distinguish_lather()


def option_hole():
    print('intro hole')
    time.sleep(1)
    print('dynamite or pole?')
    choice = input()
    if choice == 'dynamite':
        survive()
    elif choice == 'pole':
        dead()
    else:
        print('Type lather or hole please!')
        option_hole()


def dead():
    print('Game Over')


def survive():
    print('congratulations you made it!')


intro()