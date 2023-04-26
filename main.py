from bs4 import BeautifulSoup 
import requests

# music_year_selection = input("what year you would like to travel to in YYY-MM-DD format: ")
test_case_date = "2012-12-12"
music_year_selection = test_case_date
url = f"https://www.billboard.com/charts/hot-100/{music_year_selection}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

list_of_h3 = soup.select(selector="h3", id="title-of-a-story")
print(list_of_h3)
# for movie in list_of_h3:
#     print(movie.get_text())

def test_selection_music_date():
    test_case_date = "2012-12-12"
    # for testcasedate in test_cases_dates:
    url = f"https://www.billboard.com/charts/hot-100/{test_case_date}/"
        
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title.string)
    if soup.title.string == "Billboard Hot 100 – Billboard":
        return True
    return False

# print(test_selection_music_date())