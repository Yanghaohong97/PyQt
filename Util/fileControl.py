""""
Copyright (C) 2021 CVTE

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
import datetime

import AutoUpdateDMPApk


def getNewestApkName():
    today = datetime.date.today()
    print("Today is " + today.strftime('%Y%m%d'))
    return "DigitalMediaPlayer-" + today.strftime('%Y%m%d') + ".apk"


def getNewestApkPath(apkBasePath):
    return apkBasePath + getNewestApkName()


def getOutputJsonPath():
    return AutoUpdateDMPApk.outputJsonPath


def setOutputJsonPath(apkBasePath):
    print("setOutputJsonPath:apkBasePath = "+apkBasePath)
    AutoUpdateDMPApk.outputJsonPath = apkBasePath + "output.json"


def getBackupApkName():
    return "DigitalMediaPlayer.apk"
