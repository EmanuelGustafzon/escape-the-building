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
   - By using colors the uset get a better experience because it is easier to follow the game. that is why the text us red when the user has dies and it is game over, green when the user has survived and completed the game and yellow when the games starts over.

- User stories
  - As a user I want the game to go slow so I have time to read.
  - As a user I want clear instructions.

## The Design of the Game.

- This is the road map for the game. The user gets two options and have to decide one of them. The users input will affect the next output will be and how the story continues. If the user come into a room of fire, jumps out the window or make a mistake with the ambualnce the user die and the game starts over.

  ![Road Map](/images/Road%20Map%20for%20Escape%20the%20Building.jpg)

 ## Features
 
 - The user make a input and gets a output. How the story continues depends on the users decisions.
 - If the user type in an unvalid answer the user can try again because of a while loop. If the user type the correct answer but it is with spaces before or after, with big letter or small letters or mixed big and small letters does not matter. 
 - Package of dynamite that explodes by counting down from three.
 - Heading in yellow and font digital from the pyfiglet library.
 - The game instructions goes slowley by the time.sleep method.
 - User can choose a character name. If the user type nothing, the program will ask the user to put in something. Otherwise the User can have any username with any character.
 - If the user either fail or complete the game, the user get the option to start over by pressing yes. If the user press yes the screen gets cleared.

  ## Technologies

- Python

 - Python libraries
   - Colorama
   - pyfiglet
   - emoji
   - time
   - OS 

- GitHub
  - Version control system.

- GitPod
  - Development tool.

- Herokum
  - Deployment of applications.

- PIP8 Online 
  - Python code validator.

- Lucid
  - Used to create the Flowchart. 

  ## Testing 

- I validated the game's code through PEP8 Online.


   ![PEP8 Validated Code](/images/Sk%C3%A4rmbild%20(125).png)

  ## Bugs 

- Solved
  - At first the game did not run at all. The reason for this was that the first function (def welcome():) needed to be called in the end of the game.
  - The Python libraries did not work when the site was deployed. This cloud be fixed by typing pip freeze > requirements.txt to add those libraries to the requirements.txt file.

- Unsolved
  - none.

  ## Other Featured that can be implemented
   
- The one feature that I want to implement is a stopwatch. By using a threading timer the game can run at the same time as the timer and when the user has played a certain amount of the time the user fails the mission and needs to start over.
- The game has a lot of potential to expand with more paths and tricky questions. 

  ## Deployment 

- GitHub and GitPod.

  - Step one: Create new repositry.
  - Step two: choosing the Code Institute Python template.
  - Step three: Create a workspace in Gitpod.
  - Step four: using git add . , git commit -m '' and git push to note the last updates of the application and push it up to github.
  - Step four: Install Python libraries by using the pip install command, storing them in the requierments.txt file by the pip freeze > command. 

- Herokun

  - Step one: Create new application in Herokum.
  - Step two: Go into settings and click reveal config vars.
  - Step three: Add key: PORT and value: 8000. If credentials is used then add that as well with the key: CREDS and the code from the JSON file.
  - Step four: Add buildpack, I used python and Node.js.
  - Step five: Deploy the site by clicking deploy. 
  - Step six: Connect to GitHub.
  - Step seven. Choose either to deploy the site mannually or automatically. If you choose automatically the site will update anytime you push new changes to GitHub. If you choose manually you choose when you want to update the app.
  - Step eight: Click deploy branch, wait a couple of minute until the site is deplyed.
  - Step nine: Click view and see the page is live.

  ## Credits 
- Documentation from Code Institute
- Code institute GitPod tamplate. 
- My mentor Spencer
- The slack community
- This article: https://www.askpython.com/python/text-based-adventure-game'
- Stack Overflow
