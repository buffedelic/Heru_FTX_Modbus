#!/usr/bin/env python3
# -*- coding: utf-8 -

import minimalmodbus
import sys
import os
import time
import RPi.GPIO as GPIO

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #port, slaveadress
instr.precalculate_read_size = False
#instr.debug = True

GPIO.setmode(GPIO.BCM)

def set_away(state):
	# will put FTX in desired state if not allready.

	if state == "on":
		if read_status() == 0:
			switch_status(0)
		else:
			print("No change in state")
			pass
	elif state == "off":
		if read_status() == 1:
			switch_status(1)
		else:
			print("No change in state")
			pass

def read_status(register=3):
	statusstr = ["off", "on"]
	status = None
	while status is None:
		try:
			status = instr.read_bit(register, functioncode=1) #Read state if away
			print("Away mode is {}".format(statusstr[status]))
			return status
		except:
			pass

def switch_status(status):
	statusstr = ["off", "on"]
	if status == 1:
		switched_status = 0
	else:
		switched_status = 1
	done = False
	while not done:
		try:
			instr.write_bit(3, switched_status, functioncode=5) #Switch between on/off
			done = True
			print("Awaymode switched to {}".format(statusstr[switched_status]))
		except:
			pass

def RCtime (pin=10):
	reading = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(pin, GPIO.IN)

	while (GPIO.input(pin) == GPIO.LOW):
	    reading += 1
	return reading

if __name__ == '__main__':

	# Average light sensed from alarm panel.
	home = 20000 # > 50000
	away = 5000 #0-5000
	home_protection = 20000 #5001-20000

	i = 0 
	end = 100
	l = []

	#timeout = time.time() + 60*5 # 5 minutes from now
	timeout = time.time() + 10
 	while i != end:
		l.append(RCtime())
		print l[i]
		i = i + 1
		if time.time() > timeout:
			break
	average = sum(l) / float(len(l))
	print("Average: {}".format(average))

	if average > home:
		set_away("off")
		print("Alarm deactivated")
	elif average <= away:
		set_away("on")
		print("Alarm activated")
	elif away <= average <= home_protection:
		set_away("off")
		print("Home protection activated")
	print("Done")


GPIO.cleanup(10)

pass
