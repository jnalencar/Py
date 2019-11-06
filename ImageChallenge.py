# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
image = simplegui.load_image('https://i.imgur.com/JEmWOdA.png')
imgwid = image.get_width()
imghei = image.get_height()
image_size = [imgwid,imghei]
image_center = [image_size[0]/2.0, image_size[1]/2.0]
mouse = [imgwid, imghei]
# mouseclick handler
def click(pos):
    mouse[0] = pos[0]
    mouse[1] = pos[1]
    
# draw handler
def draw(canvas):
    if(imgwid > 0 and imghei > 0):
        canvas.draw_image(image, image_center, image_size, mouse, image_size)
    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
                                       
