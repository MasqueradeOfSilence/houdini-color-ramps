import numpy as np


def build_individual_color(color_position1, color_position2, num_desired_points,
                           color1, color2):
    print("Building an individual color for the ramp")
    distance1 = color_position2 - color_position1
    # distance2 = color_position3 - color_position2
    # distance3 = color_position4 - color_position3
    num_points_between_2_1 = distance1 * num_desired_points
    # num_points_between_3_2 = distance2 * num_desired_points
    # num_points_between_4_3 = distance3 * num_desired_points
    step_size_red = (color2[0] - color1[0]) / num_points_between_2_1
    step_size_green = (color2[1] - color1[1]) / num_points_between_2_1
    step_size_blue = (color2[2] - color1[2]) / num_points_between_2_1

    num_iterations = 0
    current_color_ramp = [color1]
    prev_red = color1[0]
    prev_green = color1[1]
    prev_blue = color1[2]
    while num_iterations < num_points_between_2_1:
        new_red = prev_red + step_size_red
        new_green = prev_green + step_size_green
        new_blue = prev_blue + step_size_blue
        prev_red = new_red
        prev_green = new_green
        prev_blue = new_blue
        if new_red > 1 or new_green > 1 or new_blue > 1:
            break
        current_color_ramp.append([new_red, new_green, new_blue])
        num_iterations += 1
    current_color_ramp.append(color2)
    print("The other color ramp: " + str(color_ramp))
    return color_ramp


def build_color_ramp(color_position1, color_position2, color_position3, color_position4, num_desired_points, color1,
                     color2, color3, color4):
    print("Building a color ramp")
    color1 = build_individual_color(color_position1, color_position2, num_desired_points, color1, color2)


print("Hello Houdini color ramps!")
# Color ramp: Standard fire.
# We put the RGB values, and how far apart they are.
black = [0, 0, 0]
orange = [1, 0.432, 0]
yellow = [1, 0.8833, 0]
white = [1, 1, 1]
black_position = 0
orange_position = 0.54
yellow_position = 0.893
white_position = 1
# We desire 96 points because we already have 4, and want 100 total.
desired_points = 96
# determine distances
distance_orange_to_black = orange_position - black_position
distance_yellow_to_orange = yellow_position - orange_position
distance_white_to_yellow = white_position - yellow_position
print("Orange to black distance: " + str(distance_orange_to_black))
print("Yellow to orange distance: " + str(distance_yellow_to_orange))
print("White to yellow distance: " + str(distance_white_to_yellow))
# determine what percent each distance is
num_points_between_orange_and_black = distance_orange_to_black * desired_points
num_points_between_yellow_and_orange = distance_yellow_to_orange * desired_points
num_points_between_white_and_yellow = distance_white_to_yellow * desired_points
print("Orange to black points: " + str(num_points_between_orange_and_black))
print("Yellow to orange points: " + str(num_points_between_yellow_and_orange))
print("White to yellow points: " + str(num_points_between_white_and_yellow))
# Compute the distance between each point for r, g, and b
black_to_orange_step_size_red = (orange[0] - black[0]) / num_points_between_orange_and_black
black_to_orange_step_size_green = (orange[1] - black[1]) / num_points_between_orange_and_black
black_to_orange_step_size_blue = (orange[2] - black[2]) / num_points_between_orange_and_black
print("Black to orange step size red: " + str(black_to_orange_step_size_red))
print("Black to orange step size green: " + str(black_to_orange_step_size_green))
print("Black to orange step size blue: " + str(black_to_orange_step_size_blue))
# Next, increment the values
num_iterations = 0
color_ramp = [black]
prev_red = black[0]
prev_green = black[1]
prev_blue = black[2]
while num_iterations < num_points_between_orange_and_black:
    new_red = prev_red + black_to_orange_step_size_red
    new_green = prev_green + black_to_orange_step_size_green
    new_blue = prev_blue + black_to_orange_step_size_blue
    prev_red = new_red
    prev_green = new_green
    prev_blue = new_blue
    if new_red > 1 or new_green > 1 or new_blue > 1:
        break
    color_ramp.append([new_red, new_green, new_blue])
    num_iterations += 1
color_ramp.append(orange)
print("Done adding orange to black points")
print("That color ramp: " + str(color_ramp))
# Now we need to do it for yellow to orange
yellow_to_orange_step_size_red = (yellow[0] - orange[0]) / num_points_between_yellow_and_orange
# ok I bet if I clean this up it'll be way easier. let's take a break, then switch gears
# TESTING FOR VALIDITY:
build_color_ramp(black_position, orange_position, yellow_position, white_position, desired_points, black, orange,
                 yellow, white)
