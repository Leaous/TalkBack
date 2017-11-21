from google.cloud import translate
from os import *
import os
import io

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from audio import *
from speech2text import *


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=("/Users/spencerburleigh/Downloads/servicekey.json")

def runTranslate(text, language="en"):
    #instantiates client
    translate_client = translate.Client()

    #api call to do translation
    translation = translate_client.translate(
        text,
        target_language = language)

    return('{}'.format(translation['translatedText']))

def speak(text, language):
    if language == "ar":
        system("say -v "+"Tarik "+ text)
    elif language == "zh":
        system("say -v "+"Ting-Ting "+ text)
    elif language == "en":
        system("say -v "+"Samantha "+ text)
    elif language == "fr":
        system("say -v "+"Aurelie "+ text)
    elif language == "de":
        system("say -v "+"Petra "+ text)
    elif language == "hi":
        system("say -v "+"Lekha "+ text)
    elif language == "it":
        system("say -v "+"Paola "+ text)
    elif language == "ja":
        system("say -v "+"Otoya "+ text)
    elif language == "ko":
        system("say -v "+"Yuna "+ text)
    elif language == "pt":
        system("say -v "+"Felipe "+ text)
    elif language == "ru":
        system("say -v "+"Yuri "+ text)
    elif language == "es":
        system("say -v "+"Jorge "+ text)

def run():
    record("test.rav")
    text=s2t("test.rav")
    text=runTranslate(text, "zh")
    speak(text, "zh")
