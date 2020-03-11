from pybricks.parameters import Stop
from pybricks.robotics import DriveBase

class MyDriveBase(DriveBase):
    """
    Class that will extend DriveBase with a few more methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Just invoke our parent's initializer, passing all passed arguments to it
        """
        super().__init__(*args, **kwargs)

    def drive_time_inches(self, speed, steering, time, stop=Stop.BRAKE):
        """
        Drive at the specified speed and turnrate for a given amount of time, and then stop.

        Parameters
        ----------
        speed : float – Forward speed of the robot (inches/s).
        steering : float – Turn rate of the robot (deg/s).
        time : int – Duration of the maneuver (ms).
        stop : stopping type
        stopping type (defaults to Stop.BRAKE)
        """
        speed_mm_per_sec = self.inches_to_mm(speed)
        self.drive_time(speed=speed_mm_per_sec, steering=steering, time=time)
        self.stop(stop)

    def drive_distance(self, inches, speed, steering, stop=Stop.BRAKE):
        """
        Drive a given distance in inches at a given speed with steering

        Parameters
        ----------
        inches : float
        number of inches to move
        speed : float
        forward speed of the robot in inches/sec
        steering : float
        turn rate of the robot in deg/sec
        stop : stopping type
        stopping type (defaults to Stop.BRAKE)
        """
        distance_mm = self.inches_to_mm(inches)
        speed_mm_per_sec = self.inches_to_mm(speed)
        if speed_mm_per_sec != 0:
            self.drive_time(speed=speed_mm_per_sec, steering=steering, time=abs(distance_mm/speed_mm_per_sec)*1000)
        self.stop(stop)

    def inches_to_mm(self, inches):
        """
        Convert inches to mm
        """
        return inches*25.4
