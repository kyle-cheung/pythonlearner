import json
from difflib import get_close_matches as gcm

data=json.load(open('data.json', mode='r'))

data = {word.lower() : definition for word, definition in data.items()}

def translate(word):
    word=word.lower()

    if word in data:
        return data[word]
    elif len(gcm(word, data.keys())) > 0 :
        yn = input('Did you mean {s} instead? (Y/N) '.format(s=gcm(word,data.keys())[0]))
        if yn.lower() == 'y':
            return data[gcm(word,data.keys())[0]]
        elif yn.lower() == 'n':
            return 'The word does not exist'
        else:
            return 'We didn\'t understand your response'
        
    else:
        return 'The word does not exist.'

word = input('Enter word: ')

output = translate(word)

if isinstance(output,list):
    for item in output:
        print(item)
else:
    print(output)