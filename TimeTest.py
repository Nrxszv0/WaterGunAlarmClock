import cv2
import numpy as np
import serial
import matplotlib.pyplot as plt
import time
import datetime as dt

#ser = serial.Serial("COM5", 9600, timeout=.01)
face_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_eye.xml')

pRun = False
isWakeTime = False
wakeTime = input("Enter the alarm time(H:M:S)")
print(wakeTime)
while True:    
    currentTime = dt.datetime.now()
    now = currentTime.strftime("%H:%M:%S")
    date = currentTime.strftime("%d/%m/%Y")
    if now == wakeTime:
        pRun = True
        break
    # if pRun:
        #print("date is:", date)
        # print(now)
    # time.sleep(1)

vid = cv2.VideoCapture(0)

# i = input("input(on/off): ").strip()
# if i == 'on':
#     pRun = True
# ser.write(i.encode()) #encodes to bytes
# print(ser.readline().decode('ascii'))

while pRun:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5) #depending on size of image you might want to cange vals

    for(x,y,w,h) in faces:
        centX = x + (0.5*w)
        centY = y + (0.5*y)
        centX = int(centX)
        centY = int(centY)
        sCentX =str(int(centX))
        sCentY= str(int(centY))
        data = "X:" +sCentX+"Y:"+sCentY
        print(data)
        # ser.write(data.encode())

        cv2.circle(frame,(centX,centY),3,(0,255,0), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+h] #region of gray(image). start y to end y and start x to end x
        roi_color = frame[y:y+h, x:x+h]

    cv2.imshow('frame',frame)

    # print(ser.readline().decode('ascii'))

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        # i = 'off'
        # ser.write(i.encode())
        pRun = False
        break
    
vid.release()
cv2.destroyAllWindows()
# ser.close()
        # dont want to look for eyes out of face