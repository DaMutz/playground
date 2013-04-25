#!/usr/bin/python
import time
import ablib

def modem_on():
	print "Modem ON"

	quectel_power = ablib.Pin('W','10','high')
	quectel_power_key = ablib.Pin('E','10','low')

	quectel_power_key.on()
	time.sleep(1)
	quectel_power_key.off()


if __name__ == '__main__':
	modem_on()

