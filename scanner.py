#sShow
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to show picyures from fotoShoot

#V1 R0

import fnmatch
import string
import os

class scanner:

    def __init__(self):
        self.fileType = ['*.jpg', '*.jpeg', '*.png']
        self.picList = []
    
    def scanDir(self,mainDir):
        for root, dirs, filenames in os.walk(mainDir):
            for extension in self.fileType:
                    for filename in fnmatch.filter(filenames, extension):
                            self.picList.append(os.path.join(root, filename))
        return self.picList

if __name__ == "__main__":
    myscan=scanner()
    mainDir = '.'
    fileType = ['*.jpg', '*.jpeg', '*.png']
    myscan.scanDir(mainDir)
