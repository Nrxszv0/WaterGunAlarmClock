import os
import time
import playsound 
import speech_recognition as sr 
from gtts import gTTS

def speak(text):
    tts = gTTS(text = text, lang="en") #transform text to audio file in english
    fileName = "voice.mp3" #save then paly file
    tts.save(fileName)
    playsound.playsound(fileName)

speak("cap, you sleepin")
