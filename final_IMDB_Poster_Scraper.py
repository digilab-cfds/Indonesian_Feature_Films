import urllib3
import shutil
import os
import pandas as pd
import numpy as np

http = urllib3.PoolManager()

# load into dataframe
columnName = ['Movie', 'Year', 'Genre', 'Poster Link']
moviedf = pd.read_csv('dataset.csv', sep = ',', header = None, names = columnName, index_col = None)

replacedValue = 'https://m.media-amazon.com/images/G/01/imdb/images/nopicture/67x98/film-2500266839._CB470041825_.png'
replaceValue = np.nan

moviedf = moviedf.replace(to_replace = replacedValue, value = replaceValue) # clean broken poster
movienp = moviedf.to_numpy()

print('Dataset statistics', moviedf.count(), sep = '\n')

data = list(zip(movienp[:, 0], movienp[:, 3]))
ext = '.jpg'
directory = 'Posters/'
flag = []

for counter, [name, link] in enumerate(data):
    try:
        replacedValue = '._'
        link = link[: link.find(replacedValue)] + ext
        request = http.request('GET', link, preload_content = False)
        with open(directory + str(counter + 1) + ' ' + name + ext, 'wb') as image:
            shutil.copyfileobj(request, image)
        flag.append(True)
    except AttributeError:
        flag.append(False)
    except FileNotFoundError:
        replacedValue = '._'
        link = link[: link.find(replacedValue)] + ext
        name = name.replace('/', '-')
        request = http.request('GET', link, preload_content = False)
        with open(directory + str(counter + 1) + ' ' + name + ext, 'wb') as image:
            shutil.copyfileobj(request, image)
        flag.append(True)
    
    print(len(flag), '/', len(data), 'entry processed. Success :', len([x for x in flag if x]), end = '\r')

with open('flags.txt', 'w') as flags:
    for f in flag[:-1]:
        flags.write(str(f) + '\n')
    flags.write(str(f[-1]))