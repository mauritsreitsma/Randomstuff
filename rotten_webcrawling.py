import urllib.request as urllib
from bs4 import BeautifulSoup
import numpy as np

file_data = np.loadtxt('oscar_data.txt', encoding="utf-8", delimiter=',     ', dtype=str)
years = file_data[1:, 0]
titles = file_data[1:, 3]

data= []

for n in range(1, len(years)):
    year = years[n]
    title = titles[n]
    title = title.lower()
    title = title.replace(" ", "_")
    title = title.replace("/", "_")
    title = title.replace("'", "")

    WEBSITE = 'http://disco-crawler-lab.tik.ee.ethz.ch/m/' + year + '/' + title

    try:
        response = urllib.urlopen(WEBSITE)
    except:
        print("website not found")
    else:
        page_source = response.read()

        soup = BeautifulSoup(page_source, 'html.parser')
        tomato = soup.find(class_="tomato-left")
        audience = soup.find(class_="audience-score meter")

        try:
            tomato_score = tomato.find(itemprop='ratingValue').text.strip() + '%'

        except:
            print("no tomato")
            tomato_score="none"
        try:
            audience_score = audience.find(itemprop='ratingValue').text.strip()
        except:
            print("no audience")
            audience_score = "none"

        genres = []
        for genre in soup.find_all(itemprop="genre"):
            genres.append(genre.text.strip())
        genres = '{'+", ".join(genres) + '}'

        runtime= soup.find(itemprop="duration").text.strip()

        data.append([year, title, tomato_score, audience_score, genres, runtime])

np.savetxt(fname='rotten.txt', X=data, fmt='%s', encoding="utf-8", delimiter='   ||   ')








