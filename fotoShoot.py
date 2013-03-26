#Digital photo frame
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to change photos in a slideshow fashion --TODO:Port to RPi

#V1 R0

import sys

from PyQt4 import QtCore,QtGui
from main import Ui_Form

class fotoShoot(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
