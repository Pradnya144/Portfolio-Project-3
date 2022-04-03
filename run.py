import json

f = open('words.json')
data = json.load(f)

for i in data['data']:
    print(i)

f.close()