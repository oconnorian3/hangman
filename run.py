# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows hig
"""
Imports
"""
import random
from words import words
import string 

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

def choose_word(words):
    word = random.choice(words)
    while "_" in word or " "  in word:
        word = random.choice(words)

    return word.upper()
"""
Validate letter and track that is was used
"""
def hangman ():
    word = choose_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
 
    while len(word_letters) > 0:
        print ("You already used: ", " ".join(used_letters)) 

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current Word: "," ".join(word_list))

        user_letter = input ("Guess a letter").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)   

    elif user_letter in used_letters:
        print ("Letter already used. Please try again")

    else:
        print("Invalid Character, Please Try again")               
 