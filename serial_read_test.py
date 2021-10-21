import serial

with serial.Serial('COM3', 19200, timeout=1) as ser:
    x = ser.read()          # read one byte
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line
    print(line)