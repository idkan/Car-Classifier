import numpy
import os, sys
import PIL
from PIL import Image

class Curator(object):

    def __init__(self, directory, resizeFactor):

        self.directory = directory
        self.resizeFactor = resizeFactor

    def mapDir(self):

        mappedPaths, images = [], []

        for path, subdir, files in os.walk(self.directory):
            mappedPaths.append(path)
            


        mappedPaths.pop(0) 

        print(mappedPaths)

        for path in mappedPaths:     

            try:
                os.makedirs(path + '_resized')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            for paths, subdirs, files in os.walk(path):
                for image in files:
                    images.append("\\" + str(image))

            print(images)

            for image in images:

                #Resize
                self.resizeImg(path, image, self.resizeFactor)
                #Grayscale
                #self.grayScale(files)


        
        
    def resizeImg(self, originalPath, myFile, resizeFactor):

        basewidth = resizeFactor

        outfile = originalPath + "_resized" + str(myFile)
        try:
            im = Image.open(str(originalPath) + myFile)
            wpercent = (basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))

            im = im.resize((basewidth,hsize), Image.ANTIALIAS)
            
            im.save(outfile, "JPEG", optimize = True)

        except IOError:
            print ("cannot resize '%s'" % myFile)


    def curate(self):

        self.mapDir()

        return 0



def main():

    datasetCurator = Curator("./assets/media/car_data/train", 300)

    print(datasetCurator.curate())


if __name__ == '__main__':

    main()