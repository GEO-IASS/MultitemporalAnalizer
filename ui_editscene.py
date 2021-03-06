# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editscene.ui'
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

class Ui_editScene(object):
    def setupUi(self, editScene):
        editScene.setObjectName(_fromUtf8("editScene"))
        editScene.resize(264, 322)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editScene.setWindowIcon(icon)
        self.gridLayoutWidget = QtGui.QWidget(editScene)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 273))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.basicData = QtGui.QGridLayout(self.gridLayoutWidget)
        self.basicData.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.basicData.setMargin(0)
        self.basicData.setObjectName(_fromUtf8("basicData"))
        self.minute = QtGui.QSpinBox(self.gridLayoutWidget)
        self.minute.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.minute.setMinimum(0)
        self.minute.setMaximum(59)
        self.minute.setProperty("value", 0)
        self.minute.setObjectName(_fromUtf8("minute"))
        self.basicData.addWidget(self.minute, 7, 1, 1, 1)
        self.label05 = QtGui.QLabel(self.gridLayoutWidget)
        self.label05.setObjectName(_fromUtf8("label05"))
        self.basicData.addWidget(self.label05, 4, 0, 1, 1)
        self.day = QtGui.QSpinBox(self.gridLayoutWidget)
        self.day.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.day.setMinimum(1)
        self.day.setMaximum(31)
        self.day.setProperty("value", 1)
        self.day.setObjectName(_fromUtf8("day"))
        self.basicData.addWidget(self.day, 5, 1, 1, 1)
        self.label07 = QtGui.QLabel(self.gridLayoutWidget)
        self.label07.setObjectName(_fromUtf8("label07"))
        self.basicData.addWidget(self.label07, 6, 0, 1, 1)
        self.month = QtGui.QSpinBox(self.gridLayoutWidget)
        self.month.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setProperty("value", 1)
        self.month.setObjectName(_fromUtf8("month"))
        self.basicData.addWidget(self.month, 4, 1, 1, 1)
        self.hour = QtGui.QSpinBox(self.gridLayoutWidget)
        self.hour.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.hour.setMinimum(0)
        self.hour.setMaximum(23)
        self.hour.setProperty("value", 0)
        self.hour.setObjectName(_fromUtf8("hour"))
        self.basicData.addWidget(self.hour, 6, 1, 1, 1)
        self.label02 = QtGui.QLabel(self.gridLayoutWidget)
        self.label02.setObjectName(_fromUtf8("label02"))
        self.basicData.addWidget(self.label02, 0, 0, 1, 2)
        self.label03 = QtGui.QLabel(self.gridLayoutWidget)
        self.label03.setObjectName(_fromUtf8("label03"))
        self.basicData.addWidget(self.label03, 2, 0, 1, 2)
        self.year = QtGui.QSpinBox(self.gridLayoutWidget)
        self.year.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.year.setMinimum(1900)
        self.year.setMaximum(2013)
        self.year.setProperty("value", 2013)
        self.year.setObjectName(_fromUtf8("year"))
        self.basicData.addWidget(self.year, 3, 1, 1, 1)
        self.label06 = QtGui.QLabel(self.gridLayoutWidget)
        self.label06.setObjectName(_fromUtf8("label06"))
        self.basicData.addWidget(self.label06, 5, 0, 1, 1)
        self.label04 = QtGui.QLabel(self.gridLayoutWidget)
        self.label04.setObjectName(_fromUtf8("label04"))
        self.basicData.addWidget(self.label04, 3, 0, 1, 1)
        self.label08 = QtGui.QLabel(self.gridLayoutWidget)
        self.label08.setObjectName(_fromUtf8("label08"))
        self.basicData.addWidget(self.label08, 7, 0, 1, 1)
        self.ID = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ID.setText(_fromUtf8(""))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.basicData.addWidget(self.ID, 1, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(editScene)
        self.buttonBox.setGeometry(QtCore.QRect(75, 290, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.button_remove = QtGui.QPushButton(editScene)
        self.button_remove.setGeometry(QtCore.QRect(218, 15, 31, 27))
        self.button_remove.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon1)
        self.button_remove.setObjectName(_fromUtf8("button_remove"))

        self.retranslateUi(editScene)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editScene.process)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editScene.reject)
        QtCore.QObject.connect(self.ID, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), editScene.editID)
        QtCore.QObject.connect(self.hour, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), editScene.editHour)
        QtCore.QObject.connect(self.day, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), editScene.editDay)
        QtCore.QObject.connect(self.month, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), editScene.editMonth)
        QtCore.QObject.connect(self.year, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), editScene.editYear)
        QtCore.QObject.connect(self.button_remove, QtCore.SIGNAL(_fromUtf8("clicked()")), editScene.delete)
        QtCore.QMetaObject.connectSlotsByName(editScene)

    def retranslateUi(self, editScene):
        editScene.setWindowTitle(_translate("editScene", "Edit scene", None))
        self.label05.setText(_translate("editScene", "Month", None))
        self.label07.setText(_translate("editScene", "Hour", None))
        self.label02.setText(_translate("editScene", "<html><head/><body><p><span style=\" font-weight:600;\">ID</span></p></body></html>", None))
        self.label03.setText(_translate("editScene", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>", None))
        self.label06.setText(_translate("editScene", "Day", None))
        self.label04.setText(_translate("editScene", "Year", None))
        self.label08.setText(_translate("editScene", "Minute", None))
        self.button_remove.setToolTip(_translate("editScene", "Remove Scene", None))
        self.button_remove.setStatusTip(_translate("editScene", "Remove Scene", None))
        self.button_remove.setWhatsThis(_translate("editScene", "Remove Scene", None))
        self.button_remove.setAccessibleName(_translate("editScene", "Remove Scene", None))

import icon_rc
