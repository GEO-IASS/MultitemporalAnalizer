# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_crossroad.ui'
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

class Ui_crossroad(object):
    def setupUi(self, crossroad):
        crossroad.setObjectName(_fromUtf8("crossroad"))
        crossroad.resize(426, 265)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        crossroad.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(crossroad)
        self.buttonBox.setGeometry(QtCore.QRect(240, 230, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(crossroad)
        self.label.setGeometry(QtCore.QRect(30, 10, 391, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(crossroad)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/arrows.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(crossroad)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 381, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayoutWidget = QtGui.QWidget(crossroad)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 411, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.LayerLists = QtGui.QGridLayout(self.gridLayoutWidget)
        self.LayerLists.setMargin(0)
        self.LayerLists.setObjectName(_fromUtf8("LayerLists"))
        self.list2 = QtGui.QListWidget(self.gridLayoutWidget)
        self.list2.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.list2.setObjectName(_fromUtf8("list2"))
        self.LayerLists.addWidget(self.list2, 1, 1, 1, 1)
        self.list1 = QtGui.QListWidget(self.gridLayoutWidget)
        self.list1.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.list1.setObjectName(_fromUtf8("list1"))
        self.LayerLists.addWidget(self.list1, 0, 1, 1, 1)
        self.buttonList1 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.buttonList1.setText(_fromUtf8(""))
        self.buttonList1.setObjectName(_fromUtf8("buttonList1"))
        self.LayerLists.addWidget(self.buttonList1, 0, 0, 1, 1)
        self.buttonList2 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.buttonList2.setText(_fromUtf8(""))
        self.buttonList2.setObjectName(_fromUtf8("buttonList2"))
        self.LayerLists.addWidget(self.buttonList2, 1, 0, 1, 1)
        self.buttonHelp = QtGui.QPushButton(crossroad)
        self.buttonHelp.setGeometry(QtCore.QRect(10, 230, 31, 27))
        self.buttonHelp.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHelp.setIcon(icon1)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))

        self.retranslateUi(crossroad)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), crossroad.process)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), crossroad.reject)
        QtCore.QObject.connect(self.list1, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.buttonList1.toggle)
        QtCore.QObject.connect(self.list2, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.buttonList2.toggle)
        QtCore.QObject.connect(self.buttonHelp, QtCore.SIGNAL(_fromUtf8("clicked()")), crossroad.help)
        QtCore.QMetaObject.connectSlotsByName(crossroad)

    def retranslateUi(self, crossroad):
        crossroad.setWindowTitle(_translate("crossroad", "Crossroad", None))
        self.label.setText(_translate("crossroad", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">This scene doesn\'t have a valid geographical area</span></p></body></html>", None))
        self.label_3.setText(_translate("crossroad", "<html><head/><body><p>Which do layer list you want to continue?</p></body></html>", None))
        self.buttonHelp.setToolTip(_translate("crossroad", "Help", None))
        self.buttonHelp.setStatusTip(_translate("crossroad", "Help", None))
        self.buttonHelp.setWhatsThis(_translate("crossroad", "Help", None))

import icon_rc
