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


        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = self.CLIENT_ID,
                                                    client_secret = self.CLIENT_SECRET,
                                                    redirect_uri = "https://example.com",
                                                    scope="user-library-read"))
        self.songs_list = []
        # results = self.sp.current_user_saved_tracks()
        # for idx, item in enumerate(results['items']):
        #     track = item['track']
        #     print(idx, track['artists'][0]['name'], " – ", track['name'])
        #     print("\n")
        #     print(track['external_urls']["spotify"])
        #     print("\n\n\n")

            

    def search_a_song_URIs(self, time_line, song_name):
        year = time_line.split("-")[0]
        q = f"{song_name} year:{year}"
        # q = f"{song_name} "
        song_result = self.sp.search(q, limit=1, offset=0, type='track', market=None)
        song_URI = song_result["tracks"]["items"][0]['external_urls']["spotify"]
        song_URI = song_URI.split("/")[4]
        print(song_URI)
        return song_URI
        # print(song_result)
        # for song in song_result["tracks"]["items"]:
        #     print(song["external_urls"]["spotify"])
        #     # print(song["tracks"]["items"][0]['external_urls']["spotify"])
        #     # print(song['external_urls']["spotify"])
        #     print("\n\n\n")


    def create_playlist(self,timeline, songs_list):
        # Create playlist
        playlist = self.sp.user_playlist_create(self.CLIENT_ID, name = f"{timeline} BillBoard 100", public=True, collaborative=False, description=f'This playlist contains the first Hot 100 songs at {timeline}')
        print(playlist)
        playlist_id = playlist ["id"]
        
        # Search for the URL of each song in the Songs List 
        songs_list_URIs = []
        for song in songs_list:
            song_URI = self.search_a_song_URIs(time_line=timeline, song_name=song)    
            songs_list_URIs.append(song_URI)
            
        # Add all Songs URLs to the new playlist
        self.sp.playlist_add_items(playlist_id, songs_list_URIs, position=None)
     

spotify = Spotify()
spotify.search_a_song_URIs(song_name="Oklahoma", time_line= "2000-12-12")