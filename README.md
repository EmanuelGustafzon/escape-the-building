# Escape The building!
A text based adnventure game. The user gets guided through a story. The user gets different options and questions along the game. How the story continues depends on what the users inputs are and some inputs will lead to death. This game is made as my third milestone project with Code Institute and I have used python to build it. 
## https://escape-the-building.herokuapp.com/.

## Site Owner Goals

  - As a site owner I want to provide a game that do not break at any point.
  - As a site owner I want the user to easily understand and learn the game.
  - As a site owner I want to provide a fun and also a challenging and interactive game. 

## User Experience

 - Target Audience 

   - Users who wants to play a text based adventure game with action. The game is designed to be rappid and the user needs to make many decisions in a short period of time.
   - Users who likes stories.
   - Users who wants a bit of a challenge where they sometimes need to stop and think.

- User stories

  - As a user I want the game to go slow so I have time to read.
  - As a user I want clear instructions.
  - As a user I want the screen to look clean.
  - As a user I want to try again if I die.


## The Design of the Game.

- This is the road map for the game. The user gets two options and have to decide one of them and sometimes the user gets a question to answer. The users input will affect what the next output will be and how the story continues. If the user comes into a room of fire, jumps out the window or make a mistake with the ambualnce the user dies and the game is over.

  ![Road Map](/images/Road%20Map%20for%20Escape%20the%20Building.jpg)

 ## Features

    - The first feuture the user sees is a banner and the introduction, the user choose a character name and when the user feels ready the user can click or to start the game. The user has to type in a character name and it cannot remain blank.

 ![feature Home](/images/IMG-1644.jpg)

    - The game starts with a clear screen, the story begins and the user gets different options to choose from. How the story continues depends on the users input.
    - The input can have blank spaces.
    - The input can be in lower or uppercases or mixed.
    - If the user types a unvalid input the computer will ask the user to try again.

 ![feuture game structure](/images/IMG-1646.jpg)

    - When the user looses the game the text is red and when the user wins the text is green. The user gets the option to go back to the beginning to choose a new character name or continue the game with the same name. Whatever the user choose the screen will be cleared so it looks nice and tidy.

 ![feature game over ](/images/IMG-1647.jpg)
 ![feuture win game](/images/IMG-1648.jpg)
    
    - If the user decide to use dynamite, there is a function that counts down from 3 to 0 and then the dynamite explode.

 ![feauture count down](/images/IMG-1649.jpg)
   
    - If the user at any point wants to quit the game the user can type in quit and it will lead them back to the beginning where the user can type in a character name and start over.

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



   ![PEP8 Validated Code](/images/Sk%C3%A4rmbild%20(136).png)

  ## Bugs 

- Solved
  - At first the game did not run at all. The reason for this was that the first function (def welcome():) needed to be called in the end of the game.
  - The Python libraries did not work when the site was deployed. This could be fixed by typing pip freeze > requirements.txt to add those libraries to the requirements.txt file.
  
- Unsolved
  - none.

  ## Other Featured that can be implemented
   
- One feature that I would like to implement is a stopwatch. By using a threading timer the game can run at the same time as the timer and when the user has played a certain amount of the time the user fails the mission and needs to start over.
- The game has a lot of potential to expand with more paths and tricky questions but in that case the user should not start from the beginning each time the user dies.
- Usage of images would make the game more interactive and interesting.

  ## Deployment 

- GitHub and GitPod.

  - Step one: Create new repositry.
  - Step two: Choose the Code Institute Python template.
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
  - Step eight: Click deploy branch, wait a couple of minutes until the site is deplyed.
  - Step nine: Click view and see the page is live.

  ## Credits 
- Documentation from Code Institute
- Code institute GitPod tamplate. 
- My mentor Spencer
- The slack community
- This article: https://www.askpython.com/python/text-based-adventure-game'
- Stack Overflow: https://stackoverflow.com/
- Geeks for Geeks: https://www.geeksforgeeks.org/
