# GUI-based version of RPSLS

###################################################

import simplegui
import random

# Functions that compute RPSLS

global player_choice

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if (name == 'rock'):
        return 0
    elif (name == 'Spock'):
        return 1
    elif (name == 'paper'):
        return 2
    elif (name == 'lizard'):
        return 3
    else:
        return 4


def number_to_name(number): 
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'Spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    else:
        return 'scissors'

def rpsls(player_choice):     
    # print a blank line to separate consecutive games
    # IT IS IN THE LAST LINE
    # print out the message for the player's choice
    print ('Player chooses ' + player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print ('Computer chooses ' + comp_choice)
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (diff == 0):
        print ('Player and computer tie!')
    elif (diff > 2):
        print ('Player wins!')
    else:
        print ('Computer wins!')
    
    print ('')     
    
# Handler for input field
def get_guess(guess):
    if(guess == 'rock' or guess == 'Spock' or guess == 'paper' or guess == 'paper' or guess == 'lizard' or guess == 'scissors'):
        rpsls(guess)
    else:
        print 'Error: Bad Input'
        print ''


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
