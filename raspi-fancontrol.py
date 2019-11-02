#########################################################################
# Name: raspi-fancontrol.py:
# Copyright (c) 2019 @c0ri <gaggleoffools@gmail.com>
#                    
# Description:
# This is a little Python code which will control a simple fan for your
# Raspberry Pi.
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
from time import sleep
import sys
from gpiozero import CPUTemperature

cpu = CPUTemperature()
print("The current temperature is: " + str(cpu.temperature) + " Deg. C")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# -- Fan set to GPIO Pin 7
fan = 7
# -- Setup Fan
GPIO.setup(fan, GPIO.OUT)

if cpu.temperature >= "55":
    GPIO.output(fan, GPIO.HIGH)
elif cpu.temperature <= "45":
    GPIO.output(fan, GPIO.LOW)
else:
    # -- If we can't read the temperature or for some reason it didn't return, fail with fan on.
    GPIO.output(fan, GPIO.HIGH)
