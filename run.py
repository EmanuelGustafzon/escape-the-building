def scene1():
    """
    This is a text based adventure game. The story continue as the user makes different choices along the way. In this first scene the 
    user gets a background story and what the mission is. After that the user got to decide if using the stairs or elevator to get out
    from the building.
    """

    import time
    print("""WELCOME TO ESCAPE THE BUILDING!
    Let's get started with this text based adventure experience! 
    
    Peter is a tourist in London and is taking part of a tour in
    a beutiful museum about the history on England. They are at the top floor
    and the guid is talking about many intresting facts about the history of architecture of London.
    AND THEN!!! They hear two big explosions. BAAM! BAAM! 
    The tourguid reises the valume of the radio. They got informed that two bombs has exploded on the 
    first and secound floor and it accured a fire. I look behind me and I see another bomb ticking.
    
    Your mission is to get out from the building alive before the bomb explode!
    """)
    print('You see two possiblities, either you take the elvator or the stairs')
    print('Type your choice: elevator or staris?')

    first_scene_input = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans =='incorrect'):
        if(first_scene_input.upper() == 'STAIRS'):
            print('you chosed stairs')
            ans = 'correct'
            stairs('You decided to take the stairs')
        elif(first_scene_input.upper() == 'ELEVATOR'):
            print('you choosed elevator')
            ans = 'correct'
            elevator('You decided to take the elevator')
        else:
            print('PLEASE ENTER ONE OF THE CHOICES: Elevator or stairs')
            first_scene_input = input()
scene1()





