from ev3dev2.motor import MoveDifferential

class MyMoveDifferential(MoveDifferential):
    """
    Class that will extend MoveDifferential with a few more methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Just invoke our parent's initializer, passing all passed arguments to it
        """
        super().__init__(*args, **kwargs)

    def drive_straight_distance_inches(self, speed, distance_inches, stop=True):
        """
        Drive a given distance in a straight line at a given speed
        """
        distance_mm = self.inches_to_mm(distance_inches)
        self.on_for_distance(speed=speed, distance_mm=distance_mm, brake=stop)

    def on_arc_left_inches(self, speed, radius_inches, distance_inches, stop=True):
        """
        Drive counter-clockwise in a circle of a given radius for a given distance
        """
        radius_mm = self.inches_to_mm(radius_inches)
        distance_mm = self.inches_to_mm(distance_inches)
        self.on_arc_left(speed=speed, radius_mm=radius_mm, distance_mm=distance_mm, brake=stop)

    def on_arc_right_inches(self, speed, radius_inches, distance_inches, stop=True):
        """
        Drive clockwise in a circle of a given radius for a given distance
        """
        radius_mm = self.inches_to_mm(radius_inches)
        distance_mm = self.inches_to_mm(distance_inches)
        self.on_arc_right(speed=speed, radius_mm=radius_mm, distance_mm=distance_mm, brake=stop)

    def inches_to_mm(self, inches):
        """
        Convert inches to mm
        """
        return inches*25.4
