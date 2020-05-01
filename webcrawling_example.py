import urllib.request as urllib
from bs4 import BeautifulSoup

# variables
WEBSITE = 'http://disco-crawler-lab.tik.ee.ethz.ch/academyawardnominees/'

# read source code
response = urllib.urlopen(WEBSITE)
page_source = response.read()

# parse source code and save it
soup = BeautifulSoup(page_source, 'html.parser')
table_id = soup.find(id='table')
tag = soup.find('tbody')
a = tag.get_text()
liste_1 = a.split('\n')
length = len(liste_1)
counter_1 = 0
counter_2 = 1
while counter_1 < length:
    if liste_1[counter_1] == '':
        liste_1.pop(counter_1)
        length -= 1
    elif liste_1[counter_1] == str(counter_2):
        liste_1.pop(counter_1)
        length -= 1
        counter_2 += 1
    else:
        counter_1 += 1

length_2 = len(liste_1)
counter = 0;
with open('info1.csv', 'w') as f:
    while counter < length_2:
        a = (liste_1[counter], '; ', liste_1[counter + 1], '; ', liste_1[counter + 2], '; ', liste_1[counter + 3], '; ',
             liste_1[counter + 4], '; ', liste_1[counter + 5], '\n')
        counter += 6
        f.writelines(a)
