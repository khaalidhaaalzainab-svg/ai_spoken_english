from speech_engine import speak, listen
from ai_chat import get_response

print("AI Spoken English Trainer Started")

speak("Hello. I am your AI English tutor. Let's practice English.")

while True:

    user_text = listen()

    if user_text == "I did not understand":
        speak("Please speak again")
        continue

    response = get_response(user_text)

    print("AI:", response)

    speak(response)   # Must call speak here

    if "goodbye" in response.lower():
        break