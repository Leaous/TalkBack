#takes in a file, returns a string for transcript
#modified from https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/speech

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from audio import *

languages={}

def convertToLangCode(language):
    

def s2t(langCode='en-US'):
    file='test.rav'
    record(file)
    transcript=""
    # Instantiates a client
    client = speech.SpeechClient()
    with io.open(file, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=langCode)
    response = client.recognize(config, audio)
    for result in response.results:
        transcript+=str(result.alternatives[0].transcript)
    return transcript, langCode
