import numpy as np
import cv2


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
    print("Created color ramp: " + str(current_color_ramp))
    return current_color_ramp


def build_color_ramp(color_position1, color_position2, color_position3, color_position4, num_desired_points, color1,
                     color2, color3, color4):
    print("Building a color ramp")
    final_ramp = build_individual_color(color_position1, color_position2, num_desired_points, color1, color2)
    final_ramp += build_individual_color(color_position2, color_position3, num_desired_points, color2, color3)
    final_ramp += build_individual_color(color_position3, color_position4, num_desired_points, color3, color4)
    return final_ramp


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
ramp = build_color_ramp(black_position, orange_position, yellow_position, white_position, desired_points, black, orange,
                        yellow, white)
print("Final ramp: " + str(ramp))
np_ramp = np.array(ramp)
np_ramp = np_ramp * 255
# print("Scaled up: " + str(np_ramp))
cv2.imwrite("ramp.png", np_ramp)
