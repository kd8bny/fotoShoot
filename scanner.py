#sShow
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to show picyures from fotoShoot

#V1 R0

import fnmatch
import string
import os

class scanner(mainDir):
    
    def scanDir():
        picList = []
        for root, dirs, filenames in os.walk(mainDir):
            for extension in fileType:
                    for filename in fnmatch.filter(filenames, extension):
                            picList.append(os.path.join(root, filename))
        return picList

    if __name__ == "__main__":
        picList = scanDir()
        
