import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("Hello")
speak("How are you")
speak("This is AI spoken English trainer")