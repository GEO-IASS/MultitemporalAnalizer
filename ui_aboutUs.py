# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_aboutUs.ui'
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

class Ui_aboutUs(object):
    def setupUi(self, aboutUs):
        aboutUs.setObjectName(_fromUtf8("aboutUs"))
        aboutUs.resize(332, 638)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutUs.setWindowIcon(icon)
        self.meTitle = QtGui.QLabel(aboutUs)
        self.meTitle.setGeometry(QtCore.QRect(10, 10, 371, 17))
        self.meTitle.setObjectName(_fromUtf8("meTitle"))
        self.meInfo = QtGui.QLabel(aboutUs)
        self.meInfo.setGeometry(QtCore.QRect(100, 20, 151, 101))
        self.meInfo.setObjectName(_fromUtf8("meInfo"))
        self.mePicture = QtGui.QLabel(aboutUs)
        self.mePicture.setGeometry(QtCore.QRect(20, 37, 71, 71))
        self.mePicture.setText(_fromUtf8(""))
        self.mePicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/arturo.jpg")))
        self.mePicture.setScaledContents(True)
        self.mePicture.setWordWrap(False)
        self.mePicture.setObjectName(_fromUtf8("mePicture"))
        self.supportTitle = QtGui.QLabel(aboutUs)
        self.supportTitle.setGeometry(QtCore.QRect(10, 120, 221, 20))
        self.supportTitle.setObjectName(_fromUtf8("supportTitle"))
        self.pedroPicture = QtGui.QLabel(aboutUs)
        self.pedroPicture.setGeometry(QtCore.QRect(20, 150, 71, 71))
        self.pedroPicture.setText(_fromUtf8(""))
        self.pedroPicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/pedro.jpg")))
        self.pedroPicture.setScaledContents(True)
        self.pedroPicture.setWordWrap(False)
        self.pedroPicture.setObjectName(_fromUtf8("pedroPicture"))
        self.rafaelPicture = QtGui.QLabel(aboutUs)
        self.rafaelPicture.setGeometry(QtCore.QRect(20, 230, 71, 71))
        self.rafaelPicture.setText(_fromUtf8(""))
        self.rafaelPicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/rafael.jpg")))
        self.rafaelPicture.setScaledContents(True)
        self.rafaelPicture.setWordWrap(False)
        self.rafaelPicture.setObjectName(_fromUtf8("rafaelPicture"))
        self.pedroInfo = QtGui.QLabel(aboutUs)
        self.pedroInfo.setGeometry(QtCore.QRect(100, 135, 151, 101))
        self.pedroInfo.setObjectName(_fromUtf8("pedroInfo"))
        self.rafaelInfo = QtGui.QLabel(aboutUs)
        self.rafaelInfo.setGeometry(QtCore.QRect(100, 217, 171, 101))
        self.rafaelInfo.setObjectName(_fromUtf8("rafaelInfo"))
        self.facytlInfo = QtGui.QLabel(aboutUs)
        self.facytlInfo.setGeometry(QtCore.QRect(100, 410, 171, 81))
        self.facytlInfo.setObjectName(_fromUtf8("facytlInfo"))
        self.facytPicture = QtGui.QLabel(aboutUs)
        self.facytPicture.setGeometry(QtCore.QRect(10, 420, 81, 61))
        self.facytPicture.setText(_fromUtf8(""))
        self.facytPicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/LogoFacyt.png")))
        self.facytPicture.setScaledContents(True)
        self.facytPicture.setWordWrap(False)
        self.facytPicture.setObjectName(_fromUtf8("facytPicture"))
        self.ucInfo = QtGui.QLabel(aboutUs)
        self.ucInfo.setGeometry(QtCore.QRect(100, 320, 231, 81))
        self.ucInfo.setObjectName(_fromUtf8("ucInfo"))
        self.ucPicture = QtGui.QLabel(aboutUs)
        self.ucPicture.setGeometry(QtCore.QRect(20, 330, 61, 71))
        self.ucPicture.setText(_fromUtf8(""))
        self.ucPicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/log_uc.png")))
        self.ucPicture.setScaledContents(True)
        self.ucPicture.setWordWrap(False)
        self.ucPicture.setObjectName(_fromUtf8("ucPicture"))
        self.cemviccPicture = QtGui.QLabel(aboutUs)
        self.cemviccPicture.setGeometry(QtCore.QRect(20, 510, 71, 51))
        self.cemviccPicture.setText(_fromUtf8(""))
        self.cemviccPicture.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/image/cemvicc.jpg")))
        self.cemviccPicture.setScaledContents(True)
        self.cemviccPicture.setWordWrap(False)
        self.cemviccPicture.setObjectName(_fromUtf8("cemviccPicture"))
        self.cemviccInfo = QtGui.QLabel(aboutUs)
        self.cemviccInfo.setGeometry(QtCore.QRect(100, 490, 221, 101))
        self.cemviccInfo.setObjectName(_fromUtf8("cemviccInfo"))
        self.pushButton = QtGui.QPushButton(aboutUs)
        self.pushButton.setGeometry(QtCore.QRect(10, 596, 311, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(aboutUs)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), aboutUs.degreeThesis)
        QtCore.QMetaObject.connectSlotsByName(aboutUs)

    def retranslateUi(self, aboutUs):
        aboutUs.setWindowTitle(_translate("aboutUs", "About Us", None))
        self.meTitle.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-weight:600;\">Manager/Developer</span></p></body></html>", None))
        self.meInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Arturo Mendoza</span></p><p><span style=\" font-size:9pt;\">arturo.amb89@gmail.com</span></p><p><span style=\" font-size:9pt;\">@MrTuro</span></p></body></html>", None))
        self.supportTitle.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-weight:600;\">Academic Support</span></p></body></html>", None))
        self.pedroInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Pedro Linares</span></p><p><span style=\" font-size:9pt;\">plinaresherrera@gmail.com</span></p><p><span style=\" font-size:9pt;\">@plinaresherrera</span></p></body></html>", None))
        self.rafaelInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Rafael Rodríguez</span></p><p><span style=\" font-size:9pt;\">rafaaltamiranda@yahoo.com</span></p><p><span style=\" font-size:9pt;\">@...</span></p></body></html>", None))
        self.facytlInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">FaCyT</span></p><p><span style=\" font-size:9pt;\">Faculty of Science &amp; Technology</span></p><p><span style=\" font-size:9pt;\">facyt.uc.edu.ve</span></p></body></html>", None))
        self.ucInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Universidad of Carabobo</span></p><p><span style=\" font-size:9pt;\">www.uc.edu.ve</span></p><p><span style=\" font-size:9pt;\">Venezuela</span></p></body></html>", None))
        self.cemviccInfo.setText(_translate("aboutUs", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">CEMVIC</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">2</span></p><p><span style=\" font-size:9pt;\">Multidisciplinary center of visualization</span></p><p><span style=\" font-size:9pt;\">and computing scientific</span></p></body></html>", None))
        self.pushButton.setText(_translate("aboutUs", "Open degree thesis (PDF - Spanish)", None))

import icon_rc
import image_rc
