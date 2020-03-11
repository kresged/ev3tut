#!/usr/bin/pybricks-micropython

import os
import sys

from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Put our custom libs dir on Python's sys.path
program_base = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.dirname(program_base) + os.sep + 'libs')

# Now we can import our custom libs
from mypybricks import MyDriveBase
from myutils import debug_print

# See page 38 of the Lego EV3 MicroPython Getting Started Guide for documentation
# on the DriveBase class.  In our libs directory, you will find a mypybricks.py
# module that contains an "extension" to the DriveBase class named
# MyDriveBase.  The normal DriveBase class contains a drive_time method (see page 39 of the guide).
# I hacked up a drive_distance method in MyDriveBase that allows us to drive for a given
# distance in inches at a given speed in inches/sec (I think in inches, not in mm); under the hood,
# it uses drive_time (but does all the math for us).

# Our motor constants - the port letters correspond to the letters printed on the EV3
LEFT_MOTOR_PORT = Port.B
RIGHT_MOTOR_PORT = Port.C

# Our gyro constant - note that port S2 corresponds to port 2 on the EV3
GYRO_PORT = Port.S2

# The DriveBase class needs to know what the diameter of the wheels are as well as the distance
# between the midpoints of the 2 wheels (axle_track).  I'm testing with the standard EV3 build - if
# you don't have this as your build, you'd need to adjust these numbers accordingly.  Check out
# the Lego Wheels Chart at http://wheels.sariel.pl/ for the diameters of lots of different wheels.
WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 114

# Initialize our drive motors
left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)

# Initialize our gyro sensor
gyro_sensor = GyroSensor(GYRO_PORT)

# Initialize our drive base
robot = MyDriveBase(left_motor=left_motor, right_motor=right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM, axle_track=AXLE_TRACK_MM)

turn_drift = 0

TARGET_TURN_DEGREES = 90

for i in range(8):
    gyro_sensor.reset_angle(0)
    wait(250)
    robot.drive_distance(inches=12.0, speed=4.0, steering=0)
    wait(250)
    line_drift = gyro_sensor.angle()
    gyro_sensor.reset_angle(0)
    wait(250)
    drift = line_drift + turn_drift
    target_turn = TARGET_TURN_DEGREES - drift
    if i == 0:
        debug_print("Straight line {} drift {} target_turn {}".format(i, line_drift, target_turn))
    else:
        debug_print("Straight line {} drift {} previous turn drift {} target_turn {}".format(i, line_drift, turn_drift, target_turn))
    robot.drive(speed=0.0, steering=45)
    while abs(gyro_sensor.angle()) < target_turn:
        pass
    robot.stop(Stop.BRAKE)
    wait(250)
    after_turn_reading = gyro_sensor.angle()
    turn_drift = after_turn_reading - target_turn
    debug_print("Turn {} final gyro {} target {} turn drift {}".format(i, after_turn_reading, target_turn, turn_drift))
