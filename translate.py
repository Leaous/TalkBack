#Graphics Code from the 112 website
#Button code from effbot.org
#Drop down code from stack overflow

from tkinter import *
from google.cloud import translate
from os import *
import os
import io
from text2Speech import *
import string

def draw(canvas, width, height):
    pass # replace with your drawing code!



def recordCallback():
    data.state=not data.state
    CHUNK = 1024 #measured in bytes
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 #common sampling frequency
    RECORD_SECONDS=5
    file="test.rav"
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        soundData = stream.read(CHUNK)
        frames.append(soundData)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def playCallback():
    inpLanguage=variableInput.get().lower()
    languages=initLangCodes()
    inpLangCode=languages[inpLanguage]
    text=s2t("test.rav", inpLangCode)
    oLanguage=variableOutput.get().lower()
    oLangCode=languages[oLanguage]
    print(oLanguage)
    text=runTranslate(text,oLangCode)
    print(text)
    speak(text, oLangCode)



class Struct(): pass
data = Struct()
data.state = False



width = 600 
height = 400
root = Tk()
canvas = Canvas(root, width=width, height=height)
canvas.create_text(width/2, height/5, text = "Verbal Translator", 
                font = "arial 20", fill = "black")
variableInput = StringVar(root)
variableInput.set("English") # default value

variableOutput = StringVar(root)
variableOutput.set("English")



w = OptionMenu(root, variableInput, "English", "Arabic", "Chinese", "French", 
            "German", "Hindi", "Italian", "Japanese", "Korean", "Portuguese",
            "Russian", "Spanish")
v = OptionMenu(root, variableOutput, "English", "Arabic", "Chinese", "French", 
            "German", "Hindi", "Italian", "Japanese", "Korean", "Portuguese",
            "Russian", "Spanish")
b = Button(root, text="Record", command = recordCallback, height = 10, width =10)
play = Button(root, text="Play", command = playCallback, height = 10, width =10)
b.pack()
play.pack()
w.pack()
v.pack()
canvas.pack()
draw(canvas, width, height)
root.mainloop()
print("bye")







"""
from tkinter import *

master = Tk()

def callback():
    print ("click!")

b = Button(master, text="Record", command=callback)
b.pack()

mainloop()
"""
