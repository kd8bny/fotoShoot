# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Mar 25 21:16:53 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(496, 135)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 462, 99))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dirlabel = QtGui.QLabel(self.widget)
        self.dirlabel.setObjectName(_fromUtf8("dirlabel"))
        self.horizontalLayout.addWidget(self.dirlabel)
        self.picDir = QtGui.QLineEdit(self.widget)
        self.picDir.setObjectName(_fromUtf8("picDir"))
        self.horizontalLayout.addWidget(self.picDir)
        self.dirButton = QtGui.QPushButton(self.widget)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.horizontalLayout.addWidget(self.dirButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pauselabel = QtGui.QLabel(self.widget)
        self.pauselabel.setObjectName(_fromUtf8("pauselabel"))
        self.horizontalLayout_2.addWidget(self.pauselabel)
        self.spinBox = QtGui.QSpinBox(self.widget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.ssStart = QtGui.QPushButton(self.widget)
        self.ssStart.setObjectName(_fromUtf8("ssStart"))
        self.gridLayout.addWidget(self.ssStart, 2, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.dirlabel.setBuddy(self.picDir)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ssStart, QtCore.SIGNAL(_fromUtf8("clicked()")), self.picDir.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.picDir, self.dirButton)
        Form.setTabOrder(self.dirButton, self.ssStart)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.dirlabel.setText(_translate("Form", "Photo Directory", None))
        self.dirButton.setText(_translate("Form", "Browse", None))
        self.pauselabel.setText(_translate("Form", "Slide Duration", None))
        self.ssStart.setText(_translate("Form", "Start Slide Show", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

