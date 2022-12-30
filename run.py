"""
Imports
"""
import random
from words import words
import string 
from visual import hangman_drawing
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

"""
Start game function
"""
def startgame ():
    startgame = print("How to play. Hangman is a simple word guessing game.\n Players try to figure out an unknown word by guessing letters.\n If too many letters which do not appear in the word are guessed,\n the player is hanged and loses")

    while True:
      try:
        name = input('What is your name?\n').upper()
        if name.isalpha():
            print(Fore.LIGHTGREEN_EX +'Hi',Fore.LIGHTGREEN_EX + name, Fore.LIGHTGREEN_EX +'Lets play Hangman!')
            break    
        else:
            print(Fore.RED + "Invalid Name")      
      except ValueError:
            print("Provide an Alpha value...")
      continue
"""
Pull random word
"""

def choose_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
"""
Function to begin the game itself
"""
def hangman ():
    word = choose_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
 
    while len(word_letter) > 0 and lives > 0:
        print("You have", lives, "lives left and the following letters have been used ", ' '.join(used_letters)) 

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(hangman_drawing[lives])
        print('Current Word: ', ' '.join(word_list))

        user_letter = input("Guess a letter:\n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)  
                print("") 

            else:
                lives = lives -1
                print ('\nYour Letter,', user_letter, 'is not in the word')     

        elif user_letter in used_letters:
            print ("\nLetter already used. Please try again")

        else:
            print("\nInvalid Character, Please Try again") 

    if lives == 0:
        print(hangman_drawing[lives])
        print(Fore.RED + 'You died, sorry. The word was', word)
    else:
        print(Fore.LIGHTGREEN_EX +'Woo Hoo !!! You guessed the word', word, '!!')
    """
    Gives user option to restart game
    """
    user_input = input("Would you like to play hangman again? Type 'Yes' or 'No'\n\n")

    if user_input.lower() == "no": 
        return False
    elif user_input.lower() == "yes":
        hangman()    


if __name__ == '__main__':
    startgame()
    hangman()             
 