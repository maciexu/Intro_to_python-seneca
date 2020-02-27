import json

data = json.load(open("data.json"))
print(type(data))

"rain" in data

print(data["rain"])

import difflib
from difflib import SequenceMatcher
SequenceMatcher(None, "rainn","rain").ratio()
SequenceMatcher(None, "Rain","rain").ratio()

from difflib import get_close_matches
get_close_matches("rainn",["help","book","mom","Rain","rainy"])

get_close_matches("rainn", data.keys())

get_close_matches("rainn", data.keys(), n=5)

get_close_matches("rainn", data.keys())[0]

"""
In this practice, we want to build a dictionary application. This application has the following features:
- It finds the meaning of a word that is in a dictionary file called: data.json. This file is uploaded in
the blackboard.
- If the user enters a word with capital or small letters it converts them to small letters before
searching through the dictionary file
- If the word is found, the meaning is shown. The word may have more than one meaning. In this
case, all the meanings must be shown. Please see the sample outputs, I like to have delimiter
between different items.
- If the word is not found, the application prints a friendly name that the word was not found
- If the word has a spelling error and there is a close word in the dictionary, the application suggests
the close word to the user and asks if user meant that closets word. If the user confirms, shows
the meaning, otherwise exits.
- You have to be careful about nouns user inputs Delhi, Paris, etc. If you just convert all inputs to
lowercase and then tries to find the lowercase version (e.g. delhi) in the dataset and it cannot find
it since the dataset has Delhi, but not delhi. Make sure you have the conditional block so that the
program returns the definition of names that start with a capital letter.
- Please use the following messages in communication with the user. 
"""
user = input("Please enter a word:").lower()

if user in data:
    meaning = data[user]
    for x in meaning:
        print(f"{x} \n ******")
elif user not in data:
    closet_word = get_close_matches(user, data.keys())[0]
    if closet_word not in data:
        print(f"{user} was not found.")
    elif closet_word in data:
        user2 = input(f"Do you mean {closet_word}? Y/N:  ")
        if user2 == "N":
            print("Sorry, there's no such word.")
        elif user2 == "Y":
            meaning2 = data[closet_word]
            for x in meaning2:
                print(f"{x} \n ******")
        
        
    















