import json
import random

class text_colours:
    GREEN = '\u001b[32;1m'
    WHITE = '\033[0m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35m'


def init_game():
    """
    Welcome user and provide options to play game, set difficulty or view the rules
    """
    print(text_colours.YELLOW + "Welcome to HANGMAN!!" + text_colours.WHITE)
    print("Please press " + text_colours.MAGENTA + "1" + text_colours.WHITE + " to start the game")
    print("Please press " + text_colours.MAGENTA + "2" + text_colours.WHITE + " to choose the difficulty")
    print("Please press " + text_colours.MAGENTA + "3" + text_colours.WHITE + " to view game rules")

    option = input("\n")

        

def pick_randon_word():
    """
    Choose a random word from the words.json file which the player has to guess
    """
    file = open('words.json')
    data = json.load(file)
    random_word = random.choice(data['data'])
    return random_word.upper()


def begin_game(word, total_lives):
    """
    Game play
    """
    lives = total_lives
    dashed_word = "_" * len(word)
    #user_guesses = []

    print("Let's Play! Try not to run out of lives!")
    print("Lives: " + text_colours.BLUE + str(lives) + text_colours.WHITE)
    print("\n")
    print(f" Guess the word: " + " ".join(dashed_word) + "\n")


word = pick_randon_word()
begin_game(word, 7)