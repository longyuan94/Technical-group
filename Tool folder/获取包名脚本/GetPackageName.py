# coding=utf-8

"""
德玛西亚
"""

import easygui as a
from math import floor
from tkinter import *
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox 
class APP:

    # 待测试应用路径
    apkPath = filedialog.askopenfilename()

    def __init__(self):
        self.aapt = "D:\\AndroidStudio\\AndroidStudioSDK\\platform-tools\\aapt dump badging "


    # 获取APP的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"

    # 获取APP的版本信息
    def get_apk_version(self):
        cmd = self.aapt + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
            result = result.split("'")[1]
        return result

    # 获取APP的名字
    def get_apk_name(self):
        cmd = self.aapt + self.apkPath + " | findstr application-label-zu: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split("'")[1]
        return result

    # 获取APP的包名
    def get_apk_package(self):
        cmd = self.aapt + self.apkPath + " | findstr package:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split()[1][6:-1]
        return result

    # 得到启动类
    def get_apk_activity(self):
        cmd = self.aapt + self.apkPath + " | findstr launchable-activity:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result

if __name__ == '__main__':
    APPInfo = APP()
    w1 = APPInfo.get_apk_name()
    w2 = APPInfo.get_apk_size()
    w3 = APPInfo.get_apk_version()
    w4 = APPInfo.get_apk_package()
    w5 = APPInfo.get_apk_activity()
def Login():
    msg = '天成牛逼'
    title = '品质中心'
    Fields = ['应用名称','app文件大小','app版本信息',"app包名","app的启动类"]
    ret =a.multenterbox(msg,title,Fields,values=[w1,w2,w3,w4,w5])
    print(ret)
Login()



