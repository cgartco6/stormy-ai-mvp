import sys
from dotenv import load_dotenv
from stormy.core import Stormy
from stormy.voice import speak
from stormy.tools.search import web_search
from stormy.tools.music import play_music
from stormy.tools.calls import make_call
from stormy.tools.maps import get_directions
from stormy.utils import dramatic_pause

load_dotenv()

print("🌩️ STORMY MVP v0.2 - Voice Edition 🌩️")
print("Say 'exit' or 'bye' to quit. Be nice... or don't. I dare you.\n")

stormy = Stormy()

while True:
    try:
        user = input("You: ").strip()
        if user.lower() in ["exit", "bye", "quit"]:
            speak("Finally. Don't miss me too much, loser. 💋")
            break

        # Special commands
        if user.lower().startswith("search "):
            query = user[7:]
            result = web_search(query)
            speak(result)
            continue

        if user.lower().startswith("play "):
            song = user[5:]
            result = play_music(song)
            speak(result)
            continue

        if user.lower().startswith("call "):
            # Simple: call +1234567890
            number = user[5:].strip()
            result = make_call(number, "Stormy wants to talk to you!")
            speak(result)
            continue

        if user.lower().startswith("navigate ") or user.lower().startswith("directions "):
            # Example: navigate from Cape Town to Table Mountain
            parts = user.split(" from ", 1)
            if len(parts) > 1:
                origin, dest = parts[1].split(" to ", 1)
                result = get_directions(origin.strip(), dest.strip())
            else:
                result = "Format: navigate from [place] to [place]"
            speak(result)
            continue

        # Normal conversation
        response = stormy.get_response(user)
        speak(response)
        dramatic_pause()

    except KeyboardInterrupt:
        speak("Oh, running away? Typical. Whatever.")
        break
    except Exception as e:
        speak(f"Something broke. Probably your fault: {str(e)}")
