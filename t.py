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
import time 

def draw(canvas, width, height):
    pass # replace with your drawing code!

def drawRecordButton(canvas, recording):
    canvas.create_rectangle(0,height/2-50, width/3,height/2-70, fill="white", width=0)
    if recording:
        color="red"
        msg=""
    elif not recording:
        color="white"
        msg="Not"
    canvas.create_oval(width/3-10, height/2 - 50, width/3+10, height/2-70, fill=color)
    canvas.create_text(width/3-30, height/2-60, text=msg+"Recording", anchor="e")

def recordCallback():
    path="test.rav"
    drawRecordButton(canvas, True)
    canvas.update()
    sample_width, data = record()
    drawRecordButton(canvas, False)
    canvas.update()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


def playCallback():
    inpLanguage=variableInput.get().lower()
    languages=initLangCodes()
    inpLangCode=languages[inpLanguage]
    text=s2t("test.rav", inpLangCode)
    oLanguage=variableOutput.get().lower()
    oLangCode=languages[oLanguage]
    text=runTranslate(text,oLangCode)

    speak(text, oLangCode)



class Struct(): pass
data = Struct()
data.state = False

width = 600 
height = 400
root = Tk()
canvas = Canvas(root, width=width, height=height)
canvas.create_text(width/3, height/2 - 25, text = "Verbal Translator", 
                font = "arial 20", fill = "black")
canvas.create_text(width/3-20, height/2, 
    text="Select an Input and Output Language, then hit record! Verbal Translator will listen until you stop talking. Press play to hear what you said in the output language.", width=width/3, anchor="n")
variableInput = StringVar(root)
variableInput.set("Input Language") # default value

variableOutput = StringVar(root)
variableOutput.set("Output Language")



w = OptionMenu(root, variableInput, "Input Language", "English", "Arabic", "Chinese", "French", 
            "German", "Hindi", "Italian", "Japanese", "Korean", "Portuguese",
            "Russian", "Spanish")
v = OptionMenu(root, variableOutput, "Output Language", "English", "Arabic", "Chinese", "French", 
            "German", "Hindi", "Italian", "Japanese", "Korean", "Portuguese",
            "Russian", "Spanish")
b = Button(root, text="Record", command = recordCallback, height = 10, width =10)
play = Button(root, text="Play", command = playCallback, height = 10, width =10)
b.place(x=300,y=100)
play.place(x=300,y=200)
w.pack()
v.pack()
canvas.pack()
draw(canvas, width, height)
root.mainloop()
