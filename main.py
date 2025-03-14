import this
import random        #random is a python library

def get_choices() :                   #def function_name(): is used to define a function
    player_choice = input("enter a choice = ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choices(options)                               #using the library
    choices = {"player":player_choice, "computer":computer_choice}          #Dictionary is used using {}

    return choices           #We should define what the function should return under it.

choices = get_choices()                 #This is calling of function
print(choices)

def check_win(player, computer):
    print(f"you chose {player} computer chose {computer}")      #f makes you include variables inside of the string
    if player == computer:
        return "It's a tie!"          #for return () is optional
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissors!"
    