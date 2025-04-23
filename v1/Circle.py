# You control a robot that can move and draw on the floor and are given
# a language with the following functions. 
#
# MOVE(distance)
# TURN(degrees)
# DOT
# REPEAT(times) # repetas all actions in the function N times
# basic math operations (+, -, *, and -)
#
# Write a program that draws circles of a given radius. For example,
# one can draw a square as follows:
#
# def LINE(num_dots):
#     MOVE(2)
#     DOT
#     REPEAT(num_dots)
#
# def SQUARE(size):
#    LINE(size)
#    TURN(90)
#    REPEAT(4)

def CIRCLE(radius):
    DOT
    TURN(1)
    MOVE(2 * math.pi * radius / 360)
    REPEAT(360)

# Solution: Divide the circle up in to 360 degrees and draw a dot at
# 'radius' distance away from the center. This can be best achieved
# by not returning to the center of the circle for each dot that's 
# drawn.
