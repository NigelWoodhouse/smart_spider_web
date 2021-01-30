from math import fsum
import random
def draw_insects(web_origin):
    # Create Radial Threads
    insect_number = fsum(web_origin) # Number of insect proportional to size of canvas
    s1 = [] # x position
    s2 = [] # y position
    for i in range(int(insect_number)):
        # Generate random x and y positions
        r1 = random.uniform(0,insect_number-insect_number/100)
        r2 = random.uniform(0,insect_number-insect_number/100)
        # Append positions to array
        s1.append(r1)
        s2.append(r2)

    return s1, s2, insect_number