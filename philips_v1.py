#!/usr/bin/python
import time
import serial
import sys

'''
command = {
'ON':        '\xa6\x01\x00\x00\x00\x04\x01\x18\x02\xb8',
'OFF':       '\xa6\x01\x00\x00\x00\x04\x01\x18\x01\xbb',
#'PIC-NORM':  '\x3A\x00',
#'PIC-CUST':  '\x3A\x01',
#'PIC-REAL':  '\x3A\x02',
#'PIC-FULL':  '\x3A\x03',
#'PIC-21-9':  '\x3A\x04',
#'PIC-DYN':   '\x3A\x05',
'PIP_OFF':   '\xa6\x01\x00\x00\x00\x07\x01\x3c\x00\x00\x00\x00\x9d',
'PIP_BL':    '\xa6\x01\x00\x00\x00\x07\x01\x3c\x01\x00\x00\x00\x9c',
'PIP_TL':    '\xa6\x01\x00\x00\x00\x07\x01\x3c\x01\x01\x00\x00\x9d',
'PIP_TR':    '\xa6\x01\x00\x00\x00\x07\x01\x3c\x01\x02\x00\x00\x9e',
'PIP_BR':    '\xa6\x01\x00\x00\x00\x07\x01\x3c\x01\x03\x00\x00\x9f',
'VOL0':      '\xa6\x01\x00\x00\x00\x04\x01\x44\x00\xe6',
'VOL10':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x0a\xec',
'VOL20':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x14\xf2',
'VOL30':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x1e\xf8',
'VOL40':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x28\xce',
'VOL50':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x32\xd4',
'VOL60':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x3c\xda',
'VOL70':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x46\xa0',
'VOL80':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x50\xb6',
'VOL90':     '\xa6\x01\x00\x00\x00\x04\x01\x44\x5a\xbc',
'VOL100':    '\xa6\x01\x00\x00\x00\x04\x01\x44\x64\x82',
#'M-NORM':    '\x32\x32\x32\x32\x32\x32',
#'M-MOVIE':   '\x32\x64\x32\x32\x5A\x32',
#'REP-INPUT': '\xAD',
#'IN-VGA':    '\xAC\x05\x00\x01\x00',
'IN_HDMI':   '\xa6\x01\x00\x00\x00\x07\x01\xac\x06\x02\x01\x00\x08',
#'IN-MHDMI':  '\xAC\x06\x03\x01\x00',
'IN_DP':     '\xa6\x01\x00\x00\x00\x07\x01\xac\x09\x04\x01\x00\x01',
#'IN-MDP':    '\xAC\x09\x05\x01\x00'
}'''
# get the command line argument
gg = (str(sys.argv[1]))
#configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
if gg == "VOL100":
#    print("100")
#    print(ser.name)
#    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
# send the character to the device
# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x64\x82')
#    s = ser.read(100)
#    print(s)
    ser.close()
elif gg == "VOL90":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x5a\xbc')
    ser.close()
elif gg == "VOL80":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x50\xb6')
    ser.close()
elif gg == "VOL70":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x46\xa0')
    ser.close()
elif gg == "VOL60":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x3c\xda')
    ser.close()
elif gg == "VOL50":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x32\xd4')
    ser.close()
elif gg == "VOL40":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x28\xce')
    ser.close()
elif gg == "VOL30":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x1e\xf8')
    ser.close()
elif gg == "VOL20":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x14\xf2')
    ser.close()
elif gg == "VOL10":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x0a\xec')
    ser.close()
elif gg == "VOL0":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x44\x00\xe6')
    ser.close()
elif gg == "PIP-TR":
    ser.write(b'\xa6\x01\x00\x00\x00\x07\x01\x3c\x01\x02\x00\x00\x9e')
    ser.close()
elif gg == "PIP-OFF":
    ser.write(b'\xa6\x01\x00\x00\x00\x07\x01\x3c\x00\x00\x00\x00\x9d')
    ser.close()
elif gg == "IN-HDMI":
    ser.write(b'\xa6\x01\x00\x00\x00\x07\x01\xac\x06\x02\x01\x00\x08')
    ser.close()
elif gg == "IN-DP":
    ser.write(b'\xa6\x01\x00\x00\x00\x07\x01\xac\x09\x04\x01\x00\x01')
    ser.close()
elif gg == "OFF":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x18\x01\xbb')
    ser.close()
elif gg == "ON":
    ser.write(b'\xa6\x01\x00\x00\x00\x04\x01\x18\x02\xb8')
    ser.close()
