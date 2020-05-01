import urllib.request as urllib
from bs4 import BeautifulSoup
import numpy as np

WEBSITE = 'http://disco-crawler-lab.tik.ee.ethz.ch/academyawardnominees/'

response = urllib.urlopen(WEBSITE)
page_source = response.read()

soup = BeautifulSoup(page_source, 'html.parser')

rows = soup.find_all('tr')
file_data = []

for row in rows:
    file_data. append([row.contents[3].contents[0], row.contents[5].contents[0], row.contents[7].contents[0],
                       row.contents[9].contents[0], row.contents[11].contents[0], row.contents[13].contents[0]])

np.savetxt(fname='oscar_data.txt', X=file_data, fmt='%s', encoding="utf-8", delimiter=',     ')




