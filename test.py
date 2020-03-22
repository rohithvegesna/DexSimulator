import serial

serialport = serial.Serial("COM2", 9600, timeout=0.5)
rcvd = ""
while True:
    c = serialport.read()
    if len(c) != 0:
        rcvd += c.decode("utf-8")
        for ch in c:
            print(ord(ch), " ",)
