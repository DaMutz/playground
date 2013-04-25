#!/usr/bin/python
import ablib
import time

def usb_power_overrun():
	power_overrun = ablib.Pin('W','9','in')

	while True:
		if power_overrun.get_value()==False:
			print "Power overrun !";
			time.sleep(1)

if __name__ == '__main__':
	usb_power_overrun()

