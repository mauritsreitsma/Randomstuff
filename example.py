import urllib.request as urllib
from bs4 import BeautifulSoup

# variables
WEBSITE = 'https://www.google.ch/'

# read source code
response = urllib.urlopen(WEBSITE)
page_source = response.read()

# parse source code and print it
soup = BeautifulSoup(page_source, 'html.parser')
print(soup.prettify())
