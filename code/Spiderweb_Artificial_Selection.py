# Import Libraries
from tkinter import *
from math import cos
from math import sin
from math import pi
from math import degrees
from math import fsum
from copy import deepcopy
import random
import numpy as np

# Import my libraries
# For creating the initial web
from initialization import canvas_initialization
from initialization import web_initialization

from draw_web_init import draw_web_initial

# For mutation of the web to produce 8 child webs
from UpdateWeb import update
from UpdateWeb import change_angle
from UpdateWeb import change_length
from UpdateWeb import spiral_thread_TF
from UpdateWeb import change_spiral_thread_length

# To create scattereed insect pattern
from Insects import draw_insects

# Draws the web in a canvas
def draw_web(Thread_Data_Points, my_canvas, web_origin):
    # Create Radial Threads

    for i in range(len(Thread_Data_Points[0])):
        my_canvas.create_line(web_origin,Thread_Data_Points[0][i], fill='black', width=2) # Create line between origin a radial point in TkInter

    # Create Spiral Threads
    for i in range(len(Thread_Data_Points)): # For all sprial threads (Default 20)
        for j in range(len(Thread_Data_Points[1])): # Over all radial threads (Default 8)
            if j == (len(Thread_Data_Points[0])-1):
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][0], fill='black', width=2) # Connect ends of first and last radial threads
            else:
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][j+1], fill='black', width=2) # Connect ends of adjacent radial thread clockwise
            
    return my_canvas

def draw_to_window(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin):
    # Naming convention based upon how the canvas is presented ot hte user.
    # [00, 01, 02]
    # [10, 11, 12]
    # [20, 21, 22]
    
    # Initialize all canvases for drawining with TkInter. Name, canvas dimensions, background color.
    my_canvas_00 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_01 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_02 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_10 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_11 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_12 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_20 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_21 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
    my_canvas_22 = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')
 
    # Copying all properties of the parent web to all children web. All 9 webs will hold the same genetic code
    Thread_Data_Points_00, Thread_Data_Angles_00, Thread_Length_00, Thread_Spiral_Length_00, Thread_TF_00 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_01, Thread_Data_Angles_01, Thread_Length_01, Thread_Spiral_Length_01, Thread_TF_01 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_02, Thread_Data_Angles_02, Thread_Length_02, Thread_Spiral_Length_02, Thread_TF_02 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_10, Thread_Data_Angles_10, Thread_Length_10, Thread_Spiral_Length_10, Thread_TF_10 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_11, Thread_Data_Angles_11, Thread_Length_11, Thread_Spiral_Length_11, Thread_TF_11 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_12, Thread_Data_Angles_12, Thread_Length_12, Thread_Spiral_Length_12, Thread_TF_12 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_20, Thread_Data_Angles_20, Thread_Length_20, Thread_Spiral_Length_20, Thread_TF_20 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_21, Thread_Data_Angles_21, Thread_Length_21, Thread_Spiral_Length_21, Thread_TF_21 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)
    Thread_Data_Points_22, Thread_Data_Angles_22, Thread_Length_22, Thread_Spiral_Length_22, Thread_TF_22 = deepcopy(Thread_Data_Points), deepcopy(Thread_Data_Angles), deepcopy(Thread_Length), deepcopy(Thread_Spiral_Length), deepcopy(Thread_TF)

    # Mutating the genetic data of all webs. The first plot is not modified, as the parent remains constant from previous generation.
    Thread_Data_Points_01 = update(Thread_Data_Points_01, Thread_Data_Angles_01, Thread_Length_01, Thread_Spiral_Length_01, Thread_TF_01, canvas_height, canvas_width)
    Thread_Data_Points_02 = update(Thread_Data_Points_02, Thread_Data_Angles_02, Thread_Length_02, Thread_Spiral_Length_02, Thread_TF_02, canvas_height, canvas_width)
    Thread_Data_Points_10 = update(Thread_Data_Points_10, Thread_Data_Angles_10, Thread_Length_10, Thread_Spiral_Length_10, Thread_TF_10, canvas_height, canvas_width)
    Thread_Data_Points_11 = update(Thread_Data_Points_11, Thread_Data_Angles_11, Thread_Length_11, Thread_Spiral_Length_11, Thread_TF_11, canvas_height, canvas_width)
    Thread_Data_Points_12 = update(Thread_Data_Points_12, Thread_Data_Angles_12, Thread_Length_12, Thread_Spiral_Length_12, Thread_TF_12, canvas_height, canvas_width)
    Thread_Data_Points_20 = update(Thread_Data_Points_20, Thread_Data_Angles_20, Thread_Length_20, Thread_Spiral_Length_20, Thread_TF_20, canvas_height, canvas_width)
    Thread_Data_Points_21 = update(Thread_Data_Points_21, Thread_Data_Angles_21, Thread_Length_21, Thread_Spiral_Length_21, Thread_TF_21, canvas_height, canvas_width)
    Thread_Data_Points_22 = update(Thread_Data_Points_22, Thread_Data_Angles_22, Thread_Length_22, Thread_Spiral_Length_22, Thread_TF_22, canvas_height, canvas_width)

    # Implementing buttons to select best web
    my_button_00 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_00, Thread_Data_Angles_00, Thread_Length_00, Thread_Spiral_Length_00, Thread_TF_00, web_origin))
    my_button_01 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_01, Thread_Data_Angles_01, Thread_Length_01, Thread_Spiral_Length_01, Thread_TF_01, web_origin))
    my_button_02 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_02, Thread_Data_Angles_02, Thread_Length_02, Thread_Spiral_Length_02, Thread_TF_02, web_origin))
    my_button_10 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_10, Thread_Data_Angles_10, Thread_Length_10, Thread_Spiral_Length_10, Thread_TF_10, web_origin))
    my_button_11 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_11, Thread_Data_Angles_11, Thread_Length_11, Thread_Spiral_Length_11, Thread_TF_11, web_origin))
    my_button_12 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_12, Thread_Data_Angles_12, Thread_Length_12, Thread_Spiral_Length_12, Thread_TF_12, web_origin))
    my_button_20 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_20, Thread_Data_Angles_20, Thread_Length_20, Thread_Spiral_Length_20, Thread_TF_20, web_origin))
    my_button_21 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_21, Thread_Data_Angles_21, Thread_Length_21, Thread_Spiral_Length_21, Thread_TF_21, web_origin))
    my_button_22 = Button(my_window, text='Select Above', command=lambda: button_press(Thread_Data_Points_22, Thread_Data_Angles_22, Thread_Length_22, Thread_Spiral_Length_22, Thread_TF_22, web_origin))
    
    # Generate random array of insects
    s1, s2, insect_number = draw_insects(web_origin)
    for i in range(len(s1)):

        # Draw insects using TkInter. Circle, start position x, start position y, end position x, end position y, red color.
        my_canvas_00.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_01.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_02.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_10.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_11.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_12.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_20.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_21.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')
        my_canvas_22.create_oval(s1[i],s2[i],s1[i]+insect_number/100, s2[i]+insect_number/100, fill='red', outline='red')

    # Overlay the web onto the canvas in TkInter
    my_canvas_00 = draw_web(Thread_Data_Points_00, my_canvas_00, web_origin)
    my_canvas_01 = draw_web(Thread_Data_Points_01, my_canvas_01, web_origin)
    my_canvas_02 = draw_web(Thread_Data_Points_02, my_canvas_02, web_origin)
    my_canvas_10 = draw_web(Thread_Data_Points_10, my_canvas_10, web_origin)
    my_canvas_11 = draw_web(Thread_Data_Points_11, my_canvas_11, web_origin)
    my_canvas_12 = draw_web(Thread_Data_Points_12, my_canvas_12, web_origin)
    my_canvas_20 = draw_web(Thread_Data_Points_20, my_canvas_20, web_origin)
    my_canvas_21 = draw_web(Thread_Data_Points_21, my_canvas_21, web_origin)
    my_canvas_22 = draw_web(Thread_Data_Points_22, my_canvas_22, web_origin)

    # Position of canvases for display to user
    my_canvas_00.grid(row=0, column=0)
    my_canvas_01.grid(row=0, column=1)
    my_canvas_02.grid(row=0, column=2)
    my_canvas_10.grid(row=2, column=0)
    my_canvas_11.grid(row=2, column=1)
    my_canvas_12.grid(row=2, column=2)
    my_canvas_20.grid(row=4, column=0)
    my_canvas_21.grid(row=4, column=1)
    my_canvas_22.grid(row=4, column=2)

    # Position of buttons for display to user
    my_button_00.grid(row=1, column=0)
    my_button_01.grid(row=1, column=1)
    my_button_02.grid(row=1, column=2)
    my_button_10.grid(row=3, column=0)
    my_button_11.grid(row=3, column=1)
    my_button_12.grid(row=3, column=2)
    my_button_20.grid(row=5, column=0)
    my_button_21.grid(row=5, column=1)
    my_button_22.grid(row=5, column=2)
    
    # Display array of canvases
    my_window.mainloop()
    return button_press

#When button is pressed / web is slected
def button_press(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin):
    my_canvas.delete("all") # Remove old window
    my_window.quit() # Clear old window
    # Repeat function
    draw_to_window(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin)

# CREATE INITIAL WEB

# Set up initial canvas. 300x300 pixels in size.
canvas_width, canvas_height, my_canvas, my_window = canvas_initialization(300)

#Set up initial web. Dimensions of web, number of radial threads, number of spiral threads per radial thread. 8 radial threads, 20 spiral threads (default)
Thread_Data_Angles, Thread_Data_Points, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin = web_initialization(canvas_width, canvas_height, 8, 20)
# Create first parent web
my_canvas = draw_web_initial(Thread_Data_Points, my_canvas, web_origin)

# Modify web
for k in range(200): # For 500 generations
    my_canvas.delete("all") # Remove old window
    # Run function that produces 8 child webs
    draw_to_window(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin)
