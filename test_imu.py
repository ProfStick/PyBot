""" A micropython based robot.

Robot using micropython based on an Adafruit Feather MO
https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/overview

Pins
A0/D14
A1/D15
A2/D16
A3/D17
A4/D18
A5/D19
D5 		MA1_PIN
D6		MA2_PIN
D8		NEOPIXEL
D9		BAT_PIN
D10		MB1_PIN
D11		MB2_PIN
D12
D13 	LED_PIN
"""
#TODO neopixel to reflect battery status
__author__ = "Geoff Goldrick"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "geoff.goldrick@det.nsw.edu.au"
__status__ = "Prototype"

import board
import busio #needed for IMU
import digitalio
import analogio
import time
import neopixel

from adafruit_motor import stepper
import adafruit_lsm9ds1 #IMU

BAT_PIN = board.D9
LED_PIN = board.D13
NEO_PIN = board.NEOPIXEL

#Motor setup
MA1_PIN = board.D5
MA2_PIN = board.D6
MB1_PIN = board.D10
MB2_PIN = board.D11

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

bat = analogio.AnalogIn(board.D9)
neo = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.25)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
#stepper1 = stepper.StepperMotor(MA1_PIN, MA2_PIN, MB1_PIN, MB2_PIN)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

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

    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.accelerometer))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.magnetometer))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.gyroscope))
    print('Temperature: {0:0.2f}C'.format(sensor.temperature))

'''    
	for i in range(100):
        stepper_motor.onestep()
        time.sleep(0.01)

	for i in range(100):
		stepper_motor.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)
'''