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

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

#ser = serial.Serial("COM5", 9600, timeout=.01)
face_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Harrcascades/haarcascade_eye.xml')

kbd = KeyboardController()
mse = MouseController()

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

# pRun = False
# isWakeTime = False
# # wakeTime = input("Enter the alarm time(H:M:S)")
# # print(wakeTime)
# wakeTime = "7:00:00"
# while True:    
#     currentTime = dt.datetime.now()
#     now = currentTime.strftime("%H:%M:%S")
#     date = currentTime.strftime("%d/%m/%Y")
#     if now == wakeTime:
#         pRun = True
#         break
#     # if pRun:
#         #print("date is:", date)
#         # print(now)
#     # time.sleep(1)



# for i in range(3):
#     playsound.playsound("Beep.mp3")
# playsound.playsound("Wake up before I pop a cap in yo ass .mp3")
# playsound.playsound("I am going to shoot you in.mp3")
# for i in range(5,0,-1):
#     if i == 4:
#         file = "four.mp3" #idk why speak("4") creates an invalid file
#     else:
#         file = str(i) + ".mp3"
#     playsound.playsound(file)
#     if i > 1:
#         time.sleep(0.75)

vid = cv2.VideoCapture(0)

# playsound.playsound("Commencing Fire.mp3")

# pRun = False
pRun = True
while pRun:
    # text = get_audio()
   

    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5) #depending on size of image you might want to cange vals

    if len(faces) == 0:
        # playsound.playsound("Where you at.mp3")
        print("where you at")

    for(x,y,w,h) in faces:
        centX = x + (0.5*w)
        centY = y + (0.5*h) #bruh I had an y instead of an h
        centX = int(centX)
        centY = int(centY)
        sCentX =str(int(centX))
        sCentY= str(int(centY))
        data = "X:" +sCentX+"Y:"+sCentY
        print(data)
        # print(faces,centX,centY)
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

# if face not found in screen
    # "are you awake"
    # "cap I cant see you 
    # Where you at"




# i = input("input(on/off): ").strip()
# if i == 'on':
#     pRun = True
# ser.write(i.encode()) #encodes to bytes
# print(ser.readline().decode('ascii'))