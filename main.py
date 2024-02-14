# List of colors in (red,green,blue);
color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214),
              (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172),
              (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124),
              (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119),
              (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), (122, 129, 135)]
"""
Enables users to create Pictures and Shapes 
by providing them with a Virtual Canvas.
"""
import turtle as turtle_module
import random # RGN
turtle_module.colormode(255)
# Create Instance from Turtle;
turtle1 = turtle_module.Turtle()
# Increase the Speed of Moving Turtle;
turtle1.speed("fastest")
# If you move the Turtle in Penup() state it won’t Draw Line;
turtle1.penup()
# Makes the Turtle()--->In-Visible.
#turtle1.hideturtle()
#####################
turtle1.setheading(225)#Angle of Moving.
turtle1.forward(300)#Move.
turtle1.setheading(0)
#####################
number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    turtle1.dot(20, random.choice(color_list))
    turtle1.forward(50)
    if dot_count % 10 == 0: # The Remainder of Division == 0;
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)
# Screen-of-Turtle;
screen = turtle_module.Screen()
screen.exitonclick()
###############################
#Learning programmer as go to GYM.
################################
