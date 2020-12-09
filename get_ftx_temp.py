#!/usr/bin/env python3

import minimalmodbus
import sys
import rrdtool
from decimal import *

ior = 0

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #port, slaveadress
instr.precalculate_read_size = False


temp = None
while temp is None:
	try:
		temp = instr.read_registers(1, 7, functioncode=4)
	except:
		pass

tempDec = []
for i in temp:
	if i > 6000:
		ior = i
		i = i - 65536 #65535 ar hogsta mojliga int()
	i = float(i) / 10
	tempDec.append(i)

if len(sys.argv) > 1: #if started with argument just print
	print("Database not updated, got these values:")
	print(tempDec)
	print("---------------------------------------------------")
else:
	print("Updating database with:")
	print(tempDec)
	for i in tempDec:
		ret = rrdtool.update('/home/pi/rrdDB/ftxtemp_db.rrd', 'N:%s:%s:%s:%s:%s:%s:%s' %(tempDec[0], tempDec[1], tempDec[2], tempDec[3], tempDec[4], tempDec[5], tempDec[6]));
		if ret:
			print(rrdtool.error())
