import speech_recognition as sr
import json
import os

recognizer = sr.Recognizer()

def listen(timeout=6, phrase_time_limit=10) -> str:
    print("🎤 Listening... Speak now (say 'exit' to quit)")
    
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.strip()
    
    except sr.UnknownValueError:
        print("Couldn't understand. Trying offline...")
    except sr.RequestError:
        print("No internet? Falling back to offline...")
    except Exception:
        pass
    
    # Offline Vosk fallback
    return listen_offline(audio) if 'audio' in locals() else "I didn't catch that, dumbass. Try again."

def listen_offline(audio_data):
    model_path = "stormy_ai/vosk-model-small-en-us-0.15"
    if not os.path.exists(model_path):
        return "Offline model missing. Download vosk-model-small-en-us-0.15.zip and extract to stormy_ai/ folder."
    
    try:
        from vosk import Model, KaldiRecognizer
        model = Model(model_path)
        rec = KaldiRecognizer(model, 16000)
        
        import wave
        import io
        wav_bytes = io.BytesIO()
        with wave.open(wav_bytes, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(audio_data.get_wav_data(convert_rate=16000, convert_width=2))
        wav_bytes.seek(0)
        
        data = wav_bytes.read()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            print(f"You said (offline): {text}")
            return text.strip()
        return "Didn't catch that offline either."
    except Exception as e:
        return f"Offline failed: {str(e)}"
