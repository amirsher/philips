 # Philips BDM4065UC tv/monitor RS232 control
#
# Sabrent USB 2.0 to Serial (9-Pin) DB-9 RS-232 Adapter Cable 6ft Cable (FTDI Chipset) CB-FTDI: https://www.amazon.com/gp/product/B006AA04K0/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1
# SF Cable, DB9 Female to 3.5mm Serial Cable-6 Feet: https://www.amazon.com/gp/product/B004T9BBJC/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1
# Your Cable Store Serial Port 9 Pin Null Modem Adapter DB9 Male / Female RS232: https://www.amazon.com/gp/product/B005QE4YLQ/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1
# Artpot 2.5mm Male to 3.5mm Female Stereo Audio Jack Adapter Cable Black: https://www.amazon.com/gp/product/B00RLNA62Q/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1


import time, re
import traceback
from serialz import Serial


class TV(Serial):

    command_map = {
        "power get": [0x19],
        "power off": [0x18, 0x01],
        "power on": [0x18, 0x02],
        "input get": [0xad],
        "input dp": [0xac, 0x09, 0x04, 0x01, 0x00],  # fd 04
        "input hdmi": [0xac, 0x06, 0x02, 0x01, 0x00],  # fd 02
        "input hdmi2": [0xac, 0x06, 0x03, 0x01, 0x00],  # fd 03
        "input vga": [0xac, 0x05, 0x00, 0x01, 0x00],  # ???
    }

    # result: 0x00 good; 0x01 too long; 0x02 too short; 0x03 cancelled

    def __init__(self, timeout=0.1):    # timeout=0.05
        super(TV, self).__init__(r"FTDIBUS\VID_0403+PID_6001+AI023EETA\0000", timeout=timeout)

    def _send(self, data, device):
        # data = str(data)
        buf = bytearray(data)
        buf.insert(0, 0xa6)  # header
        buf.insert(1, 0x01)  # id
        buf.insert(2, 0x00)  # category
        buf.insert(3, 0x00)  # page
        buf.insert(4, 0x00)  # function
        buf.insert(5, len(buf)-3)  # length
        buf.insert(6, 0x01)  # control
        buf.append(reduce(lambda a, b: a ^ b, buf))  # checksum
        print "_send(%s)" % format_bytearray(buf)
        # time.sleep(1)
        device.write(buf)
        rep = device.read(40)
        # FIXME: retry???
        print "    --> [%d] %s %s" % (len(rep), format_bytearray(rep), format_bytearray(rep[6:-1]))
        result = rep[6:-1]
        return result

    def command(self, cmd):
        return self.send(self.command_map[cmd])

    def toggle_power(self):
        rep = tv.command("power get")
        if rep == '\x19\x01': tv.command("power on")
        elif rep == '\x19\x02': tv.command("power off")


tv = TV()


def format_bytearray(arr):
    return "bytearray(b'%s')" % "".join("\\x{:02x}".format(c) for c in bytearray(arr))

def test():
    for i in xrange(0x06,17):
        for j in xrange(0x3,256):
            # notes: [3]: 40, 41
            TV.command_map["input hdmi"][1] = i
            TV.command_map["input hdmi"][2] = j
            result = tv.command("input hdmi")
            # print format_bytearray(result)
            # print ord(result[1])
            if result[1] == '\x00': return True
    if 1:
        time.sleep(5)
        tv.command("input dp")

def main():
    print tv
    # tv._send(tv.command_map["power get"])
    if 0: test()
    elif 1:
        # tv.command("power get")
        # tv.command("input get")
        # tv.command("power off")
        # tv.command("power on")
        # tv.command("input hdmi")
        tv.command("input hdmi2")
        # time.sleep(5)
        # tv.command("input dp")
        # tv.command("input get")
        # tv.toggle_power()

if __name__ == '__main__':
    main()
