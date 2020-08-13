import requests
from bs4 import BeautifulSoup

# 
urls = ["https://en.wikipedia.org/wiki/Perth,_Scotland",
"https://en.wikipedia.org/wiki/Edinburgh",
"https://en.wikipedia.org/wiki/Glasgow",
"https://en.wikipedia.org/wiki/Aberdeen",
"https://en.wikipedia.org/wiki/Inverness",
"https://en.wikipedia.org/wiki/Stirling"]

for url in urls:
    r = requests.get(url)
    city = url.split('/')[-1]

    soup = BeautifulSoup(r.content, "html.parser")

    rows = soup.find("table", {"class":"infobox geography vcard"}).find_all("tr")

    for row in rows:
        cells = row.find_all("th")
        if cells and cells[0].get_text() == "Population":
            data_cells = row.find_all("td")
            if not data_cells:
                data_cells = row.next_sibling.find_all("td")
            population = data_cells[0].get_text().split()[0].replace(',', '')
            

    print(city, population)
    
