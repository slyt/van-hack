import time
from serial.tools import list_ports  # pyserial

def enumerate_serial_devices():
    return set([item for item in list_ports.comports()])

def check_new_devices(old_devices):
    devices = enumerate_serial_devices()
    added = devices.difference(old_devices)
    removed = old_devices.difference(devices)
    if added:
        print('added: {}'.format(added))
    if removed:
        print('removed: {}'.format(removed))
    return devices

# Quick and dirty timing loop
old_devices = enumerate_serial_devices()
while True:
    old_devices = check_new_devices(old_devices)
    time.sleep(0.5)