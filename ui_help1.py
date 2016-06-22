# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_help1.ui'
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

class Ui_help1(object):
    def setupUi(self, help1):
        help1.setObjectName(_fromUtf8("help1"))
        help1.resize(312, 242)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/multitemporalanalyzer/icon/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help1.setWindowIcon(icon)
        self.txt = QtGui.QTextEdit(help1)
        self.txt.setGeometry(QtCore.QRect(0, 0, 312, 242))
        self.txt.setAcceptDrops(False)
        self.txt.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.txt.setObjectName(_fromUtf8("txt"))

        self.retranslateUi(help1)
        QtCore.QMetaObject.connectSlotsByName(help1)

    def retranslateUi(self, help1):
        help1.setWindowTitle(_translate("help1", "Help", None))
        self.txt.setHtml(_translate("help1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <img src=\":/plugins/multitemporalanalyzer/icon/add.png\" width=\"15\" /> to add a scene.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press OK to start the analysis.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/multitemporalanalyzer/screenshot/pressOk.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For the execution of the plugin should be added (at least) two scenes. All escenes should to represent a geographical area in common and can have neither the same ID, and the same date.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To delete a scene must select it...</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/multitemporalanalyzer/screenshot/selectScenes2.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">..and press <img src=\":/plugins/multitemporalanalyzer/icon/remove.png\" width=\"15\" />.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To delete all scenes, press <img src=\":/plugins/multitemporalanalyzer/icon/remove.png\" width=\"15\" /> without selecting any scene. It will show a warning message, where you have to accept.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/multitemporalanalyzer/screenshot/removeAllScenes.png\" width=\"250\" /></p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Double click on a scene to edit its ID and date.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/multitemporalanalyzer/screenshot/edit.png\" width=\"250\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you press <img src=\":/plugins/multitemporalanalyzer/icon/remove.png\" width=\"15\" /> (in the editing window) the scene will be eliminated.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <img src=\":/plugins/multitemporalanalyzer/icon/save.png\" width=\"15\" /> to save the scenes list (in a file) for a later analysis.</p>\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press <img src=\":/plugins/multitemporalanalyzer/icon/open.png\" width=\"15\" /> to load a list of scenes from a file.</p></body></html>", None))

import icon_rc
import screenshot_rc
