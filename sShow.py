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
    
    def __init__(self):
        self.pause=3
        fotoScan=scanner.scanner()
        self.picList=fotoScan.scanDir()
        
    def getPic(self,pic):
            fImage = Image.open(pic)
            return fImage
        
    def showTime(self):
            for index, pic in enumerate(picList):
                    picDis = self.getPic(pic);
                    picDis.show()
                    time.sleep(pause)
                           
if __name__ == "__main__":
    SShow=sShow()

    #Start slide show
    SShow.showTime(picList)
        
    
