#!/usr/bin/python
import time
import ablib

def modem_off():
	print "Modem OFF"

	quectel_power = ablib.Pin('W','10','low')
	quectel_power_key = ablib.Pin('E','10','low')


if __name__ == '__main__':
	modem_off()

