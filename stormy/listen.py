import speech_recognition as sr
import vosk  # we'll use as fallback if google fails
import json
import os

recognizer = sr.Recognizer()

def listen(timeout=5, phrase_time_limit=8) -> str:
    """Listen via microphone and return text. Tries online Google first, falls back to offline Vosk."""
    print("🎤 Stormy is listening... (speak now)")
    
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        
        # Try Google (online, more accurate)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.strip()
    
    except sr.UnknownValueError:
        print("Stormy: Couldn't understand you, dumbass. Trying offline...")
    except sr.RequestError:
        print("Stormy: No internet? Fine, using offline mode...")
    except Exception as e:
        print(f"Listen error: {e}")
    
    # Offline fallback with Vosk (needs model)
    return listen_offline(audio) if 'audio' in locals() else "Sorry, I didn't catch that."

def listen_offline(audio_data):
    # Download small English model once: https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    # Extract to stormy/vosk-model-small-en-us-0.15/
    model_path = "stormy/vosk-model-small-en-us-0.15"
    if not os.path.exists(model_path):
        return "Offline model not found. Download vosk-model-small-en-us-0.15 and put it in stormy/ folder."
    
    try:
        from vosk import Model, KaldiRecognizer
        model = Model(model_path)
        recognizer_vosk = KaldiRecognizer(model, 16000)
        
        # Convert audio to wav bytes for Vosk
        import wave
        import io
        wav_bytes = io.BytesIO()
        with wave.open(wav_bytes, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(audio_data.get_wav_data())
        wav_bytes.seek(0)
        
        data = wav_bytes.read()
        if recognizer_vosk.AcceptWaveform(data):
            result = json.loads(recognizer_vosk.Result())
            text = result.get("text", "")
            print(f"You said (offline): {text}")
            return text.strip()
        return "Didn't catch that offline either."
    except Exception as e:
        return f"Offline failed: {str(e)}"
