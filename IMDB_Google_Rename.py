import os

def checkASCII(i):
    i = ord(i)

    if i < 123 and i > 96:
        return True
    elif i < 91 and i > 64:
        return True
    elif i < 58 and i > 47:
        return True
    elif i == 32 or i == 46 or i == 45:
        return True
    else:
        return False

dir = 'Posters2/'
dirlist = os.listdir(dir)

for image in dirlist:
    try:
        keyword = '-unnapproved'
        newImage = image[:image.find(keyword)] + '.jpg'
        newImage = ''.join([i if checkASCII(i) else '' for i in newImage])
        print(newImage)
        os.rename(os.path.join(dir + image), os.path.join(dir + newImage))
    except FileNotFoundError:
        keyword = '-unnapproved'
        newImage = image[:image.find(keyword)] + '.jpg'
        newImage = ''.join([i if checkASCII(i) else '' for i in newImage])
        print(newImage)

        newImage = ''.join([i if checkASCII(i) else '' for i in newImage])
        os.rename(os.path.join(dir + image), os.path.join(dir + newImage))