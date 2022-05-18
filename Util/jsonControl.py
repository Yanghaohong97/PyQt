""""
Copyright (C) 2021 CVTE

@ 版权所有：Yanghaohong©版权所有
@ 文件名：$safeitemname$
@ 文件功能描述：
@ 创建日期：2021年7月6日
@ 创建人：Yanghaohong
@ 修改标识：2021年7月6日--con
@ 修改描述：
@ 修改日期：
@ 修改版本：V1.0.0
"""
import json

from Common import filesManager


def resolveVersionCodeFromApkOutputJson(apkOutputJsonFile):
    if not filesManager.isFileExit(apkOutputJsonFile):
        return 0

    # Load File
    file = open(apkOutputJsonFile, "rb")
    jsonFile = json.load(file)

    # Resolve File
    apkInfo = jsonFile[0]["apkData"]
    # print(apkInfo)
    apkInfo_versionCode = apkInfo["versionCode"]
    # print(type(apkInfo_versionCode))
    # print(apkInfo_versionCode)
    return apkInfo_versionCode
