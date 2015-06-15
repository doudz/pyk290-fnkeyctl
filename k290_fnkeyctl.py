#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Reconfigures the way the function keys on Logitech K290 keyboards work

Python port of https://github.com/milgner/k290-fnkeyctl
"""
__author__ = "Sébastien RAMAGE"
__version__ = "0.1"
__email__ = "sebastien.ramage@gmail.com"

import sys
import usb1

USB_VENDOR_LOGITECH = 0x046d
USB_PRODUCT_K290 = 0xc31f

def main(argv):
	context = usb1.USBContext()
	device = context.openByVendorIDAndProductID(USB_VENDOR_LOGITECH,USB_PRODUCT_K290)
	if not device:
		print('Logitech K290 not found on this system')
		return 2
	
	reset = 0 if '-r' in argv or '--reset' in argv else 1
		
	err = device.controlWrite(0x40,2,0x001a,reset,b'',1000)
	if not err:
		behaviour = "regular" if reset else "default"
		print('Successfully set function keys to {0} behaviour'.format(behaviour))
		return 0
	else:
		print('Something went wrong when sending the command: {0}'.format(err))
		return 1
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
