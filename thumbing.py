import numpy
import os, sys
import errno
import PIL
from PIL import Image


class thumber(object):

    def __init__(self, root, savedir, factor):

        self.root = root
        self.savedir = savedir
        self.factor = factor

    def squareFiles(self): 

        paths, subdirs, imgfiles = [], [], []

        for path, subdir, files in os.walk(self.root):
            paths.append(path)
            subdirs.append(subdir)
            imgfiles.append(files)

        subdirs = subdirs[0] #Sólo guarda la primera posición
        paths.pop(0) #Elimina directorio root 
        imgfiles.pop(0) #Same here pero con imágenes

        for subdir in subdirs:

            newDir = self.savedir + str(subdir)

            try:
                os.makedirs(newDir)
            except OSError as e:
                if e.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else:
                    print("couldn't write directory F...")
                    raise      

        print("Directories succesfully created")

        for i in range(len(paths)):

            for img in imgfiles[i]:

                oldImgPath = str(paths[i]) + "/" + img
                newImgPath = self.savedir + subdirs[i] + "/" + img

                try:
                    oldIm = Image.open(oldImgPath)
                    newIm = oldIm.resize((self.factor, self.factor), Image.ANTIALIAS)
                    newIm.save(newImgPath, "JPEG", optimize = True)
                
                except IOError:
                    print ("error rezising '%s'" % str(img))


            percentage = (100/len(paths) ) * i
            print("%.5f percent completed" %percentage) 

def main():

    thumbnails = thumber("./assets/media/car_data/train/", "./assets/media/car_data/TrainOpti100/", 100)

    thumbnails.squareFiles()


if __name__ == '__main__':

    main()