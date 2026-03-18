import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

def play_music(query: str = "lofi"):
    # This is a stub - full playback needs a running Spotify client + token
    print(f"🎵 Stormy would play '{query}' on Spotify right now...")
    # Example full code would use sp.start_playback() after auth
    return f"Playing some {query} for you, babe. Don't say I never do anything nice."
