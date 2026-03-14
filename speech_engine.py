import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()      # create engine each time
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except:
        return "I did not understand"