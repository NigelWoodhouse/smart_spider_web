#Import libraries
from math import cos
from math import sin
from math import pi
import random

# Governing update function
def update(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, canvas_height, canvas_width):
    Thread_TF = spiral_thread_TF(Thread_TF) # Update spiral threads true or false
    Thread_Data_Angles = change_angle(Thread_Data_Angles) # Update radial angle
    Thread_Data_Points, Thread_Length = change_length(Thread_Data_Points, Thread_Data_Angles, Thread_Length, canvas_height, canvas_width)# Update radial length
    Thread_Data_Points, Thread_Spiral_Length = change_spiral_thread_length(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, canvas_height, canvas_width) # Update spiral position
    return Thread_Data_Points

# Mutate radial angle
def change_angle(Thread_Data_Angles):
    for i in range(len(Thread_Data_Angles)):
        Thread_Data_Angles[i] = Thread_Data_Angles[i]+random.uniform(-0.2,0.2) # mutate an
        if Thread_Data_Angles[i] > 2*pi: # If greater than 2pi, set angle to 2 pi. Maintains order of radial threads.
            Thread_Data_Angles[i] = 2*pi
        elif Thread_Data_Angles[i] < 0: # If less than 0, set angle to 0. Maintains order of radial threads.
            Thread_Data_Angles[i] = 0
        else:
            pass
    Thread_Data_Angles.sort() # Sort angles incase order changes
    return Thread_Data_Angles

# Mutate radial thread lengths
def change_length(Thread_Data_Points, Thread_Data_Angles, Thread_Length, canvas_height, canvas_width):
    for i in range(len(Thread_Data_Points[0])): # For radial threads
            Thread_Length[i] = Thread_Length[i]+random.uniform(-10,10) # Change length by 10 pixels
            if Thread_Length[i] > canvas_height/2: # If greater than half height of canvas, set to half heigth of canvas
                Thread_Length[i] = canvas_height/2
            elif Thread_Length[i] < 0: # If less than 0 length (not valid), set to min of 5 pixels
                Thread_Length[i] = 5
            else:
                pass
            Thread_Coordinates = ((Thread_Length[i]*cos(Thread_Data_Angles[i])+canvas_width/2), (Thread_Length[i]*sin(Thread_Data_Angles[i])+canvas_height/2)) # Update positions of end of radial threads
            Thread_Data_Points[0][i] = Thread_Coordinates # Save coordinates
    return Thread_Data_Points, Thread_Length

# Mutate turning on and off spiral threads
def spiral_thread_TF(Thread_TF):
    for i in range(1,len(Thread_TF)):
        for j in range(len(Thread_TF[1])):
            if Thread_TF[i][j] == True: # If web is true
                r = random.random()
                remove_spiral_thread_threshold = 0.5 # 50% chance of being turned off
                if (r < remove_spiral_thread_threshold) and (i >= 1): # Frame thread cannot be truend off
                    Thread_TF[i][j] = False # Make false
            else: # false
                r = random.random()
                add_spiral_thread_threshold = 0.5 # 50% chance to change to true to make new spiral thread
                if r > add_spiral_thread_threshold: 
                    Thread_TF[i][j] = True # Make true
    return Thread_TF

# Update position of spiral thread along radial thread
def change_spiral_thread_length(Thread_Data_Points, Thread_Data_Angles, Thread_Length, Thread_Spiral_Length, Thread_TF, canvas_height, canvas_width):
    for i in range(1,len(Thread_Spiral_Length)):# For spiral thread
        for j in range(len(Thread_Spiral_Length[0])): # For radial thread
            if Thread_TF[i][j] == True:
                Thread_Spiral_Length[i][j] += random.uniform(-0.2,0.2) # adjust length along unit vector
                Thread_Spiral_Length[i][j] = abs(Thread_Spiral_Length[i][j])
                if Thread_Spiral_Length[i][j] >=1: # Max length along unit vector is 1
                    Thread_Spiral_Length[i][j] = 0.99 # Cannot exceed frame thread.
                if Thread_Spiral_Length[i][j] <=0: # Max length along unit vector is 1
                    Thread_Spiral_Length[i][j] = 0.01 # Cannot exceed frame thread.

                if Thread_Spiral_Length[i][j] > Thread_Spiral_Length[i-1][j]: # Organize threads to attempt to reduce spiral threads crossing. Will not remove all corssing.
                    Thread_Spiral_Length[i][j], Thread_Spiral_Length[i-1][j] = Thread_Spiral_Length[i-1][j], Thread_Spiral_Length[i][j]

            Thread_Data_Points[i][j] = ((Thread_Length[j]*Thread_Spiral_Length[i][j]*cos(Thread_Data_Angles[j])+canvas_width/2), (Thread_Length[j]*Thread_Spiral_Length[i][j]*sin(Thread_Data_Angles[j])+canvas_height/2)) #Update position of spiral thread
    return Thread_Data_Points, Thread_Spiral_Length