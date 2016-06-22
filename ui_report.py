# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report.ui'
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

class Ui_report(object):
    def setupUi(self, report):
        report.setObjectName(_fromUtf8("report"))
        report.resize(622, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        report.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(report)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 601, 561))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.button_save = QtGui.QPushButton(report)
        self.button_save.setGeometry(QtCore.QRect(550, 0, 31, 27))
        self.button_save.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save.setIcon(icon1)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.button_print = QtGui.QPushButton(report)
        self.button_print.setGeometry(QtCore.QRect(520, 0, 31, 27))
        self.button_print.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_print.setIcon(icon2)
        self.button_print.setObjectName(_fromUtf8("button_print"))
        self.label = QtGui.QLabel(report)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.button_aboutUs = QtGui.QPushButton(report)
        self.button_aboutUs.setGeometry(QtCore.QRect(580, 0, 31, 27))
        self.button_aboutUs.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/aboutUs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_aboutUs.setIcon(icon3)
        self.button_aboutUs.setObjectName(_fromUtf8("button_aboutUs"))

        self.retranslateUi(report)
        QtCore.QObject.connect(self.button_save, QtCore.SIGNAL(_fromUtf8("clicked()")), report.save)
        QtCore.QObject.connect(self.button_print, QtCore.SIGNAL(_fromUtf8("clicked()")), report.printReport)
        QtCore.QObject.connect(self.button_aboutUs, QtCore.SIGNAL(_fromUtf8("clicked()")), report.aboutUs)
        QtCore.QMetaObject.connectSlotsByName(report)

    def retranslateUi(self, report):
        report.setWindowTitle(_translate("report", "Report", None))
        self.textEdit.setHtml(_translate("report", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_save.setToolTip(_translate("report", "Save as PDF", None))
        self.button_save.setStatusTip(_translate("report", "Save as PDF", None))
        self.button_save.setWhatsThis(_translate("report", "Save as PDF", None))
        self.button_save.setAccessibleName(_translate("report", "Save as PDF", None))
        self.button_print.setToolTip(_translate("report", "Print", None))
        self.button_print.setStatusTip(_translate("report", "Print", None))
        self.button_print.setWhatsThis(_translate("report", "Print", None))
        self.button_print.setAccessibleName(_translate("report", "Print", None))
        self.label.setText(_translate("report", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Multitemporal Analysis Report</span></p></body></html>", None))
        self.button_aboutUs.setToolTip(_translate("report", "About Us", None))
        self.button_aboutUs.setStatusTip(_translate("report", "About Us", None))
        self.button_aboutUs.setWhatsThis(_translate("report", "About Us", None))
        self.button_aboutUs.setAccessibleName(_translate("report", "About Us", None))

import icon_rc
