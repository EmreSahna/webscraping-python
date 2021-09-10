
import requests
from bs4 import BeautifulSoup

url_home = "https://www.imdb.com"
url = "https://www.imdb.com/trailers/?ref_=nv_mv_tr"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("div", {"class":"ipc-sub-grid ipc-sub-grid--page-span-3 ipc-sub-grid--wrap styles__TrailerGridContainer-sc-1gzxy7u-0 jLRktJ"}).find_all("div",{"class":"ipc-poster-card ipc-poster-card--baseAlt ipc-poster-card--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2"})

for i in list:
    title = i.find("a",{"class":"ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable"}).text
    link = i.find("a",{"class":"ipc-lockup-overlay ipc-focusable"}).get("href")
    complete_link = f"{url_home}{link}"
    print(f"Film Name: {title.ljust(50)} Trailer Link: {complete_link}")