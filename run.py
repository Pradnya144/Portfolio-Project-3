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
    Welcome user and provide options to play game,
    set difficulty or view the rules
    """
    print(text_colours.YELLOW + "Welcome to HANGMAN!!" + text_colours.WHITE)
    print(
        "Please press " + text_colours.MAGENTA + "1" +
        text_colours.WHITE + " to start the game"
        )
    print(
        "Please press " + text_colours.MAGENTA + "2" +
        text_colours.WHITE + " to choose the difficulty"
        )
    print(
        "Please press " + text_colours.MAGENTA + "3" +
        text_colours.WHITE + " to view game rules"
        )

    option = False
    while not option:
        num = input("\n")
        if num == "1":
            option = True
            difficulty = "medium"
            return difficulty

        elif num == "2":
            option = True

        elif num == "3":
            option = True
            game_rules()

        else:
            print(
                text_colours.RED +
                "Please select 1,2 or 3 " + text_colours.WHITE)


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
    game_over = False

    print("Let's Play! Try not to run out of lives!")
    print("Lives: " + text_colours.BLUE + str(lives) + text_colours.WHITE)
    print("\n")
    print(f"Guess the word: " + " ".join(dashed_word) + "\n")

    while lives > 0 and not game_over:
        player_guess = input("Guess a letter: ").upper()

        try:
            if not player_guess.isalpha():
                raise ValueError(
                    text_colours.RED + "You can only guess alphabets,"
                    " numbers and special characters are not valid guesses." +
                    text_colours.WHITE
                )

            elif len(player_guess) > 1:
                raise ValueError(
                    text_colours.RED +
                    "You can only guess 1 alphabet at a time."
                    " This is not a valid guess." + text_colours.WHITE
                )

            elif player_guess.isalpha() and len(player_guess) == 1:
                if player_guess in user_guesses:
                    raise ValueError(
                        f"You have already guessed the letter {player_guess}"
                    )

                elif player_guess not in word:
                    message = f"The letter {text_colours.RED}{(player_guess)}"\
                              f"{text_colours.WHITE} is not in the word."\
                              " You lost a life."

                    user_guesses.append(player_guess)
                    lives -= 1

                else:
                    message = f"{text_colours.GREEN}{(player_guess)}"\
                              f"{text_colours.WHITE} is in the word."\
                              " Good guess!"

                    user_guesses.append(player_guess)
                    word_list = list(dashed_word)
                    indices = [i for i, letter in enumerate(word)
                               if letter == player_guess]
                    for index in indices:
                        word_list[index] = player_guess
                        dashed_word = "".join(word_list)

                    if "_" not in dashed_word:
                        game_over = True

        except ValueError as e:
            print(f"{e} Please try again \n")
            continue

        print(hangman_graphics(lives))

        if lives > 0:
            print(message)
            print(f"Guess the word: " + " ".join(dashed_word) + "\n")
            print("Letters guessed: " + ", ".join(sorted(user_guesses)) + "\n")
            print(f"Lives: {text_colours.BLUE}{lives}{text_colours.WHITE} \n")

    if lives == 0:
        print(f"The word was {word}")
        looser()

    if game_over:
        winner()
        print(f"{text_colours.GREEN} Congratulations!"
              " The word was {word} {text_colours.WHITE}")

    game_restart(total_lives)


def game_restart(total_lives):
    """
    Player can choose whether to play the game again
    """
    valid_input = False
    while not valid_input:

        play_again = input("Press Y to play again "
                           "Press D to choose difficulty "
                           "Press Q to quit the game : \n").upper()

        try:
            if play_again == "Y":
                valid_input = True
                word = pick_randon_word()
                begin_game(word, total_lives)

            if play_again == "D":
                valid_input = True
                total_lives = select_difficulty()
                word = pick_randon_word()
                begin_game(word, total_lives)

            elif play_again == "Q":
                valid_input = True
                main()

            else:
                raise ValueError(
                    "Please press Y,D or Q"
                )

        except ValueError as e:
            print(f"{e}")


def select_difficulty():
    """
    Player can select the level of difficulty
    """
    print("Select the level of difficulty \n")
    print(
        " Press " + text_colours.MAGENTA + "E" +
        text_colours.WHITE + " for Easy"
        )
    print(
        " Press " + text_colours.MAGENTA + "M" +
        text_colours.WHITE + " for Medium"
        )
    print(
        " Press " + text_colours.MAGENTA + "H" +
        text_colours.WHITE + " for Hard"
        )
    difficulty = False
    while not difficulty:
        choice = input("\n ").upper()
        if choice == "E":
            difficulty = True
            total_lives = 10
            return total_lives
        elif choice == "M":
            difficulty = True
            total_lives = 7
            return total_lives
        elif choice == "H":
            difficulty = True
            total_lives = 5
            return total_lives
        else:
            print(text_colours.RED + "\n Please select E, M or H to make your"
                  " choice" + text_colours.WHITE)


def game_rules():
    """
    Brief explanation of how to play the game
    """
    print(
        """
        Input one letter at a time and 
        try to guess the word. For every
        wrong guess, you will lose a life.
        When you are left with 0 lives, you
        will be hanged and that's game over!! \n
        """
    )

    return_menu = input(text_colours.GREEN + "Press enter to return to the main menu \n" + text_colours.WHITE)
    main()


def winner():
    """
    Ascii graphics for 'you won'
    """
    print(
        text_colours().GREEN + """

 ##    ##  #######  ##     ##   ##      ##  #######  ##    ## 
  ##  ##  ##     ## ##     ##   ##  ##  ## ##     ## ###   ## 
   ####   ##     ## ##     ##   ##  ##  ## ##     ## ####  ## 
    ##    ##     ## ##     ##   ##  ##  ## ##     ## ## ## ## 
    ##    ##     ## ##     ##   ##  ##  ## ##     ## ##  #### 
    ##    ##     ## ##     ##   ##  ##  ## ##     ## ##   ### 
    ##     #######   #######     ###  ###   #######  ##    ## 
        
       """ + text_colours().WHITE
    )

def looser():
    """
    Ascii graphics for 'you lost'
    """
    print(
        text_colours().RED + """
        
 ##    ##  #######  ##     ##   ##        #######   ######  ######## 
  ##  ##  ##     ## ##     ##   ##       ##     ## ##    ##    ##    
   ####   ##     ## ##     ##   ##       ##     ## ##          ##    
    ##    ##     ## ##     ##   ##       ##     ##  ######     ##    
    ##    ##     ## ##     ##   ##       ##     ##       ##    ##    
    ##    ##     ## ##     ##   ##       ##     ## ##    ##    ##    
    ##     #######   #######    ########  #######   ######     ##    
   
   """ + text_colours().WHITE
    )

def game_logo():
    """
    Ascii graphics for Hangman logo
    """
    print( 
        f"""
        {text_colours().BLUE} 
    ##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ## 
    ##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ## 
    ##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ## 
    ######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ## 
    ##     ## ######### ##  #### ##    ##  ##     ## ######### ##  #### {text_colours().YELLOW}
    ##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ### 
    ##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ## 
        {text_colours().WHITE} 
        """
    )

def hangman_graphics(lives):
    """
    Display graphics based on number of lives a player has
    """
    hangman_lives = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """






        """
    ]

    return hangman_lives[lives]


def main():
    """
    Main function of the game
    """
    game_logo()
    difficulty = init_game()
    if difficulty == "medium":
        total_lives = 7
    else:
        total_lives = select_difficulty()

    word = pick_randon_word()
    begin_game(word, total_lives)


main()