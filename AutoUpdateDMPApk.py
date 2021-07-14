# -*- coding: utf-8 -*-
""""
Copyright (C) 2017 CVTE

@ 版权所有：Yanghaohong©版权所有
@ 文件名：$safeitemname$
@ 文件功能描述：
@ 创建日期：2021年7月6日
@ 创建人：Yanghaohong
@ 修改标识：2021年7月6日
@ 修改描述：
@ 修改日期：
@ 修改版本：V1.0.0
"""
import os
import time

import QtUi

from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from Common import filesManager
from PyQt5.QtWidgets import QMainWindow

isPathCheckOk = False
apkPath = ""
targetPath = "/system_ext/priv-app/DigitalMediaPlayer/DigitalMediaPlayer.apk"

backupApkFilePath = ""


class Worker(QMainWindow, QtUi.Ui_Dialog):
    finished = pyqtSignal()  # give worker class a finished signal
    printfSignal = pyqtSignal(str)
    showSuccessSignal = pyqtSignal(str, str)
    isAdbDevicesRet = False
    isAdbRootRet = False
    isAdbRemountRet = False
    isAdbPushRet = False
    isContinueRun = True

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.isContinueRun = True  # provide a bool run condition for the class

    def startTimer(self, mSec):
        timer = QTimer()  # 计时器
        timer.timeout.connect(self.update)
        timer.start(mSec)

    def do_work(self):
        self.printf("self.isContinueRun =" + str(self.isContinueRun))
        count = 1
        self.isContinueRun = True

        if not filesManager.isFileExit(backupApkFilePath):
            filesManager.copyFile(apkPath, backupApkFilePath)

        # while self.isContinueRun and count:  # give the loop a stoppable condition
        while self.isContinueRun:  # give the loop a stoppable condition
            time.sleep(0.1)
            self.printf("Check DMP APK ......")
            if filesManager.isFileExit(backupApkFilePath):
                if not filesManager.cmpFile(apkPath, backupApkFilePath):
                    self.printf("DMP Apk isn't same! Start to copy file.")
                    self.printf("apkPath is " + apkPath)
                    self.printf("backupApkFilePath is " + backupApkFilePath)
                    filesManager.copyFile(apkPath, backupApkFilePath)
                    self.isContinueRun = False
                    time.sleep(3)
                else:
                    self.printf("DMP Apk is same! contiue!")
                    continue

                # if not self.sendAdbDevicesMsg():
                #     self.printf("send 'adb devices' return fail! contiue")
                #     continue
                # if not self.sendAdbRootMsg():
                #     self.printf("send 'adb root' return fail! contiue")
                #     continue
                # if not self.sendAdbRemountMsg():
                #     self.printf("send 'adb remount' return fail! contiue")
                #     continue
                #
                # if self.sendAdbPushMsg():
                #     self.printf("start  sendAdbSyncAndRebootMsg")
                #     self.sendAdbSyncAndRebootMsg()
                #     time.sleep(3)
                #     count = count - 1
                #     # self.showSuccessDialg("Info", "更新成功！")
                #     continue
                # else:
                #     self.printf("send 'adb push' return fail! contiue")
                #     # self.showSuccessDialg("Info", "更新失败！")
                #     continue

            else:
                self.printf("DMP Apk is same!!")

        # self.printf("self.finished.emit()")
        # self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.printf("Stop!!!!!!!!!!!!")
        self.isContinueRun = False  # set the run condition to false on stop

    def printf(self, mypstr):
        ###
        # 自定义类print函数, 借用c语言
        # printf
        # Mypstr：是待显示的字符串
        ###
        self.printfSignal.emit(mypstr)

    def showSuccessDialg(self, title, message):
        self.showSuccessSignal.emit(title, message)

    def getCheckStatus(self):
        return isPathCheckOk

    def setCheckStatus(self, status):
        if type(status) == bool:
            isPathCheckOk = status
        else:
            self.printf("The type of status isn't bool!")

    def isApkExist(self):
        return os.path.exists(apkPath)

    def sendAdbDevicesMsg(self):
        self.printf("adb devices")
        retAdbDevicesFile = os.popen("adb devices")
        deviceCount = 0
        for line in retAdbDevicesFile.readlines():
            self.printf(line)
            if ("device" in line) and ("devices" not in line):
                deviceCount = deviceCount + 1
                self.printf(str(deviceCount))

        if deviceCount == 1:
            return True
        else:
            return False

    def sendAdbRootMsg(self):
        self.printf("adb root")
        retAdbRootFile = os.popen("adb root")
        result = False
        for line in retAdbRootFile.readlines():
            self.printf(line)
            if "restarting adbd as root" in line or "adbd is already running as root" in line:
                result = True

        return result

    def sendAdbRemountMsg(self):
        self.printf("adb remount")
        retAdbRemountFile = os.popen("adb remount")
        result = False
        for line in retAdbRemountFile.readlines():
            self.printf(line)
            if "remount succeeded" in line:
                result = True

        return result

    def sendAdbPushMsg(self):
        if not filesManager.isFileExit(backupApkFilePath):
            self.printf("apk doesn't exist!")
            return False
        adbCommand = "adb push " + backupApkFilePath + " " + targetPath
        self.printf(adbCommand)
        retAdbPushFile = os.popen(adbCommand)
        result = False
        for line in retAdbPushFile.readlines():
            self.printf(line)
            if "error:" in line or "Read-only file" in line:
                result = False
            else:
                result = True
        return result

    def sendAdbSyncAndRebootMsg(self):
        self.printf("adb shell sync && adb shell reboot")
        os.popen("adb shell sync")
        os.popen("adb shell sync")
        os.popen("adb shell reboot")
