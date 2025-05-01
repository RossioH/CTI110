# P4LAB1
# 3/19/2025
# Heather Rossio
# Turtle Graphics - Draw Square and Triangle

import turtle 
win = turtle.Screen()
timmy = turtle.Turtle()
win.bgcolor('purple')

# set the way timmy looks 
timmy.pensize(6)
timmy.pencolor('green')
timmy.shape('arrow')

# looks like move foward is pixals 

# fir loop that runs 4 times

for i in range(4):
    timmy.forward(100)
    timmy.right(90)

# while loop that runs 3 times

this_run = 0

while this_run < 3:
    timmy.forward(100)
    timmy.left(120)
    this_run += 1

# keeps window open after shape is drawn 
win.mainloop()