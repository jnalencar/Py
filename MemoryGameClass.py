# implementation of card game - Memory

import simplegui
import random

state = 0
numeros = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
exposed = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
random.shuffle(numeros)
card1 = 0
card2 = 0
card3 = 0
turn = 0
aux = 0

# helper function to initialize globals
def new_game():
    global card1, card2, card3, turn
    exposed = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    random.shuffle(numeros)
    card1 = 0
    card2 = 0
    card3 = 0
    turn = 0

    
# define event handlers
def mouseclick(pos):
    global state, card1, card2,card3, turn
    # add game state logic here
    card1 = pos[0]/50
    if exposed[card1]:
        if state == 0:
            exposed[card1] = False
            card3 = card2
            card2 = card1
            state = 1
        elif state == 1:
            exposed[card1] = False
            turn += 1 
            state = 2
            print turn
            label.set_text('Turn = '+str(turn))
        else:
            if numeros[card2] != numeros[card3]:
                exposed[card2] = True
                exposed[card3] = True
            exposed[card1] = False
            state = 1
        card3 = card2
        card2 = card1
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for num in range(0,17):
        canvas.draw_line([num*50, 0], [num*50, 100], 3, 'Blue')
    for num in range(0,16):
        canvas.draw_text(str(numeros[num]),[12+(num*50),65], 50, 'White')
    for num in range(0,16):
        if exposed[num]:
            canvas.draw_polygon([[num*50,0],[(num+1)*50, 0],[(num+1)*50, 100], [num*50,100]], 2, 'Blue', 'Orange')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turn = '+str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
