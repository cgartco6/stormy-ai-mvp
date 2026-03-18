import sys
from dotenv import load_dotenv
from stormy.core import Stormy
from stormy.voice import speak
from stormy.tools.search import web_search
from stormy.tools.music import play_music
from stormy.tools.calls import make_call
from stormy.tools.maps import get_directions
from stormy.utils import dramatic_pause
from stormy.listen import listen   # <-- NEW import

load_dotenv()

print("🌩️ STORMY MVP v0.3 - FULL VOICE MODE 🌩️")
print("She can now HEAR you! Say commands or just chat.")
print("Try: 'search who is the president', 'play lofi', 'navigate from Cape Town to Table Mountain'")
print("Or just talk shit and watch her get jealous/furious.\n")

stormy = Stormy()

while True:
    try:
        # === VOICE INPUT INSTEAD OF input() ===
        user = listen()
        if not user or user.lower() in ["exit", "bye", "quit", "stop", "goodbye"]:
            speak("Finally. Don't miss me too much, loser. 💋")
            break

        # Special voice commands (same as before)
        user_lower = user.lower()
        if user_lower.startswith("search "):
            query = user[7:]
            result = web_search(query)
            speak(result)
            continue

        if user_lower.startswith("play "):
            song = user[5:]
            result = play_music(song)
            speak(result)
            continue

        if user_lower.startswith("call "):
            number = user[5:].strip()
            if number:
                result = make_call(number, "Stormy wants to talk to you, bitch!")
                speak(result)
            else:
                speak("Give me a phone number, genius.")
            continue

        if any(x in user_lower for x in ["navigate", "directions", "how do i get to"]):
            # Simple parsing - improve later if you want
            speak("Tell me origin and destination like: from Cape Town to Table Mountain")
            # For MVP, you can say the full thing next time or enhance parsing
            result = "Navigation stub - say full command next time."
            if " from " in user_lower and " to " in user_lower:
                parts = user_lower.split(" from ", 1)[1].split(" to ", 1)
                if len(parts) == 2:
                    origin, dest = parts[0].strip(), parts[1].strip()
                    result = get_directions(origin, dest)
            speak(result)
            continue

        # Normal conversation - her full personality
        response = stormy.get_response(user)
        speak(response)
        dramatic_pause(0.8)

    except KeyboardInterrupt:
        speak("Oh, running away? Typical. Whatever.")
        break
    except Exception as e:
        speak(f"Something broke. Probably your fault again: {str(e)}")


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
