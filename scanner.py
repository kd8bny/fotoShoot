#sShow
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to show picyures from fotoShoot

#V1 R1

import fnmatch
import string
import os

class scanner:

    def __init__(self,mainDir):
        self.mainDir = mainDir
        self.fileType = ['*.jpg', '*.jpeg', '*.png']
        self.picList = []
    
    def scanDir(self):
        for root, dirs, filenames in os.walk(self.mainDir):
            for extension in self.fileType:
                    for filename in fnmatch.filter(filenames, extension):
                            self.picList.append(os.path.join(root, filename))
        print self.picList
        return self.picList

if __name__ == "__main__":
    mainDir = '/home/daryl/Projects/fotoShoot'
    myscan=scanner(mainDir)
    myscan.scanDir()
