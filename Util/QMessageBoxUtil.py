# -*- coding: utf-8 -*-
""""
Copyright (C) 2017 CVTE

@ 版权所有：Yanghaohong©版权所有
@ 文件名：$safeitemname$
@ 文件功能描述：
@ 创建日期：2021/7/3 11:38
@ 创建人：Yanghaohong
@ 修改标识：2021/7/6 19:37
@ 修改描述：
@ 修改日期：
@ 修改版本：V1.0.0
"""
import sys

from PyQt5.QtGui import QTextCursor

import AutoUpdateDMPApk
import QtUi
import Util

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Common import filesManager
from Util.fileControl import getNewestApkName


def showWindow():
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())


def appendMsgToTextBrowser(str):
    myWin = MyMainForm()
    myWin.__appendMsgToTextBrowser(MyMainForm(), str)


def checkAndAddBackslashToPath(path):
    retPath = path
    if path[-1] != "\\":
        retPath = path + "\\"
    return retPath


class MyMainForm(QMainWindow, QtUi.Ui_Dialog):
    stop_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.checkPushButton.clicked.connect(self.check)
        self.startPushButton.clicked.connect(self.start)
        self.startPushButton.setEnabled(False)

        # Thread:
        self.thread = QThread()
        self.worker = AutoUpdateDMPApk.Worker()
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread

        self.worker.printfSignal.connect(self.printf)  # 连接回调
        self.worker.showSuccessSignal.connect(self.showSuccessDialg)  # 连接回调

        self.thread.started.connect(self.worker.do_work)
        # self.thread.finished.connect(self.worker.stop)

        # Start Button action:
        self.startPushButton.clicked.connect(self.thread.start)


        # Stop Button action:
        self.stopPushButton.clicked.connect(self.stop_thread)

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        self.stop_signal.emit()  # emit the finished signal on stop

    def showSuccessDialg(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.Ok)

    def showSpecialMessage(self, title, message):
        QMessageBox.information(title, message, QMessageBox.Ok)

    def showMsg(self):
        QMessageBox.information(self, '信息提示对话框', '前方右拐到达目的地', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QMessageBox.question(self, "提问对话框", "你要继续搞测试吗？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.warning(self, "警告对话框", "继续执行会导致系统重启，你确定要继续？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.critical(self, "严重错误对话框", "数组越界，程序异常退出", QMessageBox.Yes | QMessageBox.No, )
        QMessageBox.about(self, "关于对话框", "你的Windows系统是DOS1.0")

    def check(self):
        self.printf("\n ----------------------Check Start------------------")
        self.printf("start check path.")
        isSourceApkExist = False
        isBackupApkExist = False
        if self.sourcePathLineEdit.text():
            sourceApkPath = self.sourcePathLineEdit.text()
            self.printf(str(len(sourceApkPath)))
            sourceApkPath = checkAndAddBackslashToPath(sourceApkPath)
            self.printf(str(len(sourceApkPath)))
            print(getNewestApkName())
            sourceApkPath = sourceApkPath + Util.fileControl.getNewestApkName()
            self.printf("ApkSourcePath:" + sourceApkPath)
            if filesManager.isFileExit(sourceApkPath):
                isSourceApkExist = True
                AutoUpdateDMPApk.apkPath = sourceApkPath
                self.printf(sourceApkPath + " is exist.")
            else:
                self.printf("ApkSourcePath isn't exist.Please enter ApkSourcePath again! For "
                            "example, D:\\WorkSpace\\Android "
                            "TV\\cvt_app\\multi_media_player\\app\\build\outputs\\apk\\umc\\release"
                            "\\")
        else:
            self.printf("ApkSourcePath is empty! Please enter ApkSourcePath! For "
                        "example, D:\\WorkSpace\\Android "
                        "TV\\cvt_app\\multi_media_player\\app\\build\outputs\\apk\\umc\\release"
                        "\\")

        if self.backupPathLineEdit.text():
            self.printf("ApkBackupPath:" + self.backupPathLineEdit.text())
            backupApkPath = self.backupPathLineEdit.text()
            backupApkPath = checkAndAddBackslashToPath(backupApkPath)
            backupApkPath = backupApkPath + Util.fileControl.getBackupApkName()
            self.printf("ApkSourcePath:" + backupApkPath)
            if filesManager.isFileExit(backupApkPath):
                isBackupApkExist = True
                AutoUpdateDMPApk.backupApkFilePath = backupApkPath
                self.printf(backupApkPath + " is exist.")
            else:
                self.printf("BackupSourcePath isn't exist.Please enter ApkSourcePath again! For "
                            "example, D:\\")
        else:
            self.printf("ApkBackupPath is empty! Please enter ApkBackupPath! For example, D:\\")

        if isBackupApkExist and isSourceApkExist:
            AutoUpdateDMPApk.isPathCheckOk = True
            self.printf("\n ----------------------Check OK------------------")
            self.startPushButton.setEnabled(True)
        else:
            self.printf("\n ----------------------Check Fail------------------")

    def start(self):
        if self.worker.getCheckStatus():
            self.printf("\n ----------------------Start Auto Update------------------")
            if self.thread.isRunning():
                self.printf("\n self.thread.isRunning")
                self.startPushButton.clicked.connect(self.worker.do_work)
            # self.startPushButton.setEnabled(False)
            # self.stopPushButton.setEnabled(True)
        else:
            self.printf("\n Please check path first.")
            # self.startPushButton.setEnabled(False)

    def getBackupApkPath(self, str):
        return self.backupPathLineEdit.text()

    def printf(self, mypstr):
        ###
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        ###
        if type(mypstr) != str:
            return
        print("printf:" + mypstr)
        self.printTextBrowser.append(mypstr)
        cursor = self.printTextBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.printTextBrowser.setTextCursor(cursor)
        QApplication.processEvents()  # 刷新窗口
