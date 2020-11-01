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

def get_audio():
    #return waht we say into microphone
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

# speak("hello")
# get_audio()

text = get_audio()

if "hello" in text:
    speak("hello, how are you doing")

if "what is your name" in text:
    speak("I'm Elon Musk")
