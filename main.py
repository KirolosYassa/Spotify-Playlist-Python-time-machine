from bs4 import BeautifulSoup 
import requests
from spotify import *

isTestMode = True

if isTestMode:
    test_case_date = "2000-12-12"
    music_year_selection = test_case_date
else:
    music_year_selection = input("what year you would like to travel to in YYY-MM-DD format: ")
    
url = f"https://www.billboard.com/charts/hot-100/{music_year_selection}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div_of_music_song = soup.find_all("div", class_="o-chart-results-list-row-container")
songs_list = []
for movie_div in div_of_music_song:
    song_name = movie_div.find("h3", class_="c-title").text.replace("\t","").replace("\n","")
    songs_list.append(song_name)

# print(songs_list)
index = 1
for song in songs_list:
    print(f"{index}) {song}")
    index += 1
    
    
spotify = Spotify()
spotify.create_playlist(timeline = music_year_selection, songs_list= songs_list)

def test_selection_music_date():
    test_case_date = "2012-12-12"
    music_year_selection = test_case_date
    url = f"https://www.billboard.com/charts/hot-100/{music_year_selection}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    div_of_music_song = soup.find_all("div", class_="o-chart-results-list-row-container")
    songs_list = []
    for movie_div in div_of_music_song:
        song_name = movie_div.find("h3", class_="c-title").text.replace("\t","").replace("\n","")
        songs_list.append(song_name)

    print(songs_list)
    if len(songs_list) == 100:
        return True
    return False

# print(test_selection_music_date())