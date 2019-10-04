import urllib3
import os
from bs4 import BeautifulSoup

def enquote(string):
    return '"' + string + '"'

# variables
url = 'https://www.imdb.com/search/title/?title_type=feature&countries=id&adult=include&sort=release_date,asc&count=250&start='
key = '0'
tag = 'div'
identifier = 'mode-advanced'

# features
title = []
year = []
genre = []
imageLink = []
totalData = 2223
increment = 250

for i in range(1, totalData, increment):
    # initialize request
    http = urllib3.PoolManager()
    response = http.request('GET', url + str(int(key) + i))

    soup = BeautifulSoup(response.data, 'lxml') # transform to beautifulsoup type
    results = soup.findAll(tag, identifier)

    for result in results:
        title.append(result.find('h3', 'lister-item-header').a.text) # fix comma in title
        year.append(result.find('span', 'lister-item-year').text)
        # for values that maynot be available
        try:
            genre.append(result.find('span', 'genre').text.replace('\n', '').replace(' ', '')) # cleaning
            imageLink.append(result.find('img', 'loadlate')['loadlate'])
        except AttributeError:
            genre.append('')
            imageLink.append('')

        # data counter
        print(len(title), "/", totalData, "results found", end="\r")
        
# write data
fileName = 'dataset.csv'
data = list(zip(title, year, genre, imageLink))

with open(fileName, 'w') as file:
    for title, year, genre, imageLink in data[:-1]:
        print(enquote(title), year, enquote(genre), enquote(imageLink), sep = ',', end = '\n', file = file)
    title, year, genre, imageLink = data[-1]
    print(enquote(title), year, enquote(genre), enquote(imageLink), sep = ',', end = '', file = file)