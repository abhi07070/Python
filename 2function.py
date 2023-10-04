# function
def get_choices():
    player_choice = "rock"
    computer_choice = "paper"

    return player_choice
# function
def greeting():
    return "Hi"

response = greeting()
# print(response)

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')