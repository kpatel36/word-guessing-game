#!/usr/bin/env python
# coding: utf-8

# **Create a Letter Guessing Game**
# 
# Create a program that allows a user 7 chances to guess the correct word. If they do not guess the word after 7 tries, the player loses and the program will print the correct word. Otherwise, the play wins and the game.
# 
# **How to build the program**
# * When you start the game, you will need to select a random word from a list of at least 10 words (You have full control over which words you want to use for you program). This will be your secret word. Your secret word will be represented in the program as a group of underscores. For as long as the word is, you should also have that many underscores. 
# 
# * Once the word is selected, your game will commence. Perform a Google search to figure out how to select a random word from a list using Python.<br>
# **Hint** There's package you can import into your application that does this for you.
# 
# * The end user will have a total of 7 chances to guess the correct letter from the secret word. If the end user makes 7 incorrect guesses, the game will end.
# 
# * As you guess the correct letters, the letters you have guess will then take place of the underscores that letter represents. <br>
# **For Example**: If your secret word is 'watermelon' and  so far you have guessed the letters 'a' and 'e', the word you're trying to guess will appear as follows: _ a _ e _ _ e _ _ _.<br>
# **Keep in mind** that if you guess a letter that appears more than once in your secret word, make sure that the letter is populated anywhere that letter would be.

# In[8]:


import random
import string
randomwordlist = ['works', 'tacos', 'apple', 'orange', 'banana', 'papaya', 'potato', 'lettuce', 'salsa', 'tomato', 'taboo',
                  'books', 'nears', 'swill', 'swank', 'paper', 'diffuser', 'bottle', 'essential', 'oil', 'water', 'coffee', 'eraser']

number_of_tries = 0
number_of_tries_left = 7
player_board = []
guessed_letters = set() # what letters have been guessed - includes both incorrect and correct guesses
incorrect_letters = set() # what incorrect letters player has guessed
word_guess = set()
letters_remaining=set(string.ascii_uppercase)
#guessed_letters, incorrect_letters, and word_guesses - all sets to prevent repetition of entries

picked = random.choice(randomwordlist)
word = picked
word_to_guess = list(word.upper())
unguessed_letters =set(word_to_guess.copy())

def set_up():
    for letter in word_to_guess:
        player_board.append('_')
    return player_board

def letter_guess(guess):
    if guess in guessed_letters:
        print('You\'ve already tried this letter')
    elif guess in unguessed_letters:
        unguessed_letters.remove(guess)
        guessed_letters.add(guess)
        letters_remaining.remove(guess)
        print("Great Job! You got one of the letters!")
        if guess in word_to_guess:
            index=int(0)
            for i in word_to_guess: #for if there is multiple occurences of the same letter in the word
                if i==guess:
                    player_board[index]=guess
                index+=1
    else:
        print(f'Sorry - {guess} - is not a letter in this word. Try again')
        guessed_letters.add(guess)
        letters_remaining.remove(guess)
        incorrect_letters.add(guess)

def word_guesses(guess):
    if guess in word_guess:
        print('Sorry you\'ve already guessed this word, and it is incorrect, try again')
    else:
        word_guess.add(guess)
        print(guess + ' added to incorrect word guesses')    

def player_guess (guess):
    if len(guess) <=1:
        letter_guess(guess)
    elif guess == "QUIT":
        print('trying to quit')
    elif guess== word.upper():
        print ("Congrats! You got it! You Win!")
    elif len(guess) >= 1:
        word_guesses(guess)

set_up()
#player_board_string ="_".join([str(item) for item in player_board])
print(*player_board, sep =" ")
print(f'\nThis word has {len(word_to_guess)} letters in it')

while len(unguessed_letters)>0 and number_of_tries_left > 0:
    guess = (str(input('Guess a letter,the word, or type quit: ').upper()))
    if guess == word.upper():
        print("You did it!")
        break
    elif guess == "QUIT":
        print(f"Maybe next time! The word was {word.upper()}")
        break
    elif guess != word.upper():
        player_guess(guess)
        if player_board == word_to_guess:
            print(word.upper())
            print('You guessed the right word!')
            break
        else:
            print(*player_board, sep = " ")
            print('GUESSED LETTERS: ' + str(guessed_letters))
            number_of_tries_left = number_of_tries_left - 1
            number_of_tries += 1
            if number_of_tries_left > 1:
                print('You have ' + str(number_of_tries_left) + ' tries left.')
            elif number_of_tries_left == 1:
                print('You have ' + str(number_of_tries_left) + ' try left.')
        print('---------------------------------------------')
else:
    print(f"Maybe next time! The word was {word.upper()}")


# In[ ]:




