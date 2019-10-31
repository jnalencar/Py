# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH/2, HEIGHT/2], ball_radius, 2, 'Red')


# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius = ball_radius + RADIUS_INCREMENT
    frame.set_draw_handler(draw)
    
def decrease_radius():
    global ball_radius
    ball_radius = ball_radius - RADIUS_INCREMENT
    frame.set_draw_handler(draw)

def up_in_frame():
    global HEIGHT
    HEIGHT = HEIGHT - 5
    frame.set_draw_handler(draw)
    
def down_in_frame():
    global HEIGHT
    HEIGHT = HEIGHT + 5
    frame.set_draw_handler(draw)
    
def left_in_frame():
    global WIDTH
    WIDTH = WIDTH - 5
    frame.set_draw_handler(draw)
    
def right_in_frame():
    global WIDTH
    WIDTH = WIDTH + 5
    frame.set_draw_handler(draw)
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)
frame.add_button("Up in frame", up_in_frame)
frame.add_button("Down in frame", down_in_frame)
frame.add_button("Left in frame", left_in_frame)
frame.add_button("Right in frame", right_in_frame)


# Start the frame animation
frame.start()

