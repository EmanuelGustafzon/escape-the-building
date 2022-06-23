# Escape The building!
A game for anyone who are up for a challenge and wants to read a story at the same time. The game is built in python as a project for Code Institute. 
## https://escape-the-building.herokuapp.com/.

## User Experience

 - Target Audience 

   - Users who wants a text based adventure game that wants some action. The game is designed to be rappid and the user needs to take many decisions in a short period of time.
   - Users who wants a bit of a challenge where they sometimes needs to stop and think. I am thinking about the code to open the door and the last question where you need to remember what been said in the beginning of the game.

 - The flow of the game
   
   - The game does not break at any point. if the user fails the mission it starts over again.
   - The user gets clear instructions to learn and understand the game.
   - If the user makes a type error, the user simply gets the option to try again.

## The Design of the Game.

- This is the road map for the game. The user gets two options and have to decide one of them. The users input will affect the next output will be and how the story continues. If the user come into a room of fire, jumps out the window or make a mistake with the ambualnce the user die and the game starts over.

  ![Road Map](/images/Road%20Map%20for%20Escape%20the%20Building.jpg)

  ## Technologies

- Python

 - Python libraries
  - Colorama
  - pyfiglet
  - emoji
  - time

- GitHub
- GitPod
- Herokum
- PIP8 Online 
- Lucid

  ## Testing 

- I validated the game's code through PEP8 Online.


   ![PEP8 Validated Code](/images/Sk%C3%A4rmbild%20(125).png)

  ## Bugs 

- Solved
  - At first the game did not run at all. The reason for this was that the first function (def welcome():) needed to be called in the end of the game.
  - The Python libraries did not work when the site was deployed. This cloud be fixed by typing pip freeze > requirements.txt to add those libraries to the requirements.txt file.

- Unsolved
  - A timer was supposed to be set in the game. The intention was that there would be a third bomb in the building and the user needs to get out from the building in a certain time. I used the thread time method to make the timer countdown at the same time as the user plays the game. The hole game code was wrapped in a while loop. If the timer would be equal to zero the while loop break. The bug I encountered was that the timer counted down once and did not reset after the time ran out, the user won the game or the user lost the game. Because of time I decided to get rid of the timer and keep it as it is.


  ## Other Featured that can be implemented
   
- The one feature that I want to implement is a stopwatch. By using a threading timer the game can run at the same time as the timer and when the user has played a certain amount of the time the user fails the mission and needs to start over.
- The game has a lot of potential to expand with more paths and tricky questions. 

  ## Deployment 

- GitHub and GitPod.

  - Step one: Create new repositry.

- Herokun

  - Step one: 

  ## Credits 
- Documentation from Code Institute
- Code institute GitPod tamplate. 
- My mentor Spencer
- The slack community
- This article: https://www.askpython.com/python/text-based-adventure-game'
- Stack Overflow
