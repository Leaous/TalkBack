# TalkBack

This is the Hack112 project Rebecca Hong, Aditya Shekar and I built over ~10 hours. Thank you to Google, Panatir, Hudson River Trading, Oracle, and Union Pacific for sponsoring this awesome event. Thank you to 112 staff for making us go to sleep. 

TalkBack helps you to have a natural conversation with someone who speaks another language. Select a target language and then  press record. When the program detects you are done speaking, it converts the audio to speech, translates it, and then uses the appropriate macOS system voice to speak the translation. With a fast internet connection, spoken output can take as little as 5 seconds to be returned.

We make extensive use of the Google Cloud platform's APIs to maximize transcription and translation quality. An original implementation of this program also used a Google Cloud API to turn translated text to audio but we found that by downloading and using macOS system voices, the process ran faster and the voices sounded a lot better.

Languages Supported: English, Arabic, Chinese, French, German, Hindi, Italian, Japanese, Korean, Portuguese, Russian, Spanish

My role in the project was to design the general flow of the system as well as the translation (t.py) and convertion of translated text to speech using the system voices (text2speech.py).
