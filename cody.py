""" A micropython based robot.

Robot using micropython based on an Adafruit Feather MO
https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/overview

"""
#TODO neopixel to reflect battery status
__author__ = "Geoff Goldrick"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "geoff.goldrick@det.nsw.edu.au"
__status__ = "Prototype"

import board
import digitalio
import analogio
import time
import neopixel
 
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


BAT_PIN = board.D9
LED_PIN = board.D13

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

bat = analogio.AnalogIn(board.D9)
neo = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.25)


def getVoltage():
    return (bat.value * 3.3) / 65536 * 2
 
while True:
    batVoltage = getVoltage()
    print("battery voltage: {:.2f}".format(batVoltage))
    if batVoltage > 3.6:
        neo.fill(GREEN)
    elif batVoltage > 3.5:
        neo.fill(YELLOW)
    else:
        neo.fill(RED)
    
    led.value = True
    time.sleep(1)
    led.value = False
    led.value = False
    time.sleep(2)