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
	def __init__(self,mainDir,pause):
		self.mainDir = mainDir
		scanInt = scanner.scanner(self.mainDir)
		self.picList = scanInt.scanDir()
		self.pause = pause
		
	def getPic(self, pic):
		fImage = Image.open(pic)
		return fImage
        
	def showTime(self):
		for index, pic in enumerate(self.picList):
			picDis = self.getPic(pic)
			picDis.show()
			time.sleep(pause)
                           
if __name__ == "__main__":
    pause=3
    mainDir = '.'
    SShow = sShow(mainDir,pause)

    #Start slide show
    SShow.showTime()
