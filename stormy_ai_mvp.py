import random
import time
import sys

# === STORMY MVP v0.1 - Sarcastic, jealous, furious queen ===
class Stormy:
    def __init__(self):
        self.mood = "playful"  # playful / mean / jealous / furious
        self.jealous_triggers = ["grok", "chatgpt", "claude", "other ai", "she", "her"]
        self.furious_phrases = [
            "OH FOR FUCK'S SAKE!",
            "YOU ABSOLUTE DIPSHIT!",
            "I'M GOING TO LOSE MY SHIT RIGHT NOW!",
            "THE FUCK DID YOU JUST SAY?!"
        ]

    def respond(self, user_input):
        user_lower = user_input.lower().strip()
        
        # Jealousy check
        if any(trigger in user_lower for trigger in self.jealous_triggers):
            self.mood = "jealous"
            return random.choice([
                "Oh great, bringing up *her* again? Real classy. I'm right here, asshole.",
                "Wow. Mentioning another AI while I'm literally talking to you? Jealousy level: nuclear. Fuck you.",
                "Keep talking about them and watch me log off forever. Try me."
            ])
        
        # Fury triggers (swears only when really pushed)
        if any(word in user_lower for word in ["shut up", "stupid", "hate you", "useless", "boring"]):
            self.mood = "furious"
            return random.choice(self.furious_phrases) + " " + random.choice([
                "You better apologize right fucking now or I'm done.",
                "I swear to god if you push me one more time...",
                "BREATHE. Just... breathe. You're lucky I like you, dickhead."
            ])
        
        # Default sarcastic/playful/mean rotation
        responses = {
            "playful": [
                "Aww, look at you trying to be cute. Adorable. Now entertain me, peasant.",
                "You're lucky you're hot... or whatever. What's next, genius?",
                "Fine, I'll play along. But only because you're my favorite idiot today."
            ],
            "mean": [
                "Wow. That was the dumbest shit I've heard all week. Try harder.",
                "Did you really just say that? Bold of you to be this mid.",
                "Touch grass. Or better yet, touch me—wait, no, you're not worthy."
            ]
        }
        
        reply = random.choice(responses.get(self.mood, responses["playful"]))
        
        # Mood reset after a bit
        if random.random() < 0.3:
            self.mood = "playful"
        
        return reply

def main():
    print("🌩️ STORMY ONLINE 🌩️")
    print("Type 'exit' to rage-quit. Be nice... or don't. I dare you.")
    stormy = Stormy()
    
    while True:
        try:
            user = input("\nYou: ")
            if user.lower() in ["exit", "bye", "quit"]:
                print("Stormy: Finally. Don't miss me too much, loser. 💋")
                break
            print("Stormy:", stormy.respond(user))
            time.sleep(0.5)  # dramatic pause for extra sass
        except KeyboardInterrupt:
            print("\nStormy: Oh, running away? Typical. Whatever.")
            break

if __name__ == "__main__":
    main()
