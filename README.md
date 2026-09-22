# Sorting Algorithm viszualizer

This project is a sorting algorithm visualizer made with Python and Pygame.

The program generates a list of values, displays them as vertical bars, and sorts them while the process is shown on screen. The height of each bar represents its value, while the colour changes depending on how large the value is.

The main goal of this project was to better understand how sorting algorithms work by building one manually instead of using Python's built-in sorting functions.

## Features

* Visual representation of values using bars
* Dynamic bar height based on the value
* RGB colour gradient based on the value
* Randomized starting order
* Multiple sorting modes
* Adjustable simulation speed
* Configurable amount of values
* Configurable maximum value
* Optional duplicate values
* Operation counter for comparing sorting performance

## Requirements

You need Python installed on your system.

The project also uses Pygame.

Install Pygame with:

```bash
pip install pygame
```

## Configuration

The main settings can be changed near the top of the Python file.

Example:

```python
max_value = 100
max_numbers = 100
same_number = False
smart_mode = False
super_smart_mode = True
steps_per_frame = 50

max_value     Is the maximum value a bar can have.
max_numbers     Is the amount of bars generated.
same_number     Can be True or False. if True then the list is alowed to generate multiple bars with the same value.
smart_mode     If False then the program will randomly take a bar --> compares it to its neigbour and if smaller will switch the places of the bars.
smar_mode     If True then the program will run from the right to the left by comparing to it's neightbour and if nececary move to the left. This results in the program beings solver faster and always from left to right
super_smart_mode     If True then the program will skip bars that are already sorted resulting in an even faster result
steps_per_frame     The higher the number the more sorting steps it does before refreshing the screen, with lower values you want this low and with higher values you want this high, since vizualising the bar costs time
```

## Sorting

Instead of using:

values.sort()

or:

sorted(values)

the program sorts the values manually.

Two neighbouring values are compared:

if values[chosen_index] < values[chosen_index_left]:

If they are in the wrong order, their positions are swapped:

values[chosen_index], values[chosen_index_left] = \
    values[chosen_index_left], values[chosen_index]

By repeating this process many times, the list gradually becomes sorted.


## License

This project is intended for learning and experimentation.
