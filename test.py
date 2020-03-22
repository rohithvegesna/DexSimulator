import serial

serialport = serial.Serial("COM2", 9600, timeout=0.5)
rcvd = []
while True:
    c = serialport.read()
    if len(rcvd) != 0 and len(c) == 0:
        print(rcvd)
        break
    if len(c) != 0:
        rcvd.append(c)
