import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY")) if os.getenv("GOOGLE_MAPS_API_KEY") else None

def get_directions(origin: str, destination: str):
    if not gmaps:
        return "No Google Maps key in .env. You're on your own, lost soul."
    try:
        directions = gmaps.directions(origin, destination, mode="driving")
        if directions:
            leg = directions[0]['legs'][0]
            return f"From {origin} to {destination}: {leg['distance']['text']} • {leg['duration']['text']}. First step: {leg['steps'][0]['html_instructions']}"
        return "No route found. Bad destination?"
    except Exception as e:
        return f"Maps error: {str(e)}"
