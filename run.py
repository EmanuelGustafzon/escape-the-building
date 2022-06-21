name = input('Enter your name!')
print(f'Hi {name}')
start = input('would you rather play the game')
if start == 'play':
    print('great')
    setting = input('stairs or elevator?')
else:
    print('lame')
    quit()

if setting == 'stairs':
    print('distinguish or lather')
    response = input()
    if response == 'distinguish':
        print('window or hole')
        response_second = input( )
        if response_second == 'hole':
            print('You survived')
        elif response_second == 'window':
            print('you died') 
    elif response == 'lather':
        print('you died')

elif setting == 'elevator':
    print('lather of hole')
    choose = input()
    if choose == 'lather':
        print('window or hole')
        choose_second = input()
        if choose_second == 'window':
            print('you died')
        elif choose_second == 'hole':
            print('you survived')
    elif choose == 'hole':
        print('lather or jump?')
        option = input( )
        if option == 'lather':
            print('you died')
        elif option == 'jump':
            print('you survived!')


