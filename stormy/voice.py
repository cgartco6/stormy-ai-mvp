import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)   # Speed
engine.setProperty('volume', 0.9)

def speak(text: str):
    print(f"Stormy (voice): {text}")
    engine.say(text)
    engine.runAndWait()
