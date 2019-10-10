import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold = sys.maxsize)

def group(numpy):
    result = []
    result.append(numpy[0].tolist())
    pointer = numpy[0,0]
    counter = 0

    for val in numpy[1:]:
        print(val[0], pointer)
        if(val[0] == pointer):
            result[counter][1].extend(val[1])
        else:
            result.append(val.tolist())
            pointer = val[0]
            counter += 1

    return result

fileName = 'final_dataset.csv'
columnNames = ['Movie Name', 'Year', 'Genre', 'Image Link']

dataframe = pd.read_csv(fileName, delimiter = ',', names = columnNames, index_col = False)
dataframe = dataframe[['Year', 'Genre']]

# Cleaning
dataframe['Year'].replace(to_replace = r'[\s(IV)X]', value = '', regex = True, inplace = True)
dataframe['Year'].replace(to_replace = r'^\s*$', value = np.nan, regex = True, inplace = True)
dataframe.dropna(how = 'any', inplace = True) # remove records with NA values

dataframe.reset_index(drop = True, inplace = True)

outputName = 'newDataset.xlsx'
dataframe.to_excel(outputName, engine = 'xlsxwriter')

numpy = dataframe.to_numpy()

print('Unique Years : ', np.unique(numpy[:, 0]))

genres = []
for genre in numpy[:, 1]:
    genres.extend(str(genre).split(','))

print('Unique Genre : ', np.unique(genres))

for i in range(len(numpy[:, 1])):
    numpy[i, 1] = str(numpy[i, 1]).split(',')

print(count(group(numpy)))