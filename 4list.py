import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    # list
    computer_choice = ['rock','paper','scissors']
    choices = {"player":player_choice,"computer":random.choice(computer_choice)}
    return choices

choices = get_choices()
print(choices)