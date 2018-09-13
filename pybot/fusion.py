""" Sensor fusion for circuitpython.
based on the MicroPython library by Peter Hinch.
https://github.com/micropython-IMU/micropython-fusion/blob/master/fusion.py

tested on adafruit feather M0 express.
"""

__author__ = "Geoff Goldrick"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "geoff.goldrick@gmail.com"
__status__ = "Prototype"


import time
from math import sqrt, atan2, asin, degrees, radians


#define the functions and classes
class Fusion:
    """provides sensor fusion allowing heading, pitch and roll to be extracted.
    This uses the Madgwick algorithm.
    The update method must be called periodically.

    Attributes:
        declination (int): Offset for true north. A +ve value adds to heading
        magbias (tuple): Local magnetic bias factors: set from calibration
        deltat: Time between updates
        q: Vector to hold quaternion
        GyroMeasError: Original code indicates this leads to a 2 sec response time
        beta: Compute beta (see README)
        pitch:
        heading:
        roll:


    """

    def __init__(self, declination=0):
        """initiates Fusion.

        Args:
            declination (int): Optional offset for true north. A +ve value adds to heading

        Returns:

        Raises:

            """

        self.declination = declination
        self.magbias = (0, 0, 0)            # local magnetic bias factors: set from calibration
        #self.deltat = DeltaT(timediff)      # TODO Time between updates
        self.q = [1.0, 0.0, 0.0, 0.0]       # vector to hold quaternion
        GyroMeasError = radians(40)         # Original code indicates this leads to a 2 sec response time
        self.beta = sqrt(3.0 / 4.0) * GyroMeasError  # compute beta (see README)
        self.pitch = 0
        self.heading = 0
        self.roll = 0
