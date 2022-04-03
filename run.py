import json

class text_colours:
    GREEN = '\u001b[32;1m'
    WHITE = '\033[0m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35m'


print(text_colours.YELLOW + "Hello" + text_colours.MAGENTA + " World")


#f = open('words.json')
#data = json.load(f)

#for i in data['data']:
#    print(i)

#f.close()