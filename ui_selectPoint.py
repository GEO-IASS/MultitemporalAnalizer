# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selectPoint.ui'
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

class Ui_selectPoint(object):
    def setupUi(self, selectPoint):
        selectPoint.setObjectName(_fromUtf8("selectPoint"))
        selectPoint.resize(441, 392)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectPoint.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(selectPoint)
        self.buttonBox.setGeometry(QtCore.QRect(250, 360, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(selectPoint)
        self.label.setGeometry(QtCore.QRect(10, 0, 431, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pointX = QtGui.QDoubleSpinBox(selectPoint)
        self.pointX.setGeometry(QtCore.QRect(90, 27, 121, 27))
        self.pointX.setPrefix(_fromUtf8(""))
        self.pointX.setSingleStep(1.0)
        self.pointX.setObjectName(_fromUtf8("pointX"))
        self.label3 = QtGui.QLabel(selectPoint)
        self.label3.setGeometry(QtCore.QRect(80, 30, 16, 21))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.pointY = QtGui.QDoubleSpinBox(selectPoint)
        self.pointY.setGeometry(QtCore.QRect(240, 26, 121, 27))
        self.pointY.setPrefix(_fromUtf8(""))
        self.pointY.setSingleStep(1.0)
        self.pointY.setObjectName(_fromUtf8("pointY"))
        self.label4 = QtGui.QLabel(selectPoint)
        self.label4.setGeometry(QtCore.QRect(230, 30, 16, 21))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.buttonHelp = QtGui.QPushButton(selectPoint)
        self.buttonHelp.setGeometry(QtCore.QRect(10, 360, 31, 27))
        self.buttonHelp.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHelp.setIcon(icon1)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.scene = QtGui.QLabel(selectPoint)
        self.scene.setGeometry(QtCore.QRect(10, 60, 421, 221))
        self.scene.setAlignment(QtCore.Qt.AlignCenter)
        self.scene.setWordWrap(False)
        self.scene.setObjectName(_fromUtf8("scene"))
        self.line = QtGui.QFrame(selectPoint)
        self.line.setGeometry(QtCore.QRect(10, 280, 421, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(selectPoint)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 431, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(selectPoint)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 320, 421, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.radioButtons = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.radioButtons.setMargin(0)
        self.radioButtons.setObjectName(_fromUtf8("radioButtons"))
        self.yesButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.radioButtons.addWidget(self.yesButton)
        self.noButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.noButton.setObjectName(_fromUtf8("noButton"))
        self.radioButtons.addWidget(self.noButton)
        self.line_2 = QtGui.QFrame(selectPoint)
        self.line_2.setGeometry(QtCore.QRect(190, 320, 20, 31))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(selectPoint)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), selectPoint.process)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), selectPoint.reject)
        QtCore.QObject.connect(self.buttonHelp, QtCore.SIGNAL(_fromUtf8("clicked()")), selectPoint.help)
        QtCore.QObject.connect(self.pointX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), selectPoint.setPoint)
        QtCore.QObject.connect(self.pointY, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), selectPoint.setPoint)
        QtCore.QMetaObject.connectSlotsByName(selectPoint)

    def retranslateUi(self, selectPoint):
        selectPoint.setWindowTitle(_translate("selectPoint", "Select a geographical point", None))
        self.label.setText(_translate("selectPoint", "<html><head/><body><p><span style=\" font-weight:600;\">Select a geographic point of the land cover</span></p></body></html>", None))
        self.label3.setText(_translate("selectPoint", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X</span></p></body></html>", None))
        self.label4.setText(_translate("selectPoint", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y</span></p></body></html>", None))
        self.buttonHelp.setToolTip(_translate("selectPoint", "Help", None))
        self.buttonHelp.setStatusTip(_translate("selectPoint", "Help", None))
        self.buttonHelp.setWhatsThis(_translate("selectPoint", "Help", None))
        self.scene.setText(_translate("selectPoint", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_3.setText(_translate("selectPoint", "<html><head/><body><p><span style=\" font-weight:600;\">Each cover has a unique color?</span></p></body></html>", None))
        self.yesButton.setText(_translate("selectPoint", "Yes", None))
        self.noButton.setText(_translate("selectPoint", "No", None))

import icon_rc
