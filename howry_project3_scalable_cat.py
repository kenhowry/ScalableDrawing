"""
Creating a Scalable Drawing

File Name: howry_project3_scalable_cat.py
Author: Ken Howry
Date: 22.9.26
Course: COMP 1351
Assignment: Project III
Collaborators: N/A
Internet Source: N/A
"""

import dudraw

def edward_the_cat(x_position, y_position, x_scale, y_scale)->None:
    """
    Draws a cat with a bowler hat scaled and translated

    parameters: 
        x_position: float - translates the shape's x-cooridnate to x_location
        y_position: float - translates the shape's y-coordinate y_location 
        x_scale: float - a x-scale factor 
        y_scale: float - a y-scale factor
    output: none
    """
    
    #right_ear
    dudraw.set_pen_color_rgb(79, 78, 76)
    dudraw.filled_triangle(0.7 * x_scale + x_position, 0.6 * y_scale + y_position, 0.65 * x_scale + x_position, 0.8 * y_scale + y_position, 0.6 * x_scale + x_position, 0.7 * y_scale + y_position)

    #left_ear
    dudraw.set_pen_color_rgb(199, 214, 213)
    dudraw.filled_triangle(0.3 * x_scale + x_position, 0.6 * y_scale + y_position, 0.35 * x_scale + x_position, 0.8 * y_scale + y_position, 0.4 * x_scale + x_position, 0.7 * y_scale + y_position)


    #head
    dudraw.filled_ellipse(0.5 * x_scale + x_position, 0.5 * y_scale + y_position, 0.25 * x_scale, 0.25 * y_scale)

    #right_eye
    dudraw.set_pen_color_rgb(25, 255, 221)
    dudraw.filled_ellipse(0.62 * x_scale + x_position, 0.55  * y_scale + y_position, 0.025 * x_scale, 0.05 * y_scale)

    #eye_spot
    dudraw.set_pen_color_rgb(79, 78, 76)
    dudraw.filled_ellipse(0.375 * x_scale + x_position, 0.55  * y_scale + y_position, .08 * x_scale, .08 * y_scale)

    #left_eye
    dudraw.set_pen_color_rgb(255, 244, 25)
    dudraw.filled_ellipse(0.375 * x_scale + x_position, 0.55 * y_scale + y_position, 0.025 * x_scale, 0.05 * y_scale)

    #nose
    dudraw.set_pen_color_rgb(250, 196, 255)
    dudraw.filled_triangle(0.45 * x_scale + x_position, 0.45 * y_scale + y_position, 0.5 * x_scale + x_position, 0.40 * y_scale + y_position, 0.55 * x_scale + x_position, 0.45 * y_scale + y_position)

    #left_whiskers
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.line(0.3 * x_scale + x_position, 0.475 * y_scale + y_position, 0.375 * x_scale + x_position, 0.45 * y_scale + y_position)
    dudraw.line(0.3 * x_scale + x_position, 0.425 * y_scale + y_position, 0.375 * x_scale + x_position, 0.425 * y_scale + y_position)
    dudraw.line(0.3 * x_scale + x_position, 0.375 * y_scale + y_position, 0.375 * x_scale + x_position, 0.4 * y_scale + y_position)

    #right_whiskers
    dudraw.line(0.7 * x_scale + x_position, 0.475 * y_scale + y_position, 0.625 * x_scale + x_position, 0.45 * y_scale + y_position)
    dudraw.line(0.7 * x_scale + x_position, 0.425 * y_scale + y_position, 0.625 * x_scale + x_position, 0.425 * y_scale + y_position)
    dudraw.line(0.7 * x_scale + x_position, 0.375 * y_scale + y_position, 0.625 * x_scale + x_position, 0.4 * y_scale + y_position)


    #bowler_hat
    #top of the bowler hat
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.filled_ellipse(0.5 * x_scale + x_position, 0.75 * y_scale + y_position, .06 * x_scale, .04 * y_scale)

    #hat_stripe
    dudraw.set_pen_color(dudraw.BOOK_RED)
    dudraw.filled_rectangle(0.5 * x_scale + x_position, 0.75 * y_scale + y_position, 0.06 * x_scale, 0.01 * y_scale)

    #hat_bottom
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.filled_rectangle(0.5 * x_scale + x_position, 0.72 * y_scale + y_position, 0.08 * x_scale, 0.015 * y_scale)

    #body
    #base of body
    dudraw.set_pen_color_rgb(199, 214, 213)
    dudraw.filled_ellipse(0.5 * x_scale + x_position, 0.15  * y_scale + y_position, 0.25 * x_scale, 0.25 * y_scale)

    #white_part of body
    dudraw.set_pen_color_rgb(255, 255, 255)
    dudraw.filled_ellipse(0.5 * x_scale + x_position, 0.075  * y_scale + y_position, 0.18 * x_scale, 0.18 * y_scale)


#program
dudraw.set_canvas_size(200, 200);
dudraw.clear(dudraw.BOOK_LIGHT_BLUE);
edward_the_cat(0, 0, 1, 1);
dudraw.show(float('inf'))