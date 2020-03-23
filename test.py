import serial

serialport = serial.Serial("COM2", 9600, timeout=0.5)
my_bytes = b'\x02\x03\x76\x35\x30\x2e\x30\x2e\x35'
while True:
    c = serialport.read()
    if len(c) != 0:
        print(c)
        serialport.write(my_bytes)
