# -*- coding:utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from MainPage import *
import os
import re
import subprocess


class HomePage1(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='连接手机', width=12, command=self.loginCheck).grid(row=1, stick=W, pady=10, column=1)
        Button(self.page, text='退出', width=12, command=self.page.quit).grid(row=2, column=1, stick=E)

    def loginCheck(self):
        # 点击后去连接手机，连接手机后，对是否连接成功做一些判断，
        # 如何获取控制台的内容，Python2 与Python3 处理是不一样的
        # Python2的处理方式为commands模块，但是Python3中废掉了commands模块，用subprocess代替，详情使用方法访问博客：
        # https://blog.csdn.net/qq_39208536/article/details/80894752
        out = subprocess.getstatusoutput('adb devices -l')
        out1 = subprocess.getstatusoutput('adb devices')
        # out是一个tuple，(0, 'List of devices attached \nc0cfe4a4               device product:PD1515A model:vivo_X6Plus_A device:PD1515A\n')
        # out[0]为状态码，0成功，1失败
        if out[0] == 0:  # 命令成功之后，进行判断
            if 'device product' in out[1]:
                self.page.destroy()
                MainPage(self.root)
                # 连接成功返回新的页面
            else:
                self.sayTry()
                # 此时命令执行成功，但是手机没有连接上
        else:
            if out1[0] == 0:
                if 'device' in out1[1]:
                    self.page.destroy()
                    MainPage(self.root)
                    # 连接成功返回新的页面
                else:
                    self.sayTry()
            else:
                self.sayNoadb()  # 增加了对adb命令执行失败的判断。

    def connectPhone(self):
        self.page.destroy()

    def sayTry(self):
        tk.messagebox.showinfo("Message", "手机连接失败,请尝试重新连接")  # 弹出消息窗口

    def sayFail(self):
        tk.messagebox.showinfo("Message", "手机连接失败，未知错误")  # 弹出消息窗口

    # 没有安装adb判断
    def sayNoadb(self):
        tk.messagebox.showinfo("Message", "没有安装adb或者未配置adb环境变量")  # 弹出消息窗口



