# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_result.ui'
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

class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName(_fromUtf8("result"))
        result.setEnabled(True)
        result.resize(841, 429)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        result.setWindowIcon(icon)
        result.setSizeGripEnabled(False)
        self.title = QtGui.QLabel(result)
        self.title.setGeometry(QtCore.QRect(50, 10, 221, 31))
        self.title.setObjectName(_fromUtf8("title"))
        self.logo = QtGui.QLabel(result)
        self.logo.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.tabWidget = QtGui.QTabWidget(result)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 821, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.allScenes = QtGui.QWidget()
        self.allScenes.setObjectName(_fromUtf8("allScenes"))
        self.scenesList = QtGui.QListWidget(self.allScenes)
        self.scenesList.setGeometry(QtCore.QRect(0, 0, 141, 338))
        self.scenesList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.scenesList.setObjectName(_fromUtf8("scenesList"))
        self.graphic = QtGui.QLabel(self.allScenes)
        self.graphic.setGeometry(QtCore.QRect(140, 0, 681, 341))
        self.graphic.setText(_fromUtf8(""))
        self.graphic.setScaledContents(True)
        self.graphic.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.graphic.setObjectName(_fromUtf8("graphic"))
        self.tabWidget.addTab(self.allScenes, _fromUtf8(""))
        self.button_help = QtGui.QPushButton(result)
        self.button_help.setGeometry(QtCore.QRect(770, 10, 31, 27))
        self.button_help.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_help.setIcon(icon1)
        self.button_help.setObjectName(_fromUtf8("button_help"))
        self.button_aboutUs = QtGui.QPushButton(result)
        self.button_aboutUs.setGeometry(QtCore.QRect(800, 10, 31, 27))
        self.button_aboutUs.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/aboutUs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_aboutUs.setIcon(icon2)
        self.button_aboutUs.setObjectName(_fromUtf8("button_aboutUs"))
        self.button_report = QtGui.QPushButton(result)
        self.button_report.setGeometry(QtCore.QRect(740, 10, 31, 27))
        self.button_report.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/statistic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_report.setIcon(icon3)
        self.button_report.setObjectName(_fromUtf8("button_report"))
        self.button_new = QtGui.QPushButton(result)
        self.button_new.setGeometry(QtCore.QRect(710, 10, 31, 27))
        self.button_new.setText(_fromUtf8(""))
        self.button_new.setIcon(icon)
        self.button_new.setObjectName(_fromUtf8("button_new"))

        self.retranslateUi(result)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.scenesList, QtCore.SIGNAL(_fromUtf8("itemActivated(QListWidgetItem*)")), result.setTab)
        QtCore.QObject.connect(self.button_aboutUs, QtCore.SIGNAL(_fromUtf8("clicked()")), result.aboutUs)
        QtCore.QObject.connect(self.button_help, QtCore.SIGNAL(_fromUtf8("clicked()")), result.help)
        QtCore.QObject.connect(self.button_new, QtCore.SIGNAL(_fromUtf8("clicked()")), result.new)
        QtCore.QObject.connect(self.button_report, QtCore.SIGNAL(_fromUtf8("clicked()")), result.report)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        result.setWindowTitle(_translate("result", "Result", None))
        self.title.setText(_translate("result", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Multitemporal Analyzer</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.allScenes), _translate("result", "All Scenes", None))
        self.button_help.setToolTip(_translate("result", "Help", None))
        self.button_help.setStatusTip(_translate("result", "Help", None))
        self.button_help.setWhatsThis(_translate("result", "Help", None))
        self.button_help.setAccessibleName(_translate("result", "Help", None))
        self.button_aboutUs.setToolTip(_translate("result", "About Us", None))
        self.button_aboutUs.setStatusTip(_translate("result", "About Us", None))
        self.button_aboutUs.setWhatsThis(_translate("result", "About Us", None))
        self.button_aboutUs.setAccessibleName(_translate("result", "About Us", None))
        self.button_report.setToolTip(_translate("result", "Get report", None))
        self.button_report.setStatusTip(_translate("result", "Get report", None))
        self.button_report.setWhatsThis(_translate("result", "Get report", None))
        self.button_report.setAccessibleName(_translate("result", "Get report", None))
        self.button_new.setToolTip(_translate("result", "Get a new analysis", None))
        self.button_new.setStatusTip(_translate("result", "Get a new analysis", None))
        self.button_new.setWhatsThis(_translate("result", "Get a new analysis", None))
        self.button_new.setAccessibleName(_translate("result", "Get a new analysis", None))

import icon_rc
