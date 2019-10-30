# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random as rand
x = 7
randnumb = 0
# helper function to start and restart the game
def new_game(gamemode):
    # initialize global variables used in your code here
    global x
    global randnumber
    if gamemode == 1:
        print 'New game. Range is 0 to 100'      
        x = 7
        print 'Number of remaining guesses is',x
        randnumber = rand.randrange(0,100)
    else:
        print 'New game. Range is 0 to 1000'
        x = 10
        print 'Number of remaining guesses is',x
        randnumber = rand.randrange(0,1000)
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    new_game(1)
    # remove this when you add your code    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    new_game(2)
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global x
    global randnumber
    print 'Guess was', guess
    print 'Number of remaining guesses is', x-1
    x = x - 1
    if x == 0:
        print 'Oh oh, you ran out of guesses'
        print 'The correct number was',randnumber
        print ''
        new_game(1)
    elif guess > randnumber:
        print 'Lower!'
        print ''
    elif guess < randnumber:
        print 'Higher!'
        print ''
    else:
        print 'Correct!'
        print ''
        new_game(1)
    
    
# create frame
f = simplegui.create_frame('Guess the Number', 200, 200)
f.add_button('Range [0 to 100)', range100, 200)
f.add_button('Range [0 to 1000)', range1000, 200)
f.add_input('Your guess', input_guess, 200)

# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game(1)


# always remember to check your completed program against the grading rubric
