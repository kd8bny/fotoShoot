#Digital photo frame
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to change photos in a slideshow fashion --TODO:Port to RPi

#V1 R1

import sys
import os
import sShow

from PyQt4 import *
from main import *

class fotoShoot(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
	    #Set signals
        QtCore.QObject.connect(self.ui.dirButton, QtCore.SIGNAL("clicked()"), self.browse)	#browse button
        QtCore.QObject.connect(self.ui.ssStart, QtCore.SIGNAL("clicked()"), self.start)	#start button
        QtCore.QObject.connect(self.ui.picDir, QtCore.SIGNAL("copy()"), self.Dir)
        #QtCore.QObject.connect(self.ui.dirButton, QtCore.SIGNAL("clicked()"), self.browse)
        
    def Dir(self):
    	pass
    	
    def start(self):
		pass
		
    def browse(self):
    	mainDir = QtGui.QFileDialog.getExistingDirectory(self)
    	self.ui.picDir.setText(mainDir)
	


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = fotoShoot()
    myapp.show()
    sys.exit(app.exec_())
