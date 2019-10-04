from google_images_download import google_images_download
import pandas as pd
import numpy as np

# load into dataframe
columnName = ['Movie', 'Year', 'Genre', 'Poster Link']
moviedf = pd.read_csv('final_dataset.csv', sep = ',', header = None, names = columnName, index_col = None)

replacedValue = 'https://m.media-amazon.com/images/G/01/imdb/images/nopicture/67x98/film-2500266839._CB470041825_.png'
replaceValue = np.nan

moviedf = moviedf.replace(to_replace = replacedValue, value = replaceValue) # clean broken poster
movienp = moviedf.to_numpy()

flagsdf = pd.read_csv('flags.csv', sep = ',', header = None, index_col = None)
flagsnp = flagsdf.to_numpy()

print('Dataset statistics', moviedf.count(), sep = '\n')
data = list(zip(movienp[:, 0], flagsnp))

response = google_images_download.googleimagesdownload()

newFlag = []
counterSuccess = 0

for counter, [name, flag] in enumerate(data):
    if(flag == False):
        arguments = {"keywords" : '"' + name + ' film"',
                    "limit" : 1,
                    "print_urls" : True,
                    "format" : "jpg",
                    "no_directory" : True,
                    "aspect_ratio" : "tall",
                    "output_directory" : "Posters2/",
                    "prefix" : str(counter + 1) + " " + name + "-unnapproved",
                    "no_numbering" : True,
                    "silent_mode" : True}
        path = response.download(arguments)
        newFlag.append(True)
        counterSuccess = counterSuccess + 1
    else:
        newFlag.append(flag)

    counter = counter + 1
    print('Scraped images :', counter, '/', flagsnp.shape, 'Success :', counterSuccess, '-', counter - counterSuccess)

with open('newFlags.txt', 'w') as flags:
    for f in newFlag[:-1]:
        flags.write(str(f) + '\n')
    flags.write(str(f[-1]))