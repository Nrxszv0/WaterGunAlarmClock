import serial


ser = serial.Serial("COM3", 9600, timeout=.01)
while True:
    i = 'off'
    ser.write(i.encode())
    print(ser.readline().decode('ascii'))