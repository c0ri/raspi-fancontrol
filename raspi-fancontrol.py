#########################################################################
# Name: raspi-fancontrol.py:
# Copyright (c) 2019 c0ri <gaggleoffools@gmail.com> 
# Description:
# This is a little Python code which will control a simple fan for your
# Raspberry Pi. 
# 
# Updates:
#   I have since turned this into a deamon for various reasons. I left 
#   this code here to test the outputs on your GPIO Pins. You need to
#   figure out which pin to use BCM or BOARD. After setting that below
#   then you will need to also set the fan variable for the correct pin.
#
# Requires: rpigpio  
#  pip install rpigpio
#  I wrote this for Python v2.x
#
# -- License
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#  If not, please go read it here:
#  https://en.wikipedia.org/wiki/GNU_General_Public_License
#
##########################################################################

import RPi.GPIO as GPIO
import time
from time import sleep
import sys
from gpiozero import CPUTemperature

cpu = CPUTemperature()
print("The current temperature is: " + str(cpu.temperature) + " Deg. C")

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# -- Fan set to GPIO Pin 7
fan = 11
# -- Setup Fan
GPIO.setup(fan, GPIO.OUT)

if cpu.temperature >= 55.0:
    print("Fan setting is ON")
    GPIO.output(fan, GPIO.HIGH)
elif cpu.temperature <= 45.0:
    print("Fan setting is OFF")
    GPIO.output(fan, GPIO.LOW)
else:
    # -- If we can't read the temperature or for some reason it didn't return, fail with fan on.
    GPIO.output(fan, GPIO.HIGH)

time.sleep(5)
