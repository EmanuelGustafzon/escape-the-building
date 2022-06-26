# Escape The building!
A text based adnventure game. The user gets guided through a story. The user get different options and questions along the game. The story changes depends on what the users inputs are and some inputs will lead to death. This game is made as my third milestone project with Code Institute and I used python to build it. 
## https://escape-the-building.herokuapp.com/.

## Site Owner Goals

  - As a site owner I want the game to not break at any point.
  - As a site owner I want the user to easily understand and learn the game.
  - As a site owner I want to provide a fun, challenging and interactive game. 

## User Experience

 - Target Audience 

   - Users who wants to play a text based adventure game with action. The game is designed to be rappid and the user needs to make many decisions in a short period of time.
   - User who likes stories.
   - Users who wants a bit of a challenge where they sometimes needs to stop and think.

- User stories

  - As a user I want the game to go slow so I have time to read.
  - As a user I want clear instructions.

## The Design of the Game.

- This is the road map for the game. The user gets two options and have to decide one of them and sometimes a question to answer. The users input will affect what the next output will be and how the story continues. If the user come into a room of fire, jumps out the window or make a mistake with the ambualnce the user dies and the game is over.

  ![Road Map](/images/Road%20Map%20for%20Escape%20the%20Building.jpg)

 ## Features

   - The first feuture the user sees is a banner and an introduction, the user choose a character name and when the user feels ready the user can click r to start the game. The user has to type a username and it cannot remain blank.
 ![feature Home](/images/IMG-1644.jpg)
   - The game starts with a clear screen, the story begins and the user get different options to choose from. How the story continues depends on the users input.
   - The input can have blank spaces.
   - The input can be in lower or uppercase or mix them.
   - If the user types an unvalid input the computer will ask the user to type in a new inpyt.
 ![feuture game structure](/images/IMG-1646.jpg)
   - When the user loose the game the text is red and the user get the option to get back to the beginning to choose a new character name or continue the game with the same user name. What ever the user choose the screen will start cleared.
 ![feature game over ](/images/IMG-1647.jpg)
    - When the user wins the game the text is green and the user get the option to get back to the beginning to choose a new character name or continue the game with the same user name. What ever the user choose the screen will start cleared.
 ![feuture win game](/images/IMG-1648.jpg)
    - If the user decide to use dynamite, there is a function that counts down from 3 to 0.
 ![feauture count down](/images/IMG-1649.jpg)
   
    - If the user at any point want to quit the game the user can click quit. 
 
 - The user make an input and gets a output. How the story continues depends on the users input.
 - If the user type in an unvalid input the user can try again because it is running in a while loop until the answer is valid. 
 - The user input can be in lowercase and uppercase letters. The input can have blank spaces before and after. This is because of the strip() and lower() method. 
 - The package of dynamite that explodes by counting down from three is made with a function is called if the user choose dynamite.
 - The heading font color is yellow from the colorama library and with a font style of digital from the pyfiglet library.
 - The general text in the game is blue from coloroma.
 - If the user dies the text is red and if the user wins the text is green from the same library.
 - The story in the game goes slowley by the time.sleep() method.
 - The user can choose a character name. If the user type nothing, the programme will ask the user to type something until the user does. The User can have any character name with any character.
 - If the user either fail or complete the game, the user get the option to start again. If the user type r the game gets cleared and the game starts over with the same character name. If the user type c the user can choose a new character name and read the instructions again if needed.
 - The user can type quit and get back to the bginning where the user can read the instructions and choose a character name.

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
  - Step four: using git add . , git commit -m '' and git push to note the last updates of the application and store the changes in github.
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
- Stack Overflow: https://stackoverflow.com/
- Geeks for Geeks: https://www.geeksforgeeks.org/
