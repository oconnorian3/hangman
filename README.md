# Hangman #

This is an application built using python which allows the user play a game of Hangman. The user has 7 lives to guess the word correctly.

![](assets/images/responsivness.png)

## UX/UI ##

   * This is an application run over a python terminal with easy to follow instructions to get started. 

## Features ##

 * Navigation

    * Once the game begins the user is given a breakdown on how to play the game and is prpmpted to enter their name

    ![](assets/images/startgame.png)

    * If the user uses a non alpha character they recevie the below message,

    ![](assets/images/invalidname.png)

    * If the user enters a valid name they will see the below,

    ![](assets/images/validname.png)

    * Once the game begins the copmputer will pick a random word from a list of 50 seen in the word.py file. the user will then be able to guess the correct letters. The user will be allowed 7 incorrect answers . Each incorrect answer will add an element to the hangman illustration . If the player looses the familiar hangman illustration will complete along with a messagecrevealing the word.

    ![](assets/images/loosingmessage.png)

    * If the user wins the will see the below message.

    ![](assets/images/wingame.png)  

    * The users lives are kept track off during the game.
    * If the user enters a non alpha value or repeat a previous guess the game will not accept the answer and will ask them to guess again. 

    ![](assets/images/errormsg.png)

    * Once the game finishes the user will be given the option to restart the game

    ![](assets/images/restartgame.png)

 
# Testing #

  * This site works in thebrowsers, Chrome & Firefox. It does not run in Safari which looks to be a common issue with Heroku and Safari (sample thread ,many more) https://stackoverflow.com/questions/69526899/heroku-application-not-accessible-on-safari
   * I confirmed that the game gives clear instructions and the flow of the game meakes sense
   * I confirmed that the functions all work as designed and corretly give the expected responses to the user.

**Bugs** 

*Solved Problems*

  * Heroku deploys started to fail . This was due to me adding a dependency to the requirements.txt file using an incorrect syntax. Heroku did not recognise the dependency and failed to deploy as a result. Reading the Heroku build logs gave an error which prompted me to double checy the syntax.

**Validator Testing**

* HTML
   * No errors were retuned when passing through the official W3C validator

```
https://validator.w3.org/nu/?doc=https%3A%2F%2Foconnorian3.github.io%2Fallthingsspace%2Fyourimages.html
```
```
https://validator.w3.org/nu/?doc=https%3A%2F%2Foconnorian3.github.io%2Fallthingsspace%2Fcontactus.html
```
```
https://validator.w3.org/nu/?doc=https%3A%2F%2Foconnorian3.github.io%2Fallthingsspace%2Findex.html
```

* CSS
   * No errors were retuned when passing through the official (Jigsaw) validator

```
https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Foconnorian3.github.io%2Fallthingsspace%2Fassets%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
```
    
* Accessibility
  * The colours and fonts are easy to read by passing it through the lighthouse in dev tools.

![](assets/images/Lighouthouse-score.png)     

# Deployment #

**The application was deployed to Heroku. The steps to deploy are as follows:** 

  1. I logged into my personal Heroku account page, select Create new app, give a name to the new app, choose a region from the drop down list toEurope. Then click Create app.

  2. Go to the Settings tab afterwards, click Add buildpack button on the right side of the Buildpacks section, first select python and add it, then select nodejs and add it.
    
  3. Go to the Deploy tab, click GitHub in the Deployment method section, search for the repo on GitHub, click Connect.

  4. In the Manual deploy section, seclect main and then click Deploy Branch button, the app was successfully deployed after a while.

  5. Click the View button on the bottom of the page or the Open app button on the top right corner to view the programme.

  6.  The live link can be found here - https://hangmaniano.herokuapp.com/

# Credits #

* Content

  * Watched a tutorial by [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8&list=PLqoebFJFAtg940mqPamWw4_ndWbnfqFqh) on YouTube
  
