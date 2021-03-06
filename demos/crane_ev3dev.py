#!/usr/bin/micropython

import os
import sys
from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.wheel import EV3EducationSetTire

# Put our custom libs dir on Python's sys.path
program_base = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.dirname(program_base) + os.sep + 'libs')

# Now we can import our custom libs
from myev3dev2 import MyMoveDifferential

# Should we go for 50 points (push the blocks into the blue circle)
GO_FOR_FIFTY = True

# Our motor constants
ARM_MOTOR_PORT = OUTPUT_A
LEFT_MOTOR_PORT = OUTPUT_B
RIGHT_MOTOR_PORT = OUTPUT_C

# For the standard EV3 build, the wheels are 56mm
# in diameter and the distance between the midpoints of the
# 2 wheels (axle_track) is 114mm.
# Note that we are importing EV3EducationSetTire, which we will use in a little bit
# to set the wheel diameter in mm to be 56 (as well as the wheel width to be
# 28 mm).
AXLE_TRACK_MM = 114

# For the arm motor, we want positive values to be up and negative to be down.
# The way that we're configured, we have to reverse the polarity to achieve this.
arm_motor = MediumMotor(address=ARM_MOTOR_PORT)
arm_motor.polarity = MediumMotor.POLARITY_INVERSED

# Let's initialize our arm motor by putting it all the way down until it
# stalls.  With our build, it will stall when it hits the supporting arms
# for the color sensor and touch sensor (so it doesn't hit the ground - it's
# still slightly in the air.)
arm_motor.off()
arm_motor.on(speed=SpeedPercent(-75))
arm_motor.wait_until_not_moving(timeout=5000)
arm_motor.off()

# Initialize our drive base - MyMoveDifferential extends MoveDifferential, which is a 'tank-like'
# class.  Then drive forward at 25% speed for 24.0 inches.
mdiff = MyMoveDifferential(left_motor_port=LEFT_MOTOR_PORT,
    right_motor_port=RIGHT_MOTOR_PORT, wheel_class=EV3EducationSetTire,
    wheel_distance_mm=AXLE_TRACK_MM)
mdiff.drive_straight_distance_inches(speed=SpeedPercent(25), distance_inches=24.0)

# Raise the arm until we stall, which will hopefully raise the lever
# at the base of the crane.  Notice that we can specify a timeout should the
# motor not stall for whatever reason -- that way, we don't get stuck out on the game board
# and lose a token.
arm_motor.off()
arm_motor.on(speed=SpeedPercent(10))
arm_motor.wait_until_not_moving(timeout=5000)
arm_motor.off()

# Sleep for a little bit while the arm is raised so that the block
# can fall all the way down to rest on the other block.
sleep(1)

# Now lower the arm until we stall
arm_motor.off()
arm_motor.on(speed=SpeedPercent(-75))
arm_motor.wait_until_not_moving(timeout=5000)
arm_motor.off()

if GO_FOR_FIFTY:
    # Drive back a litle bit and curve clockwise - yes, we're calling the counter-clockwise
    # method because things are reversed when we're going backwards
    mdiff.on_arc_left_inches(speed=SpeedPercent(-25), radius_inches=12.0, distance_inches=8.0)

    # Drive back some more and curve counter-clockwise to straighten us out - yes, we're calling
    # the clockwise method because things are reversed when we're going backwards
    mdiff.on_arc_right_inches(speed=SpeedPercent(-25), radius_inches=12.0, distance_inches=8.0)

    # Raise the arm until it stalls to get it out of the way
    arm_motor.off()
    arm_motor.on(speed=SpeedPercent(50))
    arm_motor.wait_until_not_moving(timeout=5000)
    arm_motor.off()
    
    # Drive forward and push the blue blocks into the blue circle
    mdiff.drive_straight_distance_inches(speed=SpeedPercent(25), distance_inches=22.5)

# And go back to home by driving backwards and curving clockwise - again, we're calling the
# counter-clockwise method because things are reversed when we're going backwards
mdiff.on_arc_left_inches(speed=SpeedPercent(-75), radius_inches=18.0, distance_inches=30.0, stop=False)
