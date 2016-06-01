#!/usr/bin/python

import serial
from time import sleep
ser = serial.Serial('/dev/ttyUSB0',
                    baudrate=1200,
                    bytesize=serial.SEVENBITS,
                    parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=10,
                    xonxoff=0,
                    rtscts=1)
#wavelength = 500
sleep(.1)
#ser.write('G{0}\r'.format(wavelength))
sleep(0.5)
ser.write('SC\r')
sleep(5)
ser.write('SO\r')

print( ser.read(size=10))


def light(wavelength):
    ser.write('G{0}\r'.format(wavelength))
    
    
    
