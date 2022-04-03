import json

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

        


init_game()
#f = open('words.json')
#data = json.load(f)

#for i in data['data']:
#    print(i)

#f.close()