#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Name: logtemp-deamon.py:
# Copyright (c) 2019 c0ri <gaggleoffools@gmail.com>
# Description:
# This is a little Python code which will monitor the temperature of
# your Raspberry Pi and log it to disk on a time delay. It is run as
# a daemon.
# 
# Requires: deamonize 
#  pip install deamonize
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
from daemonize import Daemonize
import re
from time import sleep
from gpiozero import CPUTemperature


pid = "/tmp/raspi-fancontrol.pid"
tempfile = "/root/temphistory.txt"

#Delay time to retry
delay_time = 60

def main():   
  while True:
   
    try:
   
      cpu = CPUTemperature()
      f=open(tempfile, "a+")
      f.write("The Temperature is: " + str(cpu.temperature) + " Deg. C\n")
      f.close()

      time.sleep(60)
   
    except Exception, e:
   
      print "Couldn't collect. Trying again in ", delay_time/60 ,"minute(s)."
      sleep(delay_time)


daemon = Daemonize(app="raspi-fancontrol", pid=pid, action=main)
daemon.start()
