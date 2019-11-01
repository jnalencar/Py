# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def draw(canvas):
    canvas.draw_circle([100, 100], radius, 2, 'Red')
    
def write(canvas):
    canvas.draw_text('Max Radius', [60, 100], 19, 'White')
    canvas.draw_circle([100, 100], radius, 2, 'Red')
# Draw handler
def expand():
    global radius
    global WIDTH
    if radius > WIDTH/2:
        timer.stop()
        frame.set_draw_handler(write)
    else:
        radius = radius + 1
        frame.set_draw_handler(draw)
        
# Create frame and timer
frame = simplegui.create_frame('Expanding Circle', WIDTH, HEIGHT)
timer = simplegui.create_timer(100, expand)
frame.set_draw_handler(draw)

# Start timer
timer.start()
frame.start()
