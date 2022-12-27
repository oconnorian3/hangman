# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows hig
"""
Imports
"""
import random
from words import words

"""
Welcome message, plus name validator. 
"""
startgame = print("How to play. Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters. If too many letters which do not appear in the word are guessed, the player is hanged and loses")

while True:
  try:
    name = input('What is your name?').upper()
    if name.isalpha():
      print('Hi', name, 'Lets play Hangman!')
      break 
    else:
      print("Invalid Name")      
  except ValueError:
    print("Provide an Alpha value...")
    continue

"""
Pull random word
"""
def choose_word():
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word


      
