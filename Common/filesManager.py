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
import difflib
import filecmp
import os
import shutil
import sys
from threading import Thread


def copyFile(source_file, destination_file):
    print("copy "+source_file+" to "+destination_file)
    Thread(target=shutil.copy, args=[source_file, destination_file]).start()


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: 没有找到文件:%s或读取文件失败！" % filename)
        sys.exit(1)

def cmpFile(file1, file2):
    return filecmp.cmp(file1, file2)
    # d = difflib.Differ()
    # print(''.join(d.compare(file1, file2)))

def isFileExit(path):
    return os.path.exists(path)
