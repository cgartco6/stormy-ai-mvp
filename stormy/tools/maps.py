import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

def get_directions(origin: str, destination: str):
    if not os.getenv("GOOGLE_MAPS_API_KEY"):
        return "No Google Maps key. Guess you'll stay lost, loser."

    try:
        directions = gmaps.directions(origin, destination, mode="driving")
        if directions:
            route = directions[0]['legs'][0]
            return f"From {origin} to {destination}: {route['distance']['text']} in {route['duration']['text']}. " \
                   f"Main instruction: {route['steps'][0]['html_instructions']}"
        return "No route found. Maybe don't go there."
    except Exception as e:
        return f"Maps failed: {str(e)}"
