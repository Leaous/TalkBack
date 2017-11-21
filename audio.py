#modified from https://abhgog.gitbooks.io/pyaudio-manual/content/sample-project.html

#audio lecture
#pyaudio demo

#Code modified from https://people.csail.mit.edu/hubert/pyaudio/

###########################################################################
######################### Playing a WAV file ##############################
###########################################################################


"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
from array import array
from struct import pack

def play(file):
    CHUNK = 1024 #measured in bytes

    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

###########################################################################
######################### Recording a WAV file ############################
###########################################################################

def record(file):
    CHUNK = 1024 #measured in bytes
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 #common sampling frequency
    RECORD_SECONDS=5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

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
