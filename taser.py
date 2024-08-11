"""
using raspi as it has gpio pins

SIGNAL_PIN =18 // connect signal pin Signal pin
// connect vcc of relay to 5v 
// keep all ground common 

"""


#Import all neccessary features to code.
import RPi.GPIO as GPIO
import time

SIGNAL_PIN=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SIGNAL_PIN, GPIO.OUT)


def taser():
    #turning taset on
    GPIO.output(SIGNAL_PIN,1)
    #waiting secs
    time.sleep(2)
    #turing taser off
    GPIO.output(SIGNAL_PIN,0)

