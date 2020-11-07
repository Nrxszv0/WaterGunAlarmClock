import cv2
import numpy as np
import serial
import matplotlib.pyplot as plt

import time
import datetime as dt

import os
import playsound 
import speech_recognition as sr 
from gtts import gTTS

# ser = serial.Serial("COM3", 9600, timeout=.01)
face_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_eye.xml')


def speak(text):
    tts = gTTS(text = text, lang="en") #transform text to audio file in english
    fileName = text + ".mp3" #save then play file
    tts.save(fileName)
    playsound.playsound(fileName)

def get_audio():
    #return what we say into microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said


pRun = False
# wakeTime = input("Enter the alarm time(H:M:S)")
# print(wakeTime)
wakeTime = "18:42:30"
stopTime = "18:43:20"

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



def introSound():
    for i in range(3):
        playsound.playsound("Sounds/Beep.mp3")
    playsound.playsound("Sounds/Get up before I pop a cap in you.mp3")
    playsound.playsound("Sounds/I am going to shoot you in.mp3")
    for i in range(3,0,-1):
        if i == 4:
            file = "Sounds/four.mp3" #idk why speak("4") creates an invalid file
        else:
            file = "Sounds/"+ str(i) + ".mp3"
        playsound.playsound(file)
    playsound.playsound("Sounds/Commencing Fire.mp3")

def stopStuff():
    i = 'off'
    ser.write(i.encode())
    print(ser.readline().decode('ascii'))
    playsound.playsound("Done.mp3")
    pRun = False

introSound()
i = 'on'
ser.write(i.encode())
vid = cv2.VideoCapture(0)


# pRun = False
stopCounter = 0
endProgramVal = 10
pRun = True


while pRun:
    
    currentTime = dt.datetime.now()
    now = currentTime.strftime("%H:%M:%S")
    date = currentTime.strftime("%d/%m/%Y")
    if now == stopTime:
        i = 'off'
        ser.write(i.encode())        
        print(ser.readline().decode('ascii'))
        stopStuff()
        break
    

    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5) #depending on size of image you might want to cange vals

    if len(faces) == 0:
        # playsound.playsound("Where you at.mp3")
        if stopCounter < 9:
            playsound.playsound("Move.mp3")

        
        stopCounter+=1
        # print("where you at", stopCounter)

    if len(faces) != 0:
        stopCounter = 0

    if stopCounter >= endProgramVal:
        i = 'off'
        ser.write(i.encode())
                
        print(ser.readline().decode('ascii'))   
        # pRun = False
        stopStuff()
        break    

    for(x,y,w,h) in faces:
        centX = x + (0.5*w)
        centY = y + (0.5*h) #bruh I had a y instead of an h
        centX = int(centX)
        centY = int(centY)
        sCentX =str(int(centX))
        sCentY= str(int(centY))
        data = "X:" +sCentX+"Y:"+sCentY
        # print(data)

        # print(faces,centX,centY)
        ser.write(data.encode())

        cv2.circle(frame,(centX,centY),3,(0,255,0), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+h] #region of gray(image). start y to end y and start x to end x
        roi_color = frame[y:y+h, x:x+h]

    cv2.imshow('frame',frame)

    print(ser.readline().decode('ascii'))

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        # i = 'off'
        # ser.write(i.encode())        
        # pRun = False
        i = 'off'
        ser.write(i.encode())        
        print(ser.readline().decode('ascii'))  
        stopStuff()
        break
time.sleep(0.1)
i = 'off'
ser.write(i.encode()) 
# print(ser.readline().decode('ascii'))

        
    
vid.release()
cv2.destroyAllWindows()

# ser.close()
        # dont want to look for eyes out of face

# if face not found in screen
    # "are you awake"
    # "cap I cant see you 
    # Where you at"




# i = input("input(on/off): ").strip()
# if i == 'on':
#     pRun = True
# ser.write(i.encode()) #encodes to bytes
# print(ser.readline().decode('ascii'))
