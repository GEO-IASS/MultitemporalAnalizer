# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_help3.ui'
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

class Ui_help3(object):
    def setupUi(self, help3):
        help3.setObjectName(_fromUtf8("help3"))
        help3.resize(312, 212)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help3.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(help3)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 311, 211))
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(help3)
        QtCore.QMetaObject.connectSlotsByName(help3)

    def retranslateUi(self, help3):
        help3.setWindowTitle(_translate("help3", "Help", None))
        self.textEdit.setHtml(_translate("help3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Press the first tab (All Scenes) to see the variation of the surface area of the land cover over time.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/multitemporalanalyzer/screenshot/selectTab_report1.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">The other tabs expose the land cover information at each time point studied.</span></p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <img src=\":/plugins/multitemporalanalyzer/icon/statistic.png\" width=\"15\" /> to get a written report of the multitemporal analysis. This report can be printed <img src=\":/plugins/multitemporalanalyzer/icon/print.png\" width=\"15\" /> or saved as pdf <img src=\":/plugins/multitemporalanalyzer/icon/save.png\" width=\"15\" />.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <img src=\":/plugins/multitemporalanalyzer/icon/icon.png\" width=\"15\" /> to a new multitemporal analysis.</p></body></html>", None))

import icon_rc
import screenshot_rc
