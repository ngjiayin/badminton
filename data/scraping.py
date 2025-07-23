import requests
from bs4 import BeautifulSoup

url = "https://www.badmintonstatistics.net/Tournament?tournamentid=YONEXAllEnglandOpe2025f7f"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# initial attempt: tournament is specified
print(soup)
