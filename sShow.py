#sShow
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to show picyures from fotoShoot

#V1 R1

#TODO:Close images!

import os
import time
import Image
import scanner

class sShow:
    
    def __init__(self,mainDir):
        scan=scanner.scanner()
        self.picList=scan.scanDir(mainDir)
        self.pause=3
        
    def getPic(self,pic):
            fImage = Image.open(pic)
            return fImage
        
    def showTime(self,pause):
            for index, pic in enumerate(self.picList):
                    picDis = self.getPic(pic);
                    picDis.show()
                    time.sleep(self.git pause)
                           
if __name__ == "__main__":
    pause=3
    mainDir = '.'
    SShow=sShow(mainDir)

    #Start slide show
    SShow.showTime(pause)
