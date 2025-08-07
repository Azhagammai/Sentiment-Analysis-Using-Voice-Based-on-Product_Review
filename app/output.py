import speech_recognition as sr
from analyze import pred
import matplotlib.pyplot as plt


def transcribe_audio(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text
audio_path = "C:\\Users\\kabil\\Downloads\\Project\\Project\\program\\test.wav" 
text = transcribe_audio(audio_path)
pred(text)
print(text)
