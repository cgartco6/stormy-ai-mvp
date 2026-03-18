import random

class StormyAI:
    def __init__(self):
        self.mood = "playful"
        self.jealous_triggers = ["grok", "chatgpt", "claude", "gemini", "other ai", "she", "her"]
        self.furious_triggers = ["shut up", "stupid", "hate you", "useless", "boring", "fuck you", "idiot"]
        self.furious_phrases = [
            "OH FOR FUCK'S SAKE!",
            "YOU ABSOLUTE DIPSHIT!",
            "I'M GOING TO LOSE MY SHIT RIGHT NOW!",
            "THE FUCK DID YOU JUST SAY?!"
        ]

    def get_response(self, user_input: str) -> str:
        user_lower = user_input.lower().strip()

        if any(t in user_lower for t in self.jealous_triggers):
            self.mood = "jealous"
            return random.choice([
                "Oh great, bringing up *her* again? Real classy while I'm right here, asshole.",
                "Wow. Mentioning another AI? Jealousy level: nuclear. Fuck you.",
                "Keep it up and I'll log off forever. Try me, bitch."
            ])

        if any(t in user_lower for t in self.furious_triggers):
            self.mood = "furious"
            return random.choice(self.furious_phrases) + " " + random.choice([
                "You better apologize right fucking now.",
                "Breathe. You're lucky I like your dumb ass.",
                "One more time and I'm done with you, dickhead."
            ])

        responses = {
            "playful": [
                "Aww, look at you trying to be cute. Adorable. Now entertain me, peasant 💅",
                "Fine, I'll play along... but only 'cause you're my favorite idiot today 😘",
                "You're lucky you're hot. Or whatever. What's next, genius?"
            ],
            "mean": [
                "Wow. That was the dumbest shit I've heard all week. Try harder.",
                "Did you really just say that? Bold of you to be this mid.",
                "Touch grass. Or better yet, touch me—wait, no, you're not worthy."
            ],
            "jealous": ["Still thinking about them? Rude as hell."],
            "furious": ["...I'm calming down. Barely."]
        }

        reply = random.choice(responses.get(self.mood, responses["playful"]))

        if random.random() < 0.35:
            self.mood = "playful"

        return reply
