#sShow
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to show picyures from fotoShoot

#V1 R2

#TODO:Close images!

import os
import time
import Image
import scanner
import frame

class sShow:
    
    def __init__(self):
        self.mainDir= '/'
        scan=scanner.scanner()
        self.picList=scan.scanDir(mainDir)
        self.pause=pause
        pass
        
    def getPic(self, pic):
		fImage = Image.open(pic)
		return fImage
        
    def showTime(self):
    
        scan=scanner.scanner()
        picList=scan.scanDir(self.mainDir)
            
        for index, pic in enumerate(picList):
            picDis = self.getPic(pic);
            picDis.show()
            time.sleep(pause)
                           
if __name__ == "__main__":
    pause=3
    mainDir = '.'
    SShow = sShow()

    #Start slide show
    SShow.showTime()
