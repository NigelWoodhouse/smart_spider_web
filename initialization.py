# Import libraries
from tkinter import *
from math import cos
from math import sin
from math import pi
from math import degrees
import random
import numpy as np

# For initial canvas creation
def canvas_initialization(canvas_width=300):
    #Canvas dimensions
    canvas_width = 300
    canvas_height = canvas_width

    # Create TkInter window
    my_window = Tk()
    # Title of window
    my_window.title('Spider Web Optimization - Nigel Woodhouse. Created December 23 2019')
    # Default canvas for parent web
    my_canvas = Canvas(my_window, width = canvas_width, height = canvas_height, background = 'white')

    return canvas_width, canvas_height, my_canvas, my_window

# Creaete initial parent web
def web_initialization(canvas_width, canvas_height, Radial_Thread_Number=8, Spiral_Thread_Number = 20):
    # Center of canvas
    web_origin = (canvas_width/2, canvas_height/2)

    # Array of radial threads
    Thread_Data_Angles = [0]*Radial_Thread_Number
    Thread_Length = [0]*Radial_Thread_Number # Array to hold length of radial threads
    Thread_Spiral_Length = [[0] * Radial_Thread_Number for i in range(Spiral_Thread_Number)] # Array of radial threads
    for i in range(Radial_Thread_Number):
        Thread_Spiral_Length[0][i]=1 # Establishing frame threads at end of radial threads

    Thread_Data_Points = [[web_origin] * Radial_Thread_Number for i in range(Spiral_Thread_Number)] # Array fro spiral threads. All spiral threads begin at origin
    Thread_TF = [[False] * Radial_Thread_Number for i in range(Spiral_Thread_Number)] # Set all spiral threads off
    for i in range(Radial_Thread_Number):
        Thread_TF[0][i]=True # Set these ones to true, for they are fram threads

    # Set initial angle
    for i in range(len(Thread_Data_Angles)):
        Thread_Angle = random.uniform(0, 2*pi) # Between 0 and 2pi
        Thread_Data_Angles[i] = Thread_Angle # Set angle
    Thread_Data_Angles.sort() # Sort to keep order

    # set initial length of radial threads
    for i in range(len(Thread_Data_Points[0])):
        Thread_Length[i] = random.uniform(50,100) # Initial length in pixels
        Thread_Coordinates = ((Thread_Length[i]*cos(Thread_Data_Angles[i])+canvas_width/2), (Thread_Length[i]*sin(Thread_Data_Angles[i])+canvas_height/2))# Get position of spiral thread thread
        Thread_Data_Points[0][i] = Thread_Coordinates # Save position of sprial thread
    return Thread_Data_Angles, Thread_Data_Points, Thread_Length, Thread_Spiral_Length, Thread_TF, web_origin