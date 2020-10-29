import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('Sentdex/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Sentdex/haarcascade_eye.xml')

vid = cv2.VideoCapture(0)
#cv2.imshow('frame',frame)
while True:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5) #depending on size of image you might want to cange vals
    for(x,y,w,h) in faces:
        print(faces,x,y,w,h)

        centX = x + (0.5*w)
        centY = y + (0.5*y)
        centX = int(centX)
        centY = int(centY)
        print(centX,centY)
        cv2.circle(frame,(centX,centY),3,(0,255,0), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+h] #region of gray(image). start y to end y and start x to end x
        roi_color = frame[y:y+h, x:x+h]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3,6)
        
        # ex,ey,ew,eh = eyes
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex +ew, ey+eh), (0,0,255),2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
        #dont want to look for eyes out of face