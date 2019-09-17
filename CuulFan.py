#!/usr/bin/env python3

##############
# Config     #
##############

fanPin = 12
tempHigh = 50
tempLow = 40
sleeptime = 15



##############
# Code       #
##############

import RPi.GPIO as GPIO
import signal
import time
import threading
import vcgencmd as vc

GPIO.setmode(GPIO.BOARD)
GPIO.setup(fanPin, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(fanPin, 100)

e = threading.Event()
stop = False

def handler_signals(sig, frame):
    global stop
    e.set()
    stop = True

signal.signal(signal.SIGTERM, handler_signals)
signal.signal(signal.SIGINT, handler_signals)

while not stop:
    temp = int(vc.measure_temp())
    if temp >= tempHigh:
        pwm.start(100)
    elif temp <= tempLow:
        pwm.start(0)
    e.wait(timeout=sleeptime)

GPIO.cleanup()
