#Import Python Libraries
from tkinter import *
from math import cos
from math import sin
from math import pi
from math import degrees
from math import fsum
from math import sqrt
from copy import deepcopy
import time
import random
import numpy as np
import gc
import PIL.Image as Image
from PIL import ImageDraw

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
def draw_web(Thread_Data_Points, my_canvas, draw_image, web_origin):
    # Create Radial Threads
    black = (0,0,0) # COlor of web
    web_length = 0 # Store length of web for fitness function
    for i in range(len(Thread_Data_Points[0])): # For Construction and evaluation of radial threads
        my_canvas.create_line(web_origin,Thread_Data_Points[0][i], fill='black', width=2) # Create line between origin a radial point in TkInter
        draw_image.line([web_origin,Thread_Data_Points[0][i]], black, 2) # Create line between origin a radial point in PIL
        web_length += abs(np.subtract(web_origin,Thread_Data_Points[0][i])) # Add distance

    # Create Spiral Threads
    for i in range(len(Thread_Data_Points)): # For all sprial threads (Default 20)
        for j in range(len(Thread_Data_Points[1])): # Over all radial threads (Default 8)
            if j == (len(Thread_Data_Points[0])-1): # Connect ends of adjacent spiral thread clockwise
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][0], fill='black', width=2) # Connect ends of first and last radial threads in TkInter
                draw_image.line([Thread_Data_Points[i][j],Thread_Data_Points[i][0]], black, 2) # # Connect ends of first and last radial threads in PIL
                web_length += abs(np.subtract(Thread_Data_Points[i][j],Thread_Data_Points[i][0])) # Add distance
            else: # Connect first and last radial threads together to form final frame thread
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][j+1], fill='black', width=2) # Connect ends of adjacent radial thread clockwise in PIL
                draw_image.line([Thread_Data_Points[i][j],Thread_Data_Points[i][j+1]], black, 2) # Connect ends of adjacent radial thread clockwise in PIL
                web_length += abs(np.subtract(Thread_Data_Points[i][j],Thread_Data_Points[i][j+1])) # Add distance
    
    web_length = fsum(web_length) # Get total x and y distance of thread used            
            
    return my_canvas, draw_image, web_length

# To draw webs for the user using TkInter and store in PIL
def draw_to_window(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin, generation):
    # Define colors used for PIL
    white = (255,255,255)
    red = (255,0,0)

    #Increase generation count for display
    generation +=1

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

    # Initialize all canvases for drawining with PIL. RGB coloring, canvas dimensions, background color.
    my_image_default = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_00 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_01 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_02 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_10 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_11 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_12 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_20 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_21 = Image.new("RGB", (canvas_width, canvas_height), white)
    my_image_22 = Image.new("RGB", (canvas_width, canvas_height), white)

    # Setting canvases to be drawn upon in PIL
    draw_image_default = ImageDraw.Draw(my_image_default)
    draw_image_00 = ImageDraw.Draw(my_image_00)
    draw_image_01 = ImageDraw.Draw(my_image_01)
    draw_image_02 = ImageDraw.Draw(my_image_02)
    draw_image_10 = ImageDraw.Draw(my_image_10)
    draw_image_11 = ImageDraw.Draw(my_image_11)
    draw_image_12 = ImageDraw.Draw(my_image_12)
    draw_image_20 = ImageDraw.Draw(my_image_20)
    draw_image_21 = ImageDraw.Draw(my_image_21)
    draw_image_22 = ImageDraw.Draw(my_image_22)
 
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

    # Generate random array of insects
    s1, s2, insect_number = draw_insects(web_origin)
    for i in range(len(s1)): # For all canvases

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

        # Draw insects using PIL. Circle, start position x, start position y, end position x, end position y, red color.
        draw_image_default.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_00.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_01.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_02.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_10.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_11.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_12.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_20.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_21.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)
        draw_image_22.ellipse([(s1[i], s2[i]), (s1[i]+insect_number/100, s2[i]+insect_number/100)], red, red)

    # Overlay the web onto the canvas in TkInter
    my_canvas_00, draw_image_00, web_length_00 = draw_web(Thread_Data_Points_00, my_canvas_00, draw_image_00, web_origin)
    my_canvas_01, draw_image_01, web_length_01 = draw_web(Thread_Data_Points_01, my_canvas_01, draw_image_01, web_origin)
    my_canvas_02, draw_image_02, web_length_02 = draw_web(Thread_Data_Points_02, my_canvas_02, draw_image_02, web_origin)
    my_canvas_10, draw_image_10, web_length_10 = draw_web(Thread_Data_Points_10, my_canvas_10, draw_image_10, web_origin)
    my_canvas_11, draw_image_11, web_length_11 = draw_web(Thread_Data_Points_11, my_canvas_11, draw_image_11, web_origin)
    my_canvas_12, draw_image_12, web_length_12 = draw_web(Thread_Data_Points_12, my_canvas_12, draw_image_12, web_origin)
    my_canvas_20, draw_image_20, web_length_20 = draw_web(Thread_Data_Points_20, my_canvas_20, draw_image_20, web_origin)
    my_canvas_21, draw_image_21, web_length_21 = draw_web(Thread_Data_Points_21, my_canvas_21, draw_image_21, web_origin)
    my_canvas_22, draw_image_22, web_length_22 = draw_web(Thread_Data_Points_22, my_canvas_22, draw_image_22, web_origin)

    # Display generation number on figure
    my_canvas_00.create_text(0,0, fill='black', font = 'Times 20', anchor = NW, text = 'Generation: %i'%(generation))

    # Store information about all webs in array. Stores lengths, angles of radial threads. Stores potision and true/false of spiral threads. Stores Canvas. Done to easily retrieve bet web at end of fitness
    Thread_Data_Points_Array = [Thread_Data_Points_00, Thread_Data_Points_01, Thread_Data_Points_02, Thread_Data_Points_10, Thread_Data_Points_11, Thread_Data_Points_12, Thread_Data_Points_20, Thread_Data_Points_21, Thread_Data_Points_22]
    Thread_Data_Angles_Array = [Thread_Data_Angles_00, Thread_Data_Angles_01, Thread_Data_Angles_02, Thread_Data_Angles_10, Thread_Data_Angles_11, Thread_Data_Angles_12, Thread_Data_Angles_20, Thread_Data_Angles_21, Thread_Data_Angles_22]
    Thread_Length_Array = [Thread_Length_00, Thread_Length_01, Thread_Length_02, Thread_Length_10, Thread_Length_11, Thread_Length_12, Thread_Length_20, Thread_Length_21, Thread_Length_22]
    Thread_Spiral_Length_Array = [Thread_Spiral_Length_00, Thread_Spiral_Length_01, Thread_Spiral_Length_02, Thread_Spiral_Length_10, Thread_Spiral_Length_11, Thread_Spiral_Length_12, Thread_Spiral_Length_20, Thread_Spiral_Length_21, Thread_Spiral_Length_22]
    Thread_TF_Array = [Thread_TF_00, Thread_TF_01, Thread_TF_02, Thread_TF_10, Thread_TF_11, Thread_TF_12, Thread_TF_20, Thread_TF_21, Thread_TF_22]
    my_canvas_array = [my_canvas_00, my_canvas_01, my_canvas_02, my_canvas_10, my_canvas_11, my_canvas_12, my_canvas_20, my_canvas_21, my_canvas_22]

    # Position of canvases for display to user in TkInter
    my_canvas_array[0].grid(row=0, column=0)
    my_canvas_array[1].grid(row=0, column=1)
    my_canvas_array[2].grid(row=0, column=2)
    my_canvas_array[3].grid(row=1, column=0)
    my_canvas_array[4].grid(row=1, column=1)
    my_canvas_array[5].grid(row=1, column=2)
    my_canvas_array[6].grid(row=2, column=0)
    my_canvas_array[7].grid(row=2, column=1)
    my_canvas_array[8].grid(row=2, column=2)

    # Save the current generation to pictures in file directory
    my_image_default.save('spiderweb_default.png')
    my_image_00.save('spiderweb_00.png')
    my_image_01.save('spiderweb_01.png')
    my_image_02.save('spiderweb_02.png')
    my_image_10.save('spiderweb_10.png')
    my_image_11.save('spiderweb_11.png')
    my_image_12.save('spiderweb_12.png')
    my_image_20.save('spiderweb_20.png')
    my_image_21.save('spiderweb_21.png')
    my_image_22.save('spiderweb_22.png')

    # Display array of canvases
    my_window.update()

    ################################################################################################################################################################
    #FITNESS


    # LENGTH FITNESS
    web_length_array = [web_length_00, web_length_01, web_length_02, web_length_10, web_length_11, web_length_12, web_length_20, web_length_21, web_length_22] # Length of webs evaluated in draw_web
    web_length_fitness = [0]*len(web_length_array) # Initialize array
    web_length_max = max(web_length_array) # Get max amount of silk used
    
    for web in range(len(web_length_array)):
        web_length_fitness[web] = (abs(web_length_array[web]-web_length_max)) # Subtrsact all webs by max. Make positive. So values are relative to each other per generation
    
    web_length_norm_max = max(web_length_fitness) # Get the new max after subtraction

    for web in range(len(web_length_array)):
        web_length_fitness[web] = (1-web_length_fitness[web]/web_length_norm_max) # Normalizes fitness between [0,1], providing the web with least cost the most value

    # INSECT FITNESS

    web_array = [my_image_00, my_image_01, my_image_02, my_image_10, my_image_11, my_image_12, my_image_20, my_image_21, my_image_22] # Information of canvas from PIL
    red_px_array = [0]*len(web_array) # Initialize array
    web_insect_fitness = [0]*len(web_array) # Initialize array
    for web in range(len(web_array)):
        red_px=0 # Starting with 0 red pixels per canvas
        for pixel in list(web_array[web].getdata()): # Get pixel data of canvas
            if pixel == red: # If pixel is red
                red_px += 1 # Increase number of red pixels.
        red_px_array[web]=red_px # Save number of red pixels
    #print(red_px_array)
    red_px_max = max(red_px_array) # Get array with most amount of red pixels
    for web in range(len(red_px_array)):
        red_px_array[web]=(red_px_max-red_px_array[web]) # Subtract from max to find relative difference of red pixels
    #red_px_array[red_px_max_position] = sorted(set(red_px_array))[1] # Arrange array so best is first
    
    red_px_max_diff = max(red_px_array)
    for web in range(len(web_insect_fitness)): 
        web_insect_fitness[web] = red_px_array[web]/red_px_max_diff

    #OVERALL FITNESS
    fitness = [0]*len(web_array) # Initialize fitness array
    for i in range(len(fitness)):
        fitness[i] = (web_length_fitness[i]**0.3+(web_insect_fitness[i])**1.3)/2 # Fitness function as described by Equation 1. n=1, m=0.5
    
    #To Change canvas for user
    fitness_max_position = np.argmax(fitness) # Get position of best web

    # Save properties of best web
    best_canvas = my_canvas_array[fitness_max_position]
    best_Thread_Data_Points = Thread_Data_Points_Array[fitness_max_position]
    best_Thread_Data_Angles = Thread_Data_Angles_Array[fitness_max_position]
    best_Thread_Spiral_Length = Thread_Spiral_Length_Array[fitness_max_position]
    best_Thread_Length = Thread_Length_Array[fitness_max_position]
    best_Thread_TF = Thread_TF_Array[fitness_max_position]

    
    web_array[fitness_max_position].save('best.png')# Save the best web to file directory
    best_canvas.config(background='gray') # Change its background to gray to signify to the user which web is best
    my_canvas_array[fitness_max_position] = best_canvas # Replace best web with one with gray background
    # Position of all webs
    my_canvas_array[0].grid(row=0, column=0)
    my_canvas_array[1].grid(row=0, column=1)
    my_canvas_array[2].grid(row=0, column=2)
    my_canvas_array[3].grid(row=1, column=0)
    my_canvas_array[4].grid(row=1, column=1)
    my_canvas_array[5].grid(row=1, column=2)
    my_canvas_array[6].grid(row=2, column=0)
    my_canvas_array[7].grid(row=2, column=1)
    my_canvas_array[8].grid(row=2, column=2)
    
    
    my_window.update() # Show webs to user
    return best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, generation

#############################################################################################################################################################################
# MAIN SECTION

generation = 0 # Initialize gneration

# CREATE INITIAL WEB

# Set up initial canvas. 300x300 pixels in size.
canvas_width, canvas_height, my_canvas, my_window = canvas_initialization(300) 

#Set up initial web. Dimensions of web, number of radial threads, number of spiral threads per radial thread. 8 radial threads, 20 spiral threads (default)
Thread_Data_Angles, Thread_Data_Points, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin = web_initialization(canvas_width, canvas_height, 8, 20) 

# Create first parent web
my_canvas = draw_web_initial(Thread_Data_Points, my_canvas, web_origin)

# Run function that produces 8 child webs
best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, generation = draw_to_window(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin, generation)

for k in range(498): #Iterate through 798+2 generations (limit)
    my_canvas.delete("all") # Remove old window
    gc.collect() # Clear memory not in use
    # Run function that produces 8 child webs
    best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, generation = draw_to_window(best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, web_origin, generation)

# Final iteration which remains on screen for the user
my_canvas.delete("all") # Remove old window
# Run function that produces 8 child webs
best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, generation = draw_to_window(best_Thread_Data_Points, best_Thread_Data_Angles, best_Thread_Length, best_Thread_Spiral_Length, best_Thread_TF, web_origin, generation)
# Display and keep final result
my_window.mainloop()