# This is a rock paper scissors game

# Imports the random module to be used in generatoring the computers turn
import random
# Allows me to access subprocess to clear the terminal after a game
import subprocess as sp
def clearterminal():
    clearterminal = sp.call('clear',shell=True)

# This calls the other functions of the game
def play():

    choices = {'r':'Rock','p':'Paper','s':'Scissors', 0:'Rock',1:'Paper', 2:'Scissors'}

    print("Welcome to Rock-Paper-Scissors!")
    print("See if you can beat the computer...")
    player_choice = user_input(messaging('msg1'), ['r','p','s'])
    print(f"OK... You have chosen {choices[player_choice]}!")
    comp_choice = randomgenerator()
    print(f"The computer chose {choices[comp_choice]}...")
    print("Which means.....")
    result = winlogic(player_choice,comp_choice)
    print(f"You {result}!")

    pagain = user_input(messaging('msg2'),['y','n'])
    if pagain  == 'n':
        clearterminal()
        print("\n\nOk, have a nice day now!\n")
    else:
        clearterminal()
        play()

# Creates random options for the computer player
def randomgenerator():
    comp_choice = random.randrange(0,3,1)
    return comp_choice

# Prompts for user input and checks its valid
def user_input(msg,options):
    choice_made = False
    print(msg)
    while choice_made == False:
        choice_input = input("Your choice >")
        if choice_input in options:
            choice_made = True
            return choice_input
                
        else:
                print(f"Please only enter {options} without [] or ''.")

# Decides who wins each round
def winlogic(player_choice,comp_choice):

    weighting = {'r':0,'p':1, 's':2}
    scoring = {-2:'win', -1:'lose',0:'draw', 1:'win', 2:'lose'}

    logic = weighting[player_choice] - comp_choice
    return scoring[logic]

# A handy place to store messages
def messaging(i):
    messages = {
        'msg1':"Start by entering 'r' for rock, 'p' for paper or 's' for scissors",
        'msg2':"Would you like to play again?"
    }

    return messages[i]

play()