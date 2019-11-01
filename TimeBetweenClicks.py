# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global first_click
    global total_ticks
    if first_click == 'True':
        total_ticks = 0
        timer.start()
        first_click = 'False'
    else:
        timer.stop()
        first_click = 'True'
        frame.set_draw_handler(draw)
        
def draw(canvas):
    global total_ticks
    canvas.draw_text('Your time between clicks was '+str(total_ticks)+' ms', [20, 100], 19, 'Red')

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 350, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
