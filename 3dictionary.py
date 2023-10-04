def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    computer_choice = "paper"
    # dictionary
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

# choices = get_choices()
# print(choices)

# dictionary
dog = {"name":"Roger","age":8}
dog['name'] = "Syd"

# print(dog['name'])
# dog.pop('name')
# print(dog.get("name"))
del dog["name"]

print(dog.keys())
print(dog.values())
print(list(dog.items()))