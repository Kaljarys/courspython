quotes = [ 
        "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
        "On doit pouvoir choisir entre s'écouter parler et se faire entendre." 
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
user_name = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme")


def show_random_item(my_list):
  #TODO: get a random number
 item = my_list[0] #get an item from the list, just the first one for now
 print(item) #TODO: show the quote in the interpreter
 return "program is over" #returned value

print(show_random_item(quotes))

for character in characters:
    character.capitalize()

  #show another quote
