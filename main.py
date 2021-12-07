import numpy as np
from PIL import Image as img


def build_individual_color(color_position1, color_position2, num_desired_points,
                           color1, color2):
    print("Building an individual color for the ramp")
    distance1 = color_position2 - color_position1
    num_points_between_2_1 = distance1 * num_desired_points
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


def build_fire_standard_color():
    black = [0, 0, 0]
    orange = [1, 0.432, 0]
    yellow = [1, 0.8833, 0]
    white = [1, 1, 1]
    black_position = 0
    orange_position = 0.54
    yellow_position = 0.893
    white_position = 1
    # We desire 96 points because we already have 4, and want approximately 100 total.
    desired_points = 96
    ramp = build_color_ramp(black_position, orange_position, yellow_position, white_position, desired_points, black,
                            orange, yellow, white)
    print("ramp: " + str(ramp))
    np_ramp = np.array(ramp)
    np_ramp = (np_ramp * 255).astype(np.uint8)
    np_ramp = np.repeat(np_ramp[None, ...], 3, axis=0)
    print("adjusted final ramp RED: " + str(np_ramp))
    print("shape: " + str(np_ramp.shape))
    data = img.fromarray(np_ramp, "RGB")
    data.save("ramp.png")


def build_fire_blue():
    black = [0, 0, 0]
    blue = [0, 0, 1]
    sky_blue = [0, 1, 1]
    white = [1, 1, 1]
    black_position = 0
    blue_position = 0.54
    sky_blue_position = 0.893
    white_position = 1
    desired_points = 96
    ramp = build_color_ramp(black_position, blue_position, sky_blue_position, white_position, desired_points, black,
                            blue, sky_blue, white)
    print("ramp: " + str(ramp))
    np_ramp = np.array(ramp)
    np_ramp = (np_ramp * 255).astype(np.uint8)
    np_ramp = np.repeat(np_ramp[None, ...], 3, axis=0)
    print("adjusted final ramp BLUE: " + str(np_ramp))
    print("shape: " + str(np_ramp.shape))
    data = img.fromarray(np_ramp, "RGB")
    data.save("ramp_blue.png")


def build_fire_green():
    black = [0, 0, 0]
    green = [0, 0.5, 0]
    light_green = [0, 1, 0]
    white = [1, 1, 1]
    black_position = 0
    green_position = 0.518797
    light_green_position = 0.77821
    white_position = 1
    desired_points = 96
    ramp = build_color_ramp(black_position, green_position, light_green_position, white_position, desired_points, black,
                            green, light_green, white)
    print("ramp: " + str(ramp))
    np_ramp = np.array(ramp)
    np_ramp = (np_ramp * 255).astype(np.uint8)
    np_ramp = np.repeat(np_ramp[None, ...], 3, axis=0)
    print("adjusted final ramp GREEN: " + str(np_ramp))
    print("shape: " + str(np_ramp.shape))
    data = img.fromarray(np_ramp, "RGB")
    data.save("ramp_green.png")


def build_fire_pink():
    black = [0, 0, 0]
    dark_pink = [0.5, 0, 0.25]
    pink = [1, 0, 0.5]
    white = [1, 1, 1]
    black_position = 0
    dark_pink_position = 0.518797
    pink_position = 0.77821
    white_position = 1
    desired_points = 96
    ramp = build_color_ramp(black_position, dark_pink_position, pink_position, white_position, desired_points, black,
                            dark_pink, pink, white)
    print("ramp: " + str(ramp))
    np_ramp = np.array(ramp)
    np_ramp = (np_ramp * 255).astype(np.uint8)
    np_ramp = np.repeat(np_ramp[None, ...], 3, axis=0)
    print("adjusted final ramp PINK: " + str(np_ramp))
    print("shape: " + str(np_ramp.shape))
    data = img.fromarray(np_ramp, "RGB")
    data.save("ramp_pink.png")


print("Computing Houdini color ramps!")
build_fire_standard_color()
build_fire_blue()
build_fire_green()
build_fire_pink()
