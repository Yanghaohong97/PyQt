# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 425)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/<no prefix>/res/mmp_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("border-top-color:rgb(0, 0, 127);\n"
"background-color: rgb(207, 207, 207);")
        self.printTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.printTextBrowser.setGeometry(QtCore.QRect(10, 110, 701, 311))
        self.printTextBrowser.setTabletTracking(False)
        self.printTextBrowser.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:rgb(235, 235, 235);\n"
"font: 9pt \"Calibri\";\n"
"")
        self.printTextBrowser.setObjectName("printTextBrowser")
        self.sourcePathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.sourcePathLineEdit.setGeometry(QtCore.QRect(102, 10, 511, 21))
        self.sourcePathLineEdit.setStyleSheet("background-color:rgb(235, 235, 235);\n"
"font: 9pt \"Calibri\";")
        self.sourcePathLineEdit.setObjectName("sourcePathLineEdit")
        self.checkPushButton = QtWidgets.QPushButton(Dialog)
        self.checkPushButton.setGeometry(QtCore.QRect(630, 10, 75, 51))
        self.checkPushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 99, 255, 255), stop:0.551136 rgba(102, 61, 235, 255), stop:1 rgba(153, 154, 154, 255));\n"
"font: 14pt \"Calibri\";\n"
"")
        self.checkPushButton.setObjectName("checkPushButton")
        self.startPushButton = QtWidgets.QPushButton(Dialog)
        self.startPushButton.setGeometry(QtCore.QRect(10, 72, 341, 31))
        self.startPushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 99, 255, 255), stop:0.551136 rgba(102, 61, 235, 255), stop:1 rgba(153, 154, 154, 255));\n"
"font: 10pt \"Calibri\";\n"
"font: 14pt \"Calibri\";\n"
"")
        self.startPushButton.setAutoRepeatInterval(100)
        self.startPushButton.setObjectName("startPushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 99, 255, 255), stop:0.551136 rgba(102, 61, 235, 255), stop:0.977273 rgba(92, 102, 101, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 10pt \"Calibri\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 20))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 99, 255, 255), stop:0.551136 rgba(102, 61, 235, 255), stop:0.977273 rgba(92, 102, 101, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 10pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.backupPathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.backupPathLineEdit.setGeometry(QtCore.QRect(100, 40, 511, 21))
        self.backupPathLineEdit.setStyleSheet("background-color:rgb(235, 235, 235);\n"
"font: 10pt \"Calibri\";")
        self.backupPathLineEdit.setObjectName("backupPathLineEdit")
        self.stopPushButton = QtWidgets.QPushButton(Dialog)
        self.stopPushButton.setGeometry(QtCore.QRect(370, 72, 341, 31))
        self.stopPushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(82, 99, 255, 255), stop:0.551136 rgba(102, 61, 235, 255), stop:1 rgba(153, 154, 154, 255));\n"
"font: 14pt \"Calibri\";\n"
"")
        self.stopPushButton.setObjectName("stopPushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DMP自动部署"))
        self.sourcePathLineEdit.setText(_translate("Dialog", "D:\\WorkSpace\\Android_TV\\cvt_app\\multi_media_player_30\\app\\build\\outputs\\apk\\haier\\release\\"))
        self.checkPushButton.setText(_translate("Dialog", "Check"))
        self.startPushButton.setText(_translate("Dialog", "Start"))
        self.label.setText(_translate("Dialog", "ApkSourcePath:"))
        self.label_2.setText(_translate("Dialog", "ApkBackupPath:"))
        self.backupPathLineEdit.setText(_translate("Dialog", "D:\\"))
        self.stopPushButton.setText(_translate("Dialog", "Stop"))
import button_image_rc
