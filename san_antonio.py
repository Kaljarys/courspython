quotes = [ 
        "\"Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !\"",
        "\"On doit pouvoir choisir entre s'écouter parler et se faire entendre.\"" 
]
characters = [
        "alvin et les chipmunks",
        "Babar",
        "Betty Boop",
        "Calimero",
        "Casper",
        "le chat potté",
        "Kirikou",
]


import random

def get_random_item(object_list):
 rand_numb = random.randint(0, len(object_list) - 1) # get a random number
 item = object_list[rand_numb] #get an item from the list, just the first one for now
 return item #return the item

def capitalize(words):
    for word in words:
        return word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit {}".format(character, quote)

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme")


  #show another quote
