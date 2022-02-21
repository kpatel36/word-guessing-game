#from PyDictionary import PyDictionary
import random
import string
#dict=PyDictionary()
randomwordlist = ['works', 'tacos', 'apple', 'taboo', 'books', 'nears', 'swill', 'swank', 'paper', 'diffuser', 'bottle', 'essential', 'oil', 'water', 'coffee']

#how to do number of tries left? - while loop - for each correct letter, or incorrect letter or word, add to number of tries list

#print(len(PyDictionary))

spacer=" "
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
#        player_board="  ".join([str(item) for item in player_board])
    return player_board

def letter_guess(guess):
    if guess in guessed_letters:
        print('You\'ve already tried this letter')
    elif guess in unguessed_letters:
        unguessed_letters.remove(guess)
        guessed_letters.add(guess)
        letters_remaining.remove(guess)
        print("GREAT JOB! YOU GOT A LETTER")
        if guess in word_to_guess:
            index=int(0)
            for i in word_to_guess:
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
print(f'Player Board: {player_board}' + f'\nThis word has {len(word_to_guess)} letters in it')

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
            print(player_board)
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