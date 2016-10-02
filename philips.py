#!/usr/bin/python
import time
import serial
import sys
from functools import reduce
command_map = {
        "POWER-GET": [0x19],
        "ON":        [0x18, 0x02],
        "OFF":       [0x18, 0x01],
        "PIC-NORM":  [0x3A, 0x00],
        "PIC-CUST":  [0x3A, 0x01],
        "PIC-REAL":  [0x3A, 0x02],
        "PIC-FULL":  [0x3A, 0x03],
        "PIC-21-9":  [0x3A, 0x04],
        "PIC-DYN":   [0x3A, 0x05],
        "PIP-OFF":   [0x3C, 0x00, 0x00, 0x00, 0x00],
        "PIP-BL":    [0x3C, 0x01, 0x00, 0x00, 0x00],
        "PIP-TL":    [0x3C, 0x01, 0x01, 0x00, 0x00],
        "PIP-TR":    [0x3C, 0x01, 0x02, 0x00, 0x00],
        "PIP-BR":    [0x3C, 0x01, 0x03, 0x00, 0x00],
        "VOL0":      [0x44, 0x00],
        "VOL10":     [0x44, 0x0A],
        "VOL20":     [0x44, 0x14],
        "VOL30":     [0x44, 0x1e],
        "VOL40":     [0x44, 0x28],
        "VOL50":     [0x44, 0x32],
        "VOL60":     [0x44, 0x3C],
        "VOL70":     [0x44, 0x46],
        "VOL80":     [0x44, 0x50],
        "VOL90":     [0x44, 0x5A],
        "VOL100":    [0x44, 0x64],
        "M-NORM":    [0x32, 0x32, 0x32, 0x32, 0x32, 0x32],
        "M-MOVIE":   [0x32, 0x64, 0x32, 0x32, 0x5A, 0x32],
        "REP-INPUT": [0xAD],
        "IN-VGA":    [0xAC, 0x05, 0x00, 0x01, 0x00],
        "IN-HDMI":   [0xAC, 0x06, 0x02, 0x01, 0x00],
        "IN-MHDMI":  [0xAC, 0x06, 0x03, 0x01, 0x00],
        "IN-DP":     [0xAC, 0x09, 0x04, 0x01, 0x00],
        "IN-MDP":    [0xAC, 0x09, 0x05, 0x01, 0x00],




    }

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
}
'''
#configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
# prepare the command to send
buf = bytearray(command_map[str(sys.argv[1])]) 
buf.insert(0, 0xa6)  # header
buf.insert(1, 0x01)  # id
buf.insert(2, 0x00)  # category
buf.insert(3, 0x00)  # page
buf.insert(4, 0x00)  # function
buf.insert(5, len(buf)-3)  # length
buf.insert(6, 0x01) 
buf.append(reduce(lambda a, b: a ^ b, buf))
print(bytes(buf))
ser.write(bytes(buf))
ser.close()
