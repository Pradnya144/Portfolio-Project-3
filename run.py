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
    user_guesses = []

    print("Let's Play! Try not to run out of lives!")
    print("Lives: " + text_colours.BLUE + str(lives) + text_colours.WHITE)
    print("\n")
    print(f"Guess the word: " + " ".join(dashed_word) + "\n")

    
    while lives > 0:
        player_guess = input("Guess a letter: ").upper()

        try:
            if not player_guess.isalpha():
                raise ValueError(
                    text_colours.RED + "You can only guess alphabets, numbers and special characters are not valid guesses." + text_colours.WHITE
                )
            
            elif len(player_guess) > 1:
                raise ValueError(
                    text_colours.RED + "You can only guess 1 alphabet at a time. This is not a valid guess." + text_colours.WHITE
                )

            elif player_guess.isalpha() and len(player_guess) == 1:
                if player_guess in user_guesses:
                    raise ValueError(
                    f"You have already guessed the letter {(player_guess)}"
                    )

                elif player_guess not in word:
                    print(f"The letter {text_colours.RED}{(player_guess)}{text_colours.WHITE} is not in the word. You lost a life.")

                    user_guesses.append(player_guess)
                    lives -=1
                    print(f"Lives: {lives} \n")

                else:
                    print(f"{text_colours.RED}{(player_guess)}{text_colours.WHITE} is in the word. Good guess!")

                    user_guesses.append(player_guess)
                    word_list = list(dashed_word)
                    indices = [i for i, letter in enumerate(word)
                               if letter == player_guess]
                    for index in indices:
                        word_list[index] = player_guess
                        dashed_word = "".join(word_list)

                    if "_" not in dashed_word:
                        print("YOU WON")
                        print(f"The word is {word}")
                        break

                    else:
                        print(f"Guess the word: " + " ".join(dashed_word) + "\n")
                        print("Letters guessed: " + ", ".join(sorted(user_guesses)) + "\n")


        except ValueError as e:
            print(f"{e} Please try again \n")
            continue

    if lives == 0:
        print(f"The word was {word}")
        print("YOU LOST!")


word = pick_randon_word()
begin_game(word, 7)