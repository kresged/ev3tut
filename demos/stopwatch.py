#!/usr/bin/pybricks-micropython

# Note that even though we're using Lego's micropython, it is possible to pull in some of the ev3dev2 functionality.
# Just be careful -- not everything plays very well together (especially sound)!!!
from time import sleep
from pybricks import ev3brick as brick
from pybricks.tools import StopWatch
from pybricks.parameters import Button
from ev3dev2.console import Console

# Some "constants" to implement some flow control
STOPPED = 1
RUNNING = 2
FROZEN = 3

# Set up a new stop watch
sw = StopWatch()
sw.pause()
sw.reset()

# Start off in the stopped state
state = STOPPED

# frozen_time holds the time at which we were frozen
frozen_time = 0

# We'll extend Console from ev3dev2.  Note that all of the console fonts are located on the EV3 at:
#  /usr/share/consolefonts
class OurConsole(Console):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def display_time(self, mstime, isFrozen=False):
        (seconds, ms) = divmod(mstime, 1000)
        (hours, seconds) = divmod(seconds, 3600)
        (minutes, seconds) = divmod(seconds, 60)
        if isFrozen:
            self.text_at("(%02d:%02d:%02d.%03d)" % (hours, minutes, seconds, ms), row=5, column=7, alignment='C')
        else:
            self.text_at("%02d:%02d:%02d.%03d" % (hours, minutes, seconds, ms), row=4, column=8, alignment='C')

console = OurConsole(font='Lat15-TerminusBold24x12')
console.reset_console()

while True:
    console.reset_console()
    console.text_at("STOPWATCH", row=1, column=7, alignment='C')

    # If both the UP and DOWN buttons are pressed together, exit the program
    if Button.UP in brick.buttons() and Button.DOWN in brick.buttons():
        # break will exit the while loop
        break
    # Regardless of state, up button will immediately transition us to STOPPED
    elif Button.UP in brick.buttons():
        frozen_time = 0
        sw.pause()
        sw.reset()
        state = STOPPED
    elif state == STOPPED:
        if Button.CENTER in brick.buttons():
            sw.resume()
            state = RUNNING
    elif state == RUNNING:
        if Button.DOWN in brick.buttons():
            sw.pause()
            state = STOPPED
        elif Button.LEFT in brick.buttons():
            frozen_time = sw.time()
            state = FROZEN
    elif state == FROZEN:
        if Button.RIGHT in brick.buttons():
            state = RUNNING

    if state == STOPPED:
        console.text_at("STOP", row=2, column=7, alignment='C')
        console.display_time(sw.time())
    elif state == RUNNING:
        console.text_at("RUN", row=2, column=7, alignment='C')
        console.display_time(sw.time())
    elif state == FROZEN:
        console.text_at("FROZEN", row=2, column=7, alignment='C')
        console.display_time(frozen_time)
        console.display_time(sw.time(), True)

    # Do not loop at a super fast rate - sleep for a little bit.  Saves battery and makes the display smoother.
    sleep(.25)
