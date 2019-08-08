#!/usr/bin/env python
# -*- coding: utf-8 -

import minimalmodbus
import sys
import os
import time
import RPi.GPIO as GPIO

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.STOPBITS = 2

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 4) #port, slaveadress
instr.precalculate_read_size = False
#instr.debug = True

GPIO.setmode(GPIO.BCM)

def set_away(state):
	# will put FTX in desired state if not allready.

	if state == "on":
		if read_status() == 0:
			switch_status(0)
		else:
			print "No change in state"
			pass
	elif state == "off":
		if read_status() == 1:
			switch_status(1)
		else:
			print "No change in state"
			pass

def read_status(register=3):
	statusstr = ["off", "on"]
	status = None
	while status is None:
		try:
			status = instr.read_bit(register, functioncode=1) #läs av status för bortaläge
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
			instr.write_bit(3, switched_status, functioncode=5) #Switcha status mellan av/på
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
	# This takes about 1 millisecond per loop cycle

	while (GPIO.input(pin) == GPIO.LOW):
	    #print "low"
	    reading += 1
	return reading

if __name__ == '__main__':
	# buff = "191.168.1.69" #example
	# while os.system("ping -n 1 " + buff) == 0: #buff hemma
	# 	if read_status(3) == 0:
	# 	    print(hostname, 'is up!')
	# 		pass
	# 	elif read_status(3) == 1:
	# 	    print(hostname, 'is down!')

	# 		switched_status(read_status(3))
	# 		pass
	# else: 
	# 	pass  

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
			#print "broke while loop"
			break
	average = sum(l) / float(len(l))
	print("Average: {}".format(average))

	if average > home:
		set_away("off")
		print "Alarm deactivated"
	elif average <= away:
		set_away("on")
		print "Alarm activated"
	elif away <= average <= home_protection:
		set_away("off")
		print "Home protection activated"
	print "Done"


GPIO.cleanup(10)

pass
