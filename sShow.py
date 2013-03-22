#Digital photo frame
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to change photos in a slideshow fashion --TODO:Port to RPi

#V1 R0

#TODO:Close images!

class sShow(QMainWindow, main.Ui_Ui_Form):
        import os
        import time
        import Image
        import fnmatch
        import string

        def scanDir():
                picList = []
                for root, dirs, filenames in os.walk(mainDir):
                        for extension in fileType:
                                for filename in fnmatch.filter(filenames, extension):
                                        picList.append(os.path.join(root, filename))
                return picList


        def getPic(pic):
                fImage = Image.open(pic)
                return fImage
        
        def showTime():
                for index, pic in enumerate(picList):
                        picDis = getPic(pic);
                        picDis.show()
                        time.sleep(pause)
                    
        
        if __name__ == "__main__":
                mainDir = '.'
                fileType = ['*.jpg', '*.jpeg', '*.png']
                pause = 3 #in secs

                picList = scanDir()
        
                #Start slide show
                showTime()
