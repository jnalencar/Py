# template for "Stopwatch: The Game"
import simplegui

# define global variables
timelapse = 0
hit = 0
total = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total
    global hit
    timer.stop()
    total = total + 1
    if (timelapse % 10 == 0):
        hit = hit + 1
    
def reset():
    global timelapse
    timelapse = 0

def resethitmiss():
    global hit
    global total
    hit = 0
    total = 0
# define event handler for timer with 0.1 sec interval
def tick():
    global timelapse
    timelapse = timelapse + 1
    print timelapse
    frame.set_draw_handler(draw)

# define draw handler
def draw(canvas):
    global timelapse
    D = timelapse%10
    C = (timelapse%100)/10
    B = (timelapse%600)/100
    A = timelapse/600
    canvas.draw_text(str(A)+':'+str(B)+str(C)+'.'+str(D), [65, 100], 30, 'White')
    canvas.draw_text(str(hit)+'/'+str(total), [85,27], 27, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)
timer = simplegui.create_timer(100, tick)
# register event handlers
frame.add_button('Start', start, 200)
frame.add_button('Stop', stop, 200)
frame.add_button('Reset', reset, 200)
frame.add_button("Reset Hits'n'Misses", resethitmiss, 200)

# start frame
frame.start()
frame.set_draw_handler(draw)

# Please remember to review the grading rubric
