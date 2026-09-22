import os
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen_width = 1500  # can be changed, the bars will automatically change in size based on this (minimum of 150)
screen_height = 1400 # can be changed, the bars will automatically change in size based on this (minumum of 150)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("sorter")

values = []
index_values = []
chosen_value = 0
chosen_index = 0
rgb = 0
operations = 0
time = 0


#           """CONFIG"""
max_value = 100 # the max value a part can have, influenced the height
max_numbers = 100 # the maximum amoount of parts
same_numer = False # can be True or False if True parts with the same value can be generated
smart_mode = False # when using smart mode the code will use a smarter method to sort the list
super_smart_mode = True # better than smart_mode don't use True for both



if not same_numer:
    if max_numbers > max_value:
        max_value = max_numbers

indices = []
while len(values) < max_numbers:
    if same_numer:
        for i in range(1, max_numbers):
            value = random.randint(1, max_value)
            if value < 1:
                value = 1
            values.append(value)
    else:
        for i in range(1, max_numbers + 1):
            value = i
            value += 1
            values.append(value)
        random.shuffle(values)


if smart_mode:
    if super_smart_mode:
        super_smart_mode = False
if smart_mode:
    chosen_index = len(values) - 1
if super_smart_mode:
    chosen_index = 1
    end_index = len(values) - 1


for i in range(len(values)):
    idx = i
    indices.append(idx)
for indice in indices:
    value = values[indice]
    print(f"index: {indice} has value {value}")

running = True
while running:
    #clock_value = 6000 # can be changed. the higher the number the faster the simulation goes (this is a maximum number, so the real speed depends on your system)
    #clock.tick(clock_value)
    screen.fill((255, 255, 255))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB equation
    for indice in indices:
        value = values[indice]
        if value >= max_value / 2:
            offset = value - (max_value / 2)
            A = max_value / 2
            B = 255 / A
            rgbG = offset * B
            rgbB = 0

            rgbR = 255 * (max_value - value) / (max_value / 2 - 1)
        else:
            rgbB = 255 * (max_value / 2 - value * 2) / (max_value / 2 - 1)
            rgbG = 0
            offset = value
            A = max_value / 2
            B = 255 / A
            rgbR = offset * B
        if rgbR > 255:
            rgbR = 255
        elif rgbR < 0:
            rgbR = 0
        if rgbG > 255:
            rgbG = 255
        elif rgbG < 0:
            rgbG = 0
        if rgbB > 255:
            rgbB = 255
        elif rgbB < 0:
            rgbB = 0
        rgb = (rgbR, rgbG, rgbB)

        # makes the bars change size and coordinates depending on the size of the screen
        height_changer = (screen_height - 100) / max_value
        height = (value * height_changer)

        # stops rounding gaps
        x_start = round(20 + (indice * (screen_width - 40) / max_numbers))
        x_end = round(20 + ((indice + 1) * (screen_width - 40) / max_numbers))
        width = x_end - x_start

        # draws the lines
        pygame.draw.rect(screen, rgb, (x_start, int((screen_height - 50) - height), width, int(height)))

    pygame.display.flip()

    steps_per_frame = 2000

    for _ in range(steps_per_frame):

        # sorting algorithm
        if not smart_mode and not super_smart_mode:
            chosen_index = random.randint(1, len(values) - 1)
            chosen_index_left = chosen_index - 1

            if values[chosen_index] < values[chosen_index_left]:
                values[chosen_index], values[chosen_index_left] = values[chosen_index_left], values[chosen_index]
                operations += 1

        elif smart_mode:
            if chosen_index > 0:
                chosen_index_left = chosen_index - 1

                if values[chosen_index] < values[chosen_index_left]:
                    values[chosen_index], values[chosen_index_left] = values[chosen_index_left], values[chosen_index]
                    operations += 1

                chosen_index -= 1

            else:
                chosen_index = len(values) - 1

        elif super_smart_mode:
            chosen_index_left = chosen_index - 1

            if values[chosen_index] < values[chosen_index_left]:
                values[chosen_index], values[chosen_index_left] = values[chosen_index_left], values[chosen_index]
                operations += 1

            chosen_index += 1

            if chosen_index > end_index:
                end_index -= 1
                chosen_index = 1

            if end_index <= 0:
                break







with open("operations.txt", "w") as file:
    file.write(str(operations))
print(operations)

pygame.quit()


