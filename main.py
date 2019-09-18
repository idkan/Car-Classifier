import numpy as np
import os 
import re
import PIL
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import keras
from keras.utils import to_categorical
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU



dirName = os.path.join(os.getcwd(), 'assets\\media\\car_data\\train')
imgPath = dirName + os.sep

images = []
directories = []
directoriesCount = []
prevRoot = ''
count = 0

for root, dirnames, filenames in os.walk(imgPath):
    for filename in filenames:
        if re.search("\.(jpg|JPEG|jpeg|png|bmp|tiff)$",filename):
            filePath = os.path.join(root, filename)
            image = plt.imread(filePath)
            images.append(image)
            count += 1

    if prevRoot != root :
        print(root,count)
        prevRoot = root
        directories.append(root)
        directoriesCount.append(count)
        count = 0
directoriesCount.append(count)

directoriesCount = directoriesCount[1:]
print(f'Directorios leidos: {len(directories)}')
print(f'Imagenes en directorios: {directoriesCount}')
print(f'Imagenes totales: {sum(directoriesCount)}')


labels = []
index = 0

for count in directoriesCount:
    for i in range(count):
        labels.append(index)
        index += 1
print(f'Etiquedas creadas: {len(labels)}')

marcas = []
index = 0
for directory in directories:
    name = directory.split(os.sep)
    print(index, name[len(name)-1])
    marcas.append(name[len(name)-1])
    index += 1

y = np.array(labels)
x = np.array(images, dtype=np.unit8)

classes = np.unique(y)
nClasses = len(classes)
print(f'Total de etiquetas: {nClasses}')
print(f'Asignación de etiquetas: {classes}')
