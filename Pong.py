# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [random.randrange(-5,0),random.randrange(-3,-1)]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == 0:
        ball_vel = [random.randrange(1,5),random.randrange(1,3)]
        ball_pos = [WIDTH / 2, HEIGHT / 2]
    else:
        ball_vel = [random.randrange(-5,-1),random.randrange(1,3)]
        ball_pos = [WIDTH / 2, HEIGHT / 2]        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = (HEIGHT/2) - HALF_PAD_HEIGHT
    paddle2_pos = (HEIGHT/2) - HALF_PAD_HEIGHT
    spawn_ball(1)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global PAD_WIDTH
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    if (ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = - ball_vel[1]
    if ((ball_pos[0] - BALL_RADIUS <= PAD_WIDTH)):
        if(HEIGHT - paddle1_pos > ball_pos[1] and HEIGHT - PAD_HEIGHT - paddle1_pos < ball_pos[1]):
            if(ball_vel[0] < 0):
                ball_vel[0] = ball_vel[0] - 1
            else:
                ball_vel[0] = ball_vel[0] + 1
            ball_vel[0] = - ball_vel[0]
        else:
            score2 += 1
            spawn_ball(0)
    if ((ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH)):
        if(HEIGHT - paddle2_pos > ball_pos[1] and HEIGHT - PAD_HEIGHT - paddle2_pos < ball_pos[1]):
            if(ball_vel[0] < 0):
                ball_vel[0] = ball_vel[0] - 1
            else:
                ball_vel[0] = ball_vel[0] + 1
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball(1)
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Blue", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if (paddle1_pos == 0 or paddle1_pos + PAD_HEIGHT == HEIGHT):
        paddle1_vel = 0
    
    paddle2_pos += paddle2_vel
    if (paddle2_pos == 0 or paddle2_pos + PAD_HEIGHT == HEIGHT):
        paddle2_vel = 0
    # draw paddles   
    canvas.draw_line([HALF_PAD_WIDTH,HEIGHT - paddle1_pos],[HALF_PAD_WIDTH, HEIGHT - PAD_HEIGHT - paddle1_pos], 8, 'Green')
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, HEIGHT - paddle2_pos],[WIDTH - HALF_PAD_WIDTH, HEIGHT - PAD_HEIGHT - paddle2_pos], 8, "Yellow")
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [50,50], 32, 'Blue')
    canvas.draw_text(str(score2), [WIDTH - 50,50], 32, 'Blue')
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    global HEIGHT, PAD_HEIGHT
    if key == simplegui.KEY_MAP['down']:
        if (paddle1_pos == 0):
            paddle1_vel = 0
        else:
            paddle1_vel = paddle1_vel - 5
    elif key == simplegui.KEY_MAP['up']:
        if (paddle1_pos + PAD_HEIGHT == HEIGHT):
            paddle1_vel = 0
        else:
            paddle1_vel = paddle1_vel + 5
    elif key == simplegui.KEY_MAP['w']:
        if (paddle2_pos + PAD_HEIGHT == HEIGHT):
            paddle2_vel = 0
        else:
            paddle2_vel = paddle2_vel + 5
    elif key == simplegui.KEY_MAP['s']:
        if (paddle2_pos == 0):
            paddle2_vel = 0
        else:
            paddle2_vel = paddle2_vel - 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New Game', new_game, 200)

# start frame
new_game()
frame.start()
