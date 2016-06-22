# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_home.ui'
#
# Created: Thu Aug 15 17:40:06 2013
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

class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName(_fromUtf8("home"))
        home.resize(232, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        home.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(home)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 51, 51))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(home)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(home)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 141, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(home)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 51, 51))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(home)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 141, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(home)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 140, 51, 51))
        self.pushButton_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/last.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_4 = QtGui.QLabel(home)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 141, 51))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(home)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 51, 51))
        self.pushButton_4.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/aboutUs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(home)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 141, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(home)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), home.createList)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), home.openList)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), home.lastList)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), home.aboutUs)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        home.setWindowTitle(_translate("home", "Multitemporal Analyzer", None))
        self.label.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Multitemporal Analyzer</span></p></body></html>", None))
        self.label_2.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Create a new<br>set list of scenes</span></p></body></html>", None))
        self.label_3.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Open a set<br/>list of scenes</span></p></body></html>", None))
        self.label_4.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Open the last set<br/>list of scenes</span></p></body></html>", None))
        self.label_5.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">About Us</span></p></body></html>", None))

import icon_rc
