#!/usr/bin/python
import serial
import sys
from functools import reduce
import subprocess
command_map = {
        "POWER-STATE": [0x19],
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
#configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
# prepare the command to send
command = bytearray(command_map[str(sys.argv[1])]) # Data
command.insert(0, 0xa6)  # Header
command.insert(1, 0x01)  # Display ID
command.insert(2, 0x00)  # Category
command.insert(3, 0x00)  # Page
command.insert(4, 0x00)  # Function
command.insert(5, len(command)-3)  # Length
command.insert(6, 0x01) # Control
command.append(reduce(lambda a, b: a ^ b, command)) # Checksum
#print(bytes(command))
ser.write(bytes(command))
ser.close()
subprocess.run(['notify-send', 'Philips', str(sys.argv[1]), '--icon=video-display'])# can use Popen instead of run
