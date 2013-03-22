# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Mar 18 17:04:34 2013
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
        Form.resize(614, 422)
        self.ssStart = QtGui.QPushButton(Form)
        self.ssStart.setGeometry(QtCore.QRect(250, 380, 121, 27))
        self.ssStart.setObjectName(_fromUtf8("ssStart"))
        self.picDir = QtGui.QLineEdit(Form)
        self.picDir.setGeometry(QtCore.QRect(160, 160, 113, 27))
        self.picDir.setObjectName(_fromUtf8("picDir"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 220, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.dirlabel = QtGui.QLabel(Form)
        self.dirlabel.setGeometry(QtCore.QRect(40, 160, 111, 17))
        self.dirlabel.setObjectName(_fromUtf8("dirlabel"))
        self.pauselabel = QtGui.QLabel(Form)
        self.pauselabel.setGeometry(QtCore.QRect(50, 230, 101, 17))
        self.pauselabel.setObjectName(_fromUtf8("pauselabel"))
        self.dirButton = QtGui.QPushButton(Form)
        self.dirButton.setGeometry(QtCore.QRect(300, 160, 98, 27))
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.dirlabel.setBuddy(self.picDir)
        self.pauselabel.setBuddy(self.lineEdit)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ssStart, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.copy)
        QtCore.QObject.connect(self.ssStart, QtCore.SIGNAL(_fromUtf8("clicked()")), self.picDir.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.picDir, self.dirButton)
        Form.setTabOrder(self.dirButton, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.ssStart)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ssStart.setText(_translate("Form", "Start Slide Show", None))
        self.dirlabel.setText(_translate("Form", "Photo Directory", None))
        self.pauselabel.setText(_translate("Form", "Slide Duration", None))
        self.dirButton.setText(_translate("Form", "Browse", None))
