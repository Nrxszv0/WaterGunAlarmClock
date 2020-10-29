import serial
import time
ser = serial.Serial("COM3", 9600, timeout=.01)

while True:
    i = input("input(on/off): ").strip()
    if i == 'done':
        print('finished')
        break
    ser.write(i.encode()) #encodes to bytes
    time.sleep(0.1)
    print(ser.readline().decode('ascii'))

ser.close()