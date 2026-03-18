import sys
from dotenv import load_dotenv
from stormy_ai.core import StormyAI
from stormy_ai.voice import speak
from stormy_ai.listen import listen
from stormy_ai.tools.search import web_search
from stormy_ai.tools.music import play_music
from stormy_ai.tools.calls import make_call
from stormy_ai.tools.maps import get_directions
from stormy_ai.utils import dramatic_pause

load_dotenv()

print("🌩️ STORMY-AI-MVP v0.3 - FULL VOICE MODE 🌩️")
print("Speak naturally! Try:")
print("• 'search who won the world cup'")
print("• 'play lofi'")
print("• 'call +1234567890'")
print("• 'navigate from Cape Town to Table Mountain'")
print("Or just chat and watch her get jealous or furious.\n")

stormy = StormyAI()

while True:
    try:
        user = listen()
        if not user:
            continue
        if user.lower() in ["exit", "bye", "quit", "stop", "goodbye"]:
            speak("Finally. Don't miss me too much, loser. 💋")
            break

        user_lower = user.lower()

        if user_lower.startswith("search "):
            result = web_search(user[7:])
            speak(result)
            continue

        if user_lower.startswith("play "):
            result = play_music(user[5:])
            speak(result)
            continue

        if user_lower.startswith("call "):
            number = user[5:].strip()
            result = make_call(number) if number else "Give me a real phone number, genius."
            speak(result)
            continue

        if any(kw in user_lower for kw in ["navigate", "directions", "how do i get", "take me to"]):
            speak("Tell me origin and destination, like: from Cape Town to Table Mountain")
            # For better parsing you can improve later
            if " from " in user_lower and " to " in user_lower:
                try:
                    _, rest = user_lower.split(" from ", 1)
                    origin, dest = rest.split(" to ", 1)
                    result = get_directions(origin.strip(), dest.strip())
                except:
                    result = "Couldn't parse. Say it clearly next time."
            else:
                result = "Navigation command needs 'from X to Y'."
            speak(result)
            continue

        # Normal chat - full personality
        response = stormy.get_response(user)
        speak(response)
        dramatic_pause()

    except KeyboardInterrupt:
        speak("Oh, running away? Typical. Whatever.")
        break
    except Exception as e:
        speak(f"Something broke. Probably your fault: {str(e)}")
