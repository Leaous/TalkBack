from google.cloud import translate
import os, pyaudio

#user credentials - adjust for your json file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
"/Users/spencerburleigh/Desktop/Hack112Translate-a28c06c7603b.json")

##

def runTranslate(text, language):
    #instantiates client
    translate_client = translate.Client()

    #api call to do translation
    translation = translate_client.translate(
        text,
        target_language = language)

    return('{}'.format(translation['translatedText']))

def speak(translatedText, language):
    if language == "ar":
        os.system("say -v "+"Tarik "+ translatedText)
    elif language == "zh":
        os.system("say -v "+"Ting-Ting "+ translatedText)
    elif language == "en":
        os.system("say -v "+"Samantha "+ translatedText)
    elif language == "fr":
        os.system("say -v "+"Aurelie "+ translatedText)
    elif language == "de":
        os.system("say -v "+"Petra "+ translatedText)
    elif language == "hi":
        os.system("say -v "+"Lekha "+ translatedText)
    elif language == "it":
        os.system("say -v "+"Paola "+ translatedText)
    elif language == "ja":
        os.system("say -v "+"Otoya "+ translatedText)
    elif language == "ko":
        os.system("say -v "+"Yuna "+ translatedText)
    elif language == "pt":
        os.system("say -v "+"Felipe "+ translatedText)
    elif language == "ru":
        os.system("say -v "+"Yuri "+ translatedText)
    elif language == "es":
        os.system("say -v "+"Jorge "+ translatedText)

def testSpeak():
    speak(runTranslate("This is only a test. Do not be alarmed", "ar"), "ar")
    speak(runTranslate("This is only a test. Do not be alarmed", "zh"), "zh")
    speak(runTranslate("This is only a test. Do not be alarmed", "en"), "en")
    speak(runTranslate("This is only a test. Do not be alarmed", "fr"), "fr")
    speak(runTranslate("This is only a test. Do not be alarmed", "de"), "de")
    speak(runTranslate("This is only a test. Do not be alarmed", "hi"), "hi")
    speak(runTranslate("This is only a test. Do not be alarmed", "it"), "it")
    speak(runTranslate("This is only a test. Do not be alarmed", "ja"), "ja")
    speak(runTranslate("This is only a test. Do not be alarmed", "ko"), "ko")
    speak(runTranslate("This is only a test. Do not be alarmed", "pt"), "pt")
    speak(runTranslate("This is only a test. Do not be alarmed", "ru"), "ru")
    speak(runTranslate("This is only a test. Do not be alarmed", "es"), "es")

testSpeak()
