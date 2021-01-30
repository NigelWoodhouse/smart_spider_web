def draw_web_initial(Thread_Data_Points, my_canvas, web_origin):
    # Create Radial Threads
    for i in range(len(Thread_Data_Points[0])):
        my_canvas.create_line(web_origin,Thread_Data_Points[0][i], fill='black', width=2) # Create Radial lines in TkInter

    # Create Frame Threads
    for i in range(len(Thread_Data_Points)): #For Radial threads (default)
        for j in range(len(Thread_Data_Points[1])):
            if j == (len(Thread_Data_Points[0])-1):
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][0], fill='black', width=2) # Connect ends of first and last radial threads
            else:
                my_canvas.create_line(Thread_Data_Points[i][j],Thread_Data_Points[i][j+1], fill='black', width=2) # Connect ends of adjacent radial thread clockwise
    return my_canvas