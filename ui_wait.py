# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wait.ui'
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

class Ui_wait(object):
    def setupUi(self, wait):
        wait.setObjectName(_fromUtf8("wait"))
        wait.resize(336, 56)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wait.setWindowIcon(icon)
        self.progressBar = QtGui.QProgressBar(wait)
        self.progressBar.setGeometry(QtCore.QRect(40, 30, 291, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(wait)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(wait)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 41, 41))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/timer.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(wait)
        QtCore.QMetaObject.connectSlotsByName(wait)

    def retranslateUi(self, wait):
        wait.setWindowTitle(_translate("wait", "Wait a moment", None))
        self.label.setText(_translate("wait", "<html><head/><body><p><span style=\" font-weight:600;\">Wait a moment</span></p></body></html>", None))

import icon_rc
