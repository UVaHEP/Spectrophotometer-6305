import vxi11
import serial
from time import sleep
from agilent import *


host = '128.143.196.233'
port = '5025'
voltage = -1.2
wstart = 400
wstop = 700
wdelta = 50

sp = serial.Serial('/dev/ttyUSB0',
                    baudrate=1200,
                    bytesize=serial.SEVENBITS,
                    parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=10,
                    xonxoff=0,
                    rtscts=1)

a = Agilent(host, port)

wavelength = wstart

while wavelength <= wstop:
    sp.write('G{0}\r'.format(wavelength))
    sleep(0.5)
    current1 = float(a.ReadIVPoint(voltage))
    current2 = float(a.ReadIVPoint(voltage))
    current3 = float(a.ReadIVPoint(voltage))
    current  = (current1 + current2 + current3)/3.0
    print '{0} {1}'.format(wavelength, current)
    wavelength += wdelta
    
