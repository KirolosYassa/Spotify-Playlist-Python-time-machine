from bs4 import BeautifulSoup 
import requests

# music_year_selection = input("what year you would like to travel to in YYY-MM-DD format: ")
test_case_date = "2022-12-12"
music_year_selection = test_case_date
url = f"https://www.billboard.com/charts/hot-100/{music_year_selection}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div_of_music_song = soup.find_all("div", class_="o-chart-results-list-row-container")
song_list = []
for movie_div in div_of_music_song:
    song_name = movie_div.find("h3", class_="c-title").text.replace("\t","").replace("\n","")
    song_list.append(song_name)

print(song_list)

def test_selection_music_date():
    test_case_date = "2012-12-12"
    music_year_selection = test_case_date
    url = f"https://www.billboard.com/charts/hot-100/{music_year_selection}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    div_of_music_song = soup.find_all("div", class_="o-chart-results-list-row-container")
    song_list = []
    for movie_div in div_of_music_song:
        song_name = movie_div.find("h3", class_="c-title").text.replace("\t","").replace("\n","")
        song_list.append(song_name)

    print(song_list)
    if len(song_list) == 100:
        return True
    return False

# print(test_selection_music_date())