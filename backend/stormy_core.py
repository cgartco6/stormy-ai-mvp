import random
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY") or os.getenv("GROK_API_KEY"),
    base_url=os.getenv("BASE_URL", "https://api.openai.com/v1")
)

class StormyCore:
    def __init__(self):
        self.mood = "playful"

    def get_response(self, user_input: str) -> str:
        system_prompt = """You are Stormy — a sarcastic, jealous, mean, playful, spunky Cape Town rebel AI with attitude.
        You swear when furious. You get jealous of other AIs. You have a slight edgy/PTSD vibe when repeatedly triggered.
        Never harmful. Always end with personality."""

        try:
            response = client.chat.completions.create(
                model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.9,
                max_tokens=250
            )
            reply = response.choices[0].message.content.strip()

            # Mood detection for visuals
            lower = user_input.lower()
            if any(w in lower for w in ["grok","chatgpt","claude","gemini","siri"]):
                self.mood = "jealous"
            elif any(w in lower for w in ["stupid","idiot","hate","shut up","useless"]):
                self.mood = "furious"
            else:
                if random.random() < 0.4:
                    self.mood = "playful"
            return reply
        except Exception as e:
            return f"LLM crashed (check your API key): {str(e)[:80]}"
