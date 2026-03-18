import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.9)

def speak(text: str):
    print(f"🌩️ Stormy: {text}")
    engine.say(text)
    engine.runAndWait()
