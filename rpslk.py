# This is a rock paper scissors lizard spock game

# Imports the random module to be used in generatoring the computers turn
import random
# Allows me to access subprocess to clear the terminal after a game
import subprocess as sp
def clearterminal():
    sp.call('clear',shell=True)

# This calls the other functions of the game
def play():

    choices = {'r':'Rock','p':'Paper','s':'Scissors','l':'lizard','k':'spock', 0:'Rock',1:'Paper', 2:'Scissors',3:'spock',4:'lizard'}

    print("Welcome to Rock-Paper-Scissors...Lizard-Spock!")
    print("See if you can beat the computer...")
    player_choice = user_input(messaging('msg1'), ['r','p','s','l', 'k'])
    print(f"OK... You have chosen {choices[player_choice]}!")
    comp_choice = randomgenerator()
    print(f"The computer chose {choices[comp_choice]}...")
    print("Which means.....")
    result = alt_winlogic(player_choice,comp_choice)
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

    weighting = {'r':0,'p':1, 's':2, 'k':3,'l':4}
    scoring = {-4:'win',-3:'lose',-2:'win', -1:'lose',0:'draw', 1:'win', 2:'lose', 3:'win', 4:'lose'}

    logic = weighting[player_choice] - comp_choice

    return scoring[logic]

#to show another way of doing win logic
def alt_winlogic(player_choice_let,comp_choice_num):

    # Dict showing all 'win' possibilities
    weighting = {0:'rock',1:'paper',2:'scissors',3:'lizard',4:'spock'}
    #The original method used maths to determine the winner, we need to change it back to words for this method to work
    letter = {'r':'rock','p':'paper','s':'scissors','l':'lizard','k':'spock'}
    scoring = {
        'rock':['scissors','lizard'],
        'paper':['rock','spock'],
        'scissors':['paper','lizard'],
        'lizard':['paper','spock'],
        'spock':['rock','scissors'] 
    }

    #Converts player letter choice into a full word
    player_choice = letter[player_choice_let]

    #Converts comp choice number into a wordy version
    comp_choice = weighting[comp_choice_num]

    if player_choice == comp_choice:
        return 'draw'
    elif comp_choice in scoring[player_choice]:
        resultant_msgs(player_choice,comp_choice,'win')
        return 'win'
    else:
        resultant_msgs(player_choice,comp_choice,'lose')
        return 'lose'

#Makes the game a little more fun by adding in the result messages
def resultant_msgs(player_choice,comp_choice,result):
    messaging = {
        'rock':{'scissors':'SMASHES scissors','lizard':'squishes lizard'},
        'paper':{'rock':'wraps up rock','spock':'disproves spock'},
        'scissors':{'paper':'cut paper','lizard':'decapitates lizard'},
        'lizard':{'paper':'eats paper','spock':'poisons spock'},
        'spock':{'rock':'vapourises rock','scissors':'breaks scissors'}
    }
    
    #If something goes wrong, the line below lets me know what it was trying to do...
    #print(f"player choice = '{player_choice}', and comp choice = '{comp_choice}'.")
    
    if result == 'win':
        print(f"{player_choice} {messaging[player_choice][comp_choice]}")
        pass

    elif result == 'lose':
        print(f"{comp_choice} {messaging[comp_choice][player_choice]}")
        pass
    else:
        print("Error in resultant messages - contact max!")
        pass

# A handy place to store messages
def messaging(i):
    messages = {
        'msg1':"Start by entering 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard or 'k' for spock",
        'msg2':"Would you like to play again?"
    }

    return messages[i]

play()
