#takes in a file, returns a string for transcript
#modified from https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/speech

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from audio import *

def s2t(file, langCode='en-US'):
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
    return transcript

def transcribe_streaming():
    """Streams transcription of the given audio file."""
    client = speech.SpeechClient()
    CHUNK = 1024 #measured in bytes
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 #common sampling frequency
    RECORD_SECONDS=5
    file="test.rav"
    p = pyaudio.PyAudio()
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audioStream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        content=audioStream.read(CHUNK)
        # In practice, stream should be a generator yielding chunks of audio data.
        stream = [content]
        requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                    for chunk in stream)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US')
        streaming_config = types.StreamingRecognitionConfig(config=config)
        # streaming_recognize returns a generator.
        responses = client.streaming_recognize(streaming_config, requests)
        for response in responses:
            for result in response.results:
                print('Finished: {}'.format(result.is_final))
                print('Stability: {}'.format(result.stability))
                alternatives = result.alternatives
                for alternative in alternatives:
                    print('Confidence: {}'.format(alternative.confidence))
                    print('Transcript: {}'.format(alternative.transcript))

def initLangCodes():
    languages={}
    languages["arabic"]="ar"
    languages["chinese"]="zh"
    languages["english"]="en"
    languages["hindi"]="hi"
    languages["german"]="de"
    languages["french"]="fr"
    languages["italian"]="it"
    languages["japanese"]="ja"
    languages["korean"]="ko"
    languages["portuguese"]="pt"
    languages["russian"]="ru"
    languages["spanish"]="es"
    return languages

''' #sometimes needed depending on input
def initLangCodes():
    languages={}
    languages["arabic"]="ar-SA"
    languages["chinese"]="cmn-Hans-CN"
    languages["english"]="en-US"
    languages["hindi"]="hi-IN"
    languages["german"]="de-DE"
    languages["french"]="fr-FR"
    languages["italian"]="it-IT"
    languages["japanese"]="ja-JP"
    languages["korean"]="ko-KR"
    languages["portuguese"]="pt-PT"
    languages["russian"]="ru-RU"
    languages["spanish"]="es-ES"
    return languages
'''

def findLang(transcript):
    languages=initLangCodes()
    for word in transcript:
        word=lower(word) #convert to lowercase
        if word in languages:
            return languages[word]
