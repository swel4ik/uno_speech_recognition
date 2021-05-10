import speech_recognition as sr
import time


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    start_time = time.time()
    audio = r.listen(source, phrase_time_limit=10)

try:
    text = r.recognize_google(audio)
    print("Human's command: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))