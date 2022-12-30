"""
Imports
"""
import random
from words import words
import string 
from visual import hangman_drawing

"""
Welcome message, plus name validator.
"""
startgame = print("How to play. Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters. If too many letters which do not appear in the word are guessed, the player is hanged and loses")

while True:
  try:
    name = input('What is your name?\n').upper()
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
    while '_' in word or ' ' in word:
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
        print('You died, sorry. The word was', word)
    else:
        print('Congratualtions! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()              
 