import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class Spotify:
    
    def __init__(self):
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = self.CLIENT_ID,
                                                    client_secret = self.CLIENT_SECRET,
                                                    redirect_uri = "https://example.com",
                                                    scope="user-library-read"))

        results = sp.current_user_saved_tracks(limit=1)
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
            print(idx, item)
            

    def search_a_song(self):
        url = "https://api.spotify.com/v1/search"
        
        access_token = self.CLIENT_ID
        search_params = {
            "q": "track:Marboot Be Astek",
            "type": "track",
            "market": "ES",
            "limit": 1,
            
        }
        headers = {
            "client_id": self.CLIENT_ID
        }
        response = requests.get(url=url, headers=headers, params= search_params)
        print(response.json())
        
        



    def create_playlist(self):
        
        url = "https://api.spotify.com/v1/users/{user_id}/playlists"
        
                

spotify = Spotify()
spotify.search_a_song()