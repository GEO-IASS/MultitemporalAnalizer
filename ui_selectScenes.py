# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selectScenes.ui'
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

class Ui_selectScenes(object):
    def setupUi(self, selectScenes):
        selectScenes.setObjectName(_fromUtf8("selectScenes"))
        selectScenes.resize(371, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectScenes.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(selectScenes)
        self.buttonBox.setGeometry(QtCore.QRect(170, 312, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listLayer = QtGui.QListWidget(selectScenes)
        self.listLayer.setGeometry(QtCore.QRect(10, 40, 351, 271))
        self.listLayer.setProperty("showDropIndicator", False)
        self.listLayer.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listLayer.setObjectName(_fromUtf8("listLayer"))
        self.button_remove = QtGui.QPushButton(selectScenes)
        self.button_remove.setGeometry(QtCore.QRect(210, 10, 31, 27))
        self.button_remove.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon1)
        self.button_remove.setObjectName(_fromUtf8("button_remove"))
        self.button_help = QtGui.QPushButton(selectScenes)
        self.button_help.setGeometry(QtCore.QRect(300, 10, 31, 27))
        self.button_help.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_help.setIcon(icon2)
        self.button_help.setObjectName(_fromUtf8("button_help"))
        self.button_aboutUs = QtGui.QPushButton(selectScenes)
        self.button_aboutUs.setGeometry(QtCore.QRect(330, 10, 31, 27))
        self.button_aboutUs.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/aboutUs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_aboutUs.setIcon(icon3)
        self.button_aboutUs.setObjectName(_fromUtf8("button_aboutUs"))
        self.button_add = QtGui.QPushButton(selectScenes)
        self.button_add.setGeometry(QtCore.QRect(180, 10, 31, 27))
        self.button_add.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon4)
        self.button_add.setObjectName(_fromUtf8("button_add"))
        self.label = QtGui.QLabel(selectScenes)
        self.label.setGeometry(QtCore.QRect(10, 16, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.button_open = QtGui.QPushButton(selectScenes)
        self.button_open.setGeometry(QtCore.QRect(240, 10, 31, 27))
        self.button_open.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_open.setIcon(icon5)
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.button_save = QtGui.QPushButton(selectScenes)
        self.button_save.setGeometry(QtCore.QRect(270, 10, 31, 27))
        self.button_save.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save.setIcon(icon6)
        self.button_save.setObjectName(_fromUtf8("button_save"))

        self.retranslateUi(selectScenes)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), selectScenes.process)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), selectScenes.reject)
        QtCore.QObject.connect(self.button_add, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.add)
        QtCore.QObject.connect(self.button_remove, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.remove)
        QtCore.QObject.connect(self.button_help, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.help)
        QtCore.QObject.connect(self.button_aboutUs, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.aboutUs)
        QtCore.QObject.connect(self.listLayer, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), selectScenes.edit)
        QtCore.QObject.connect(self.button_open, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.openList)
        QtCore.QObject.connect(self.button_save, QtCore.SIGNAL(_fromUtf8("clicked()")), selectScenes.saveList)
        QtCore.QMetaObject.connectSlotsByName(selectScenes)

    def retranslateUi(self, selectScenes):
        selectScenes.setWindowTitle(_translate("selectScenes", "Select Scenes", None))
        self.button_remove.setToolTip(_translate("selectScenes", "Remove Scene", None))
        self.button_remove.setStatusTip(_translate("selectScenes", "Remove Scene", None))
        self.button_remove.setWhatsThis(_translate("selectScenes", "Remove Scene", None))
        self.button_remove.setAccessibleName(_translate("selectScenes", "Remove Scene", None))
        self.button_help.setToolTip(_translate("selectScenes", "Help", None))
        self.button_help.setStatusTip(_translate("selectScenes", "Help", None))
        self.button_help.setWhatsThis(_translate("selectScenes", "Help", None))
        self.button_help.setAccessibleName(_translate("selectScenes", "Help", None))
        self.button_aboutUs.setToolTip(_translate("selectScenes", "About Us", None))
        self.button_aboutUs.setStatusTip(_translate("selectScenes", "About Us", None))
        self.button_aboutUs.setWhatsThis(_translate("selectScenes", "About Us", None))
        self.button_aboutUs.setAccessibleName(_translate("selectScenes", "About Us", None))
        self.button_add.setToolTip(_translate("selectScenes", "Add New Scene", None))
        self.button_add.setStatusTip(_translate("selectScenes", "Add New Scene", None))
        self.button_add.setWhatsThis(_translate("selectScenes", "Add New Scene", None))
        self.button_add.setAccessibleName(_translate("selectScenes", "Add New Scene", None))
        self.label.setText(_translate("selectScenes", "<html><head/><body><p><span style=\" font-weight:600;\">Select Scenes</span></p></body></html>", None))
        self.button_open.setToolTip(_translate("selectScenes", "Open Scene List", None))
        self.button_open.setStatusTip(_translate("selectScenes", "Open Scene List", None))
        self.button_open.setWhatsThis(_translate("selectScenes", "Open Scene List", None))
        self.button_open.setAccessibleName(_translate("selectScenes", "Open Scene List", None))
        self.button_save.setToolTip(_translate("selectScenes", "Save Scene List", None))
        self.button_save.setStatusTip(_translate("selectScenes", "Save Scene List", None))
        self.button_save.setWhatsThis(_translate("selectScenes", "Open Scene List", None))
        self.button_save.setAccessibleName(_translate("selectScenes", "Open Scene List", None))

import icon_rc
