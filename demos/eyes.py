#!/usr/bin/pybricks-micropython

# Note that we are using Lego's micropython program (see first line above)

from time import sleep
from pybricks import ev3brick as brick
from pybricks.parameters import Button, ImageFile

# List of images to display
images = [ImageFile.UP, ImageFile.MIDDLE_RIGHT, ImageFile.DOWN, ImageFile.MIDDLE_LEFT]
# How long to sleep after displaying each image
image_delay_secs = 0.5

# Some "constants" to help control our moving through the images list (sadly,
# micropython does not support Enum, which is the "easiest" way to declare
# constants in Python).  This goes to show you that all versions of Python are not
# equal, so just because something *should* work in full-blown Python3 does not mean
# it will work in micropython!!!
COUNTER_CLOCKWISE = -1
PAUSE = 0
CLOCKWISE = 1

# Start off displaying the images in a clockwise fashion
direction = CLOCKWISE

# Keep track of position in images list -- lists in Python start with position/index 0, NOT 1!!!
position = 0

# Clear the display
brick.display.clear()

# Display the images until the user presses the left button
while not Button.LEFT in brick.buttons():
    brick.display.image(images[position])
    sleep(image_delay_secs)

    # If the user presses both the UP and DOWN buttons together, pause.
    # This demonstrates that brick.buttons() really returns a list with
    # all the buttons pressed in it.
    if Button.UP in brick.buttons() and Button.DOWN in brick.buttons():
        direction = PAUSE
    # Else if the user presses just the UP button, go clockwise
    elif Button.UP in brick.buttons():
        direction = CLOCKWISE
    # Else if the user presses just the DOWN button, go counter-clockwise
    elif Button.DOWN in brick.buttons():
        direction = COUNTER_CLOCKWISE

    # Move to the next position in the list
    position = position + direction
    
    # But if we went negative, we need to set the position to the end of the list
    if position < 0:
        position = len(images) - 1
    # Or if we went past the end of the list, we need to set it to the beginning of the list
    elif position >= len(images):
        position = 0