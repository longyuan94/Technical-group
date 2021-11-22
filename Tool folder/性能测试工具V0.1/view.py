from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import os
import subprocess
import datetime
import tkinter as tk
import threading
import time
# from PIL import Image, ImageTk
import re
import signal
import tkinter.filedialog


# 基础功能
class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    # 基础功能页面展示
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Button(self, text='截屏', width=25, height=5, command=self.screenshot).grid(row=1, stick=W, pady=10)
        # Button(self, text='录像',width=25,height=5,command=self.screenrecord).grid(row=2, stick=W, pady=10)
        self.switchscrBtn = Button(self, text='开始录像', width=25, height=5, command=self.switchscreenrecord)
        self.switchscrBtn.grid(row=2, stick=W, pady=10)

        # Button(self, text='安装APK', width=25, height=5, command=self.screenrecord).grid(row=3, stick=W, pady=10)

    # def screenrecord(self):
    #     Label(self).grid(row=0, stick=W, pady=10)
    #     Label(self, text='开始录屏请点击下方按钮').grid(row=3, stick=W, pady=10)
    #     self.B = Button(self, text='开始', width=12, command=self.switch)
    #     self.B.grid(row=6, stick=E, pady=10)

    def switchscreenrecord(self):

        if self.switchscrBtn['text'] == '开始录像':
            self.switchscrBtn['text'] = '结束录像'
            self.startrecord()

        else:
            self.switchscrBtn['text'] = '开始录像'
            self.endrecord()

    def startrecord(self):
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.name1 = nowtime + 'test.mp4'
        out = 'adb shell screenrecord /sdcard/test.mp4'
        self.pro = subprocess.Popen(out, stderr=subprocess.PIPE)

    # 结束进程
    def endrecord(self):
        self.pro.kill()
        out2 = subprocess.getstatusoutput(
            'adb pull /sdcard/test.mp4 .\{}'.format(self.name1))  # .close()是关闭文件的   .kill（）是杀掉进程

    # 截图函数
    def screenshot(self):
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        name = nowtime + '.png'
        out = subprocess.getstatusoutput('adb shell screencap -p /sdcard/screen.png')
        out1 = subprocess.getstatusoutput('adb pull /sdcard/screen.png .\{}'.format(name))
        if out[0] == 0 and out1[0] == 0:
            pass
        else:
            tk.messagebox.showinfo("Message", "未知原因，截图失败")  # 弹出消息窗口


# 安装APK
class InstallFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.number = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Button(self, text='查找安装文件', width=25, height=5, command=self.search).grid(row=1, stick=W, pady=10)

    def search(self):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        self.filename = tkinter.filedialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)),
                                                           filetypes=[("apk格式", "apk")])
        Label(self, text='路径为：').grid(row=2, stick=W, pady=10)
        Label(self, text=self.filename).grid(row=3, pady=10, stick=W)
        self.B = Button(self, text='开始安装', width=12, command=self.switch)
        self.B.grid(row=6, stick=E, pady=10)

    def switch(self):
        print(self.B)

        if self.B['text'] == '开始安装':
            self.B['text'] = '结束安装'
            self.startinstall()  # 调取安装APK函数

        else:
            self.B['text'] = '开始安装'
            self.endinstall()  # 结束抓取日志函数

    def startinstall(self):
        tk.messagebox.showinfo("Message", "马上开始安装")
        out1 = self.filename
        out = 'adb install -r '
        # adb install 为安装  adb install -r为覆盖安装
        out2 = out + out1
        self.pro = subprocess.Popen(out2, stderr=subprocess.PIPE)

    def endinstall(self):
        self.pro.kill()


# monkey压测
class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.packageName = StringVar()  # 包名
        self.pressureNum = StringVar()  # 打压次数
        self.seedNum = StringVar()  # 标记
        self.logLevel = StringVar()  # 日志级别
        self.throttle = StringVar()  # 时间间隔
        self.ignoreCrash = StringVar()  # 忽略崩溃
        self.ignoreANR = StringVar()  # 忽略闪退
        self.ignoreTimeout = StringVar()  # 忽略超时
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='包名: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.packageName).grid(row=1, column=1, stick=E)
        Label(self, text='压力: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.pressureNum).grid(row=2, column=1, stick=E)
        self.press = Entry(self, textvariable=self.pressureNum)
        self.press.insert(10, 1000)
        Label(self, text='标记: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.seedNum).grid(row=3, column=1, stick=E)
        self.seed = Entry(self, textvariable=self.seedNum)
        self.seed.insert(10, 1)

        # 创建一个下拉列表
        Label(self, text='日志级别: ').grid(row=4, stick=W, pady=10)
        numberChosen = ttk.Combobox(self, width=12, textvariable=self.logLevel, state='readonly')
        numberChosen['values'] = (1, 2, 3)  # 设置下拉列表的值
        numberChosen.grid(column=1, row=4, stick=E)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(2)  # 设置下拉列表默认显示的值，1为 numberChosen['values'] 的下标值
        # 创建一个下拉列表,时间间隔throttle
        Label(self, text='throttle').grid(row=5, stick=W, pady=10)
        numberChosen = ttk.Combobox(self, width=12, textvariable=self.throttle, state='readonly')
        numberChosen['values'] = (100, 150, 200, 250, 300, 350, 400)  # 设置下拉列表的值
        numberChosen.grid(column=1, row=5, stick=E)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)  # 设置下拉列表默认显示的值，1为 numberChosen['values'] 的下标值

        Checkbutton(self, text='忽略崩溃', onvalue=1, offvalue=0, variable=self.ignoreCrash).grid(row=6, column=1, stick=E)
        # offvalue  #设置Off的值=0
        # onvalue   #设置on的值=1

        Checkbutton(self, text='忽略超时', onvalue=1, offvalue=0, variable=self.ignoreTimeout).grid(row=7, column=1,
                                                                                                stick=E)
        self.startBtn = Button(self, text='开始压测', command=self.switch)
        self.startBtn.grid(row=8, column=5, stick=E, pady=5)

        Button(self, text='报告分析').grid(row=9, column=5, stick=E, pady=5)
        # 制作中

    # 开始与结束之间的切换
    def switch(self):

        if self.startBtn['text'] == '开始压测':
            self.startBtn['text'] = '强行终止'
            self.monkey()  # 开始跑monkey

        else:
            self.startBtn['text'] = '开始压测'
            self.killPro()  # 结束monkey

    def monkey(self):
        packageName = self.packageName.get()  # 包名
        print('包名{}'.format(packageName))
        pressureNum = int(self.pressureNum.get())  # 打压次数
        print('打压次数:{}'.format(pressureNum))
        seedNum = int(self.seedNum.get())  # 标记
        print('标记：{}'.format(seedNum))
        logLevel = int(self.logLevel.get())  # 日志级别
        print('日志级别:{}'.format(logLevel))
        ignoreCrash = self.ignoreCrash.get()
        print('忽略崩溃:{}'.format(ignoreCrash))
        ignoreTimeout = self.ignoreTimeout.get()
        throttle = int(self.throttle.get())
        print('时间间隔:{}'.format(throttle))

        print('忽略超时:{}'.format(ignoreTimeout))

        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'Monkey' + nowtime + ".txt"
        logcat_file = open(filename, 'w')
        logcmd = r'adb shell monkey -p {} -s {} -v -v -v --throttle {} --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes {}'.format(
            packageName, seedNum, throttle, pressureNum)
        self.pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)

    # 结束进程
    def some_adb_cmd(self):
        p = subprocess.Popen('adb shell cd sdcard && cd Android && cd data && ps |grep monkey', stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        return_code = p.poll()
        while return_code is None:
            line = p.stdout.readline()
            return_code = p.poll()
            line = line.strip()
            line1 = str(line, "utf-8")
            pattern = re.compile(r'[^\d]+(\d+)[^\d]+')
            res = re.findall(pattern, line1)
            # os.kill(int(res), signal.SIGKILL)
            res1 = res[0]
            a = 'adb shell cd sdcard && cd Android && cd data'
            a1 = 'kill ' + res1
            a2 = a + " && " + a1
            p1 = subprocess.Popen(a2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            break

    def killPro(self):

        self.some_adb_cmd()


# log日志
class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.filterTag = StringVar()  # 过滤标签
        self.filterStr = StringVar()  # 过滤字符串
        self.filterRegular = StringVar()  # 正则过滤
        self.logLevel = StringVar()  # 日志级别
        self.filterFormat = StringVar()  # 过滤项格式
        self.createPage()

    def createPage(self):
        # Label(self, text='过滤标签: ').grid(row=1, stick=W, pady=10)

        # entry=Entry(self, textvariable=self.filterTag).grid(row=1, column=1, stick=E)
        Label(self, text='过滤字符串: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.filterStr).grid(row=2, column=1, stick=E)
        # Label(self, text='正则过滤: ').grid(row=3, stick=W, pady=10)
        # Entry(self, textvariable=self.filterRegular).grid(row=3, column=1, stick=E)
        # 日志级别############################################################
        # 创建一个下拉列表
        # Label(self, text='日志级别: ').grid(row=4, stick=W, pady=10)
        # Label(self).grid(row=0, stick=W, pady=10)
        # numberChosen = ttk.Combobox(self, width=12, textvariable=self.logLevel, state='readonly')
        # numberChosen['values'] = (1, 2, 3)  # 设置下拉列表的值
        # numberChosen.grid(column=1, row=4, stick=E)  # 设置其在界面中出现的位置  column代表列   row 代表行
        # numberChosen.current(1)  # 设置下拉列表默认显示的值，1为 numberChosen['values'] 的下标值
        # 过滤格式############################################################
        Label(self, text='过滤项格式: ').grid(row=5, stick=W, pady=10)
        Label(self).grid(row=0, stick=W, pady=10)
        filterFormat = ttk.Combobox(self, width=12, textvariable=self.filterFormat, state='readonly')
        # -- V : Verbose (明细);
        # -- D : Debug (调试);
        # -- I : Info (信息);
        # -- W : Warn (警告);
        # -- E : Error (错误);
        # -- F : Fatal (严重错误);
        filterFormat['values'] = ('Verbose', 'Debug', 'Warn', 'Error', 'Fatal')  # 设置下拉列表的值
        filterFormat.grid(column=1, row=5, stick=E)  # 设置其在界面中出现的位置  column代表列   row 代表行
        filterFormat.current(1)  # 设置下拉列表默认显示的值，1为 numberChosen['values'] 的下标值
        # Button(self, text='开始', width=12,command=self.switch).grid(row=6, stick=E, pady=10)
        self.B = Button(self, text='开始', width=12, command=self.switch)
        self.B.grid(row=6, stick=E, pady=10)

    # 开始与结束之间的切换
    def switch(self):
        print(self.B)

        if self.B['text'] == '开始':
            self.B['text'] = '结束'
            self.logCat()  # 调取抓取日志函数


        else:
            self.B['text'] = '开始'
            self.killPro()  # 结束抓取日志函数

    # def filterLog(self):
    def logCat(self):
        # packageName = self.packageName.get()  # 包名
        # print('包名{}'.format(packageName))

        # 过滤标签
        # filterTag=self.filterTag.get()
        # print('过滤标签:{}'.format(filterTag))
        # print('过滤字符串:{}'.format(self.filterStr.get()))
        # 过滤字符串
        filterStr = self.filterStr.get()
        print('过滤字符串:{}'.format(filterStr))
        # 正则过滤
        # filterRegular=self.filterRegular.get()

        # print('正则过滤:{}'.format(filterRegular))
        # 日志级别
        # logLevel=self.logLevel.get()
        # print('日志级别:{}'.format(logLevel))
        # 过滤格式项
        filterFormat = self.filterFormat.get()
        print('过滤格式项:{}'.format(filterFormat))

        # 抓取日志
        # def logCat(self):
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = nowtime + ".txt"
        logcat_file = open(filename, 'w')
        # logcmd = r'adb shell monkey -p {} -s {} -v -v -v --throttle {} --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes {}'.format(
        #   packageName, seedNum
        # p = subprocess.Popen('adb shell cd sdcard && cd Android && cd data && ps |grep monkey', stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if filterFormat != '' and filterStr != '':
            logcmd = r'adb shell cd sdcard && cd Android && cd data &&  logcat *:{} | grep {}'.format(filterFormat,
                                                                                                      filterStr)
        elif filterFormat != '' and filterStr == '':
            logcmd = r'adb shell cd sdcard && cd Android && cd data &&  logcat *:{}'.format(filterFormat)
        elif filterFormat == '' and filterStr != '':
            logcmd = r'adb shell cd sdcard && cd Android && cd data &&  logcat | grep {}'.format(filterStr)
        else:
            logcmd = 'adb logcat -v time'
        # logcmd = 'adb logcat -v time'
        self.pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)

    # 结束进程
    def killPro(self):
        self.pro.kill()  # .close()是关闭文件的   .kill（）是杀掉进程


# 性能测试界面
class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Button(self, text='内存监测', width=12, command=self.getMemory).grid(row=1, stick=E, pady=10, column=1)
        # Button(self, text='手机CPU监测', width=12, command=self.allCpu).grid(row=2, stick=E, pady=10, column=1)
        Button(self, text='当前应用CPU', width=12, command=self.myCpu).grid(row=2, stick=E, pady=10, column=1)
        Button(self, text='电量信息', width=12, command=self.charge).grid(row=3, stick=E, pady=10, column=1)
        Button(self, text='启动时间', width=12, command=self.startTime).grid(row=4, stick=E, pady=10, column=1)

    # 电量信息
    def charge(self):
        print('电量信息')
        out = subprocess.getstatusoutput('adb shell dumpsys battery')
        top = tk.Toplevel()
        top.title('电量信息')

        top.geometry('%dx%d' % (600, 600))  # 设置窗口大小
        t = Text(top, width=600, height=600)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()

    # 内存数据获取
    def getMemory(self):
        import re
        out = subprocess.getstatusoutput('adb shell dumpsys window | findstr mCurrentFocus ')
        str1 = out[1]
        pattern = re.compile(r'u0\s*(.+?)\/')
        res = re.findall(pattern, str1)
        self.package = res[0]  # 获取当前应用的包名

        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # filename = "startime"+nowtime+".txt"
        filename = "startime" + nowtime + ".xls"
        startime_file = open(filename, 'w')
        order = "adb shell dumpsys meminfo {}".format(self.package)  # 获取内存的命令
        self.pro = subprocess.Popen(order, stdout=startime_file, stderr=subprocess.PIPE)

    # 手机内当前前十位的应用cpu占用动态监测
    def allCpu(self):
        top = tk.Toplevel()
        top.title('内存监测')

        top.geometry('%dx%d' % (700, 1400))  # 设置窗口大小
        # Text文本框的定义和输出
        t = Text(top, width=700, height=100)
        t.pack(fill=tkinter.X, side=tkinter.BOTTOM)
        top.mainloop()
        # out = subprocess.getstatusoutput('adb shell&&top -m 10 -s cpu')
        logcmd = 'adb shell&&top -m 10 -s cpu'
        out = subprocess.Popen(logcmd, stderr=subprocess.PIPE)
        t.insert(tkinter.END, "{}".format(out[1]))
        t.see(tkinter.END)
        t.update()

    # 当前应用占用CPU显示
    def myCpu(self):
        import re
        out = subprocess.getstatusoutput('adb shell dumpsys window | findstr mCurrentFocus ')
        str1 = out[1]
        pattern = re.compile(r'u0\s*(.+?)\/')
        res = re.findall(pattern, str1)
        self.packageName = res[0]  # 获取当前应用的包名
        out = subprocess.getstatusoutput('adb shell dumpsys cpuinfo | find "{}"'.format(self.packageName))
        top = tk.Toplevel()
        top.title('当前应用')

        top.geometry('%dx%d' % (300, 100))  # 设置窗口大小
        t = Text(top, width=300, height=100)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()

    def startTime(self):
        pass


# 设置页面
class SeetingFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='设置开发中').pack()


# 高级页面
class SeniorFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        # 查看手机上已经安装的所有的包名列表
        Label(self, text='当前应用包名: ').grid(row=1, stick=W, pady=10)
        Button(self, text='当前应用', width=12, command=self.currentPackage).grid(row=1, stick=E, pady=10, column=1)

        # 查看手机上已经安装的所有的包名列表
        Label(self, text='包名列表: ').grid(row=2, stick=W, pady=10)
        Button(self, text='包名列表', width=12, command=self.listPackage).grid(row=2, stick=E, pady=10, column=1)
        # 查看当前手机屏幕分辨率
        Label(self, text='设备分辨率: ').grid(row=3, stick=W, pady=10)
        Button(self, text='分辨率', width=12, command=self.resolution).grid(row=3, stick=E, pady=10, column=1)
        # 查看手机系统版本
        Label(self, text='当前手机版本: ').grid(row=4, stick=W, pady=10)
        Button(self, text='手机版本', width=12, command=self.systemversion).grid(row=4, stick=E, pady=10, column=1)
        Label(self, text='手机设备id: ').grid(row=5, stick=W, pady=10)
        Button(self, text='设备id', width=12, command=self.deviceid).grid(row=5, stick=E, pady=10, column=1)

    # 当前应用的包名及activity
    def currentPackage(self):
        out = subprocess.getstatusoutput('adb shell dumpsys window | findstr mCurrentFocus ')
        top = tk.Toplevel()
        top.title('当前应用')

        top.geometry('%dx%d' % (700, 100))  # 设置窗口大小
        t = Text(top, width=700, height=100)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()

    # 所有的包名列表
    def listPackage(self):
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'package' + nowtime + ".txt"
        logcat_file = open(filename, 'w')
        logcmd = 'adb shell pm list packages'
        self.pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
        out = subprocess.getstatusoutput('adb shell pm list packages')

        top = tk.Toplevel()
        top.title('包名列表')

        top.geometry('%dx%d' % (400, 1200))  # 设置窗口大小

        t = Text(top, width=400, height=900)
        t.insert('1.0', "{}".format(out[1]))
        # 插入文本，用引号引起来“1.0” 这个是插入文本的坐标，且1与0之间为点，而不是逗号，切记

        # wraplength： 指定多少单位后开始换行
        # justify:  指定多行的对齐方式
        # 例子： Label(top, text='查看当前手机上所有包名: ',wraplength = 80,justify = 'left').grid(row=1,stick=W, pady=10)
        t.pack()
        top.mainloop()

    # 当前应用的包名及activity
    def resolution(self):
        out = subprocess.getstatusoutput('adb shell wm size')
        top = tk.Toplevel()
        top.title('分辨率')

        top.geometry('%dx%d' % (300, 100))  # 设置窗口大小
        t = Text(top, width=300, height=100)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()

    def systemversion(self):
        out = subprocess.getstatusoutput('adb shell getprop ro.build.version.release')
        top = tk.Toplevel()
        top.title('手机系统版本')

        top.geometry('%dx%d' % (300, 100))  # 设置窗口大小
        t = Text(top, width=300, height=100)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()

    def deviceid(self):
        out = subprocess.getstatusoutput('adb get-serialno')
        top = tk.Toplevel()
        top.title('手机设备id')

        top.geometry('%dx%d' % (600, 100))  # 设置窗口大小
        t = Text(top, width=600, height=100)
        t.insert('1.0', "{}".format(out[1]))
        t.pack()
        top.mainloop()


# 帮助页面
class HelpFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        a = '''如有疑问，请联系倪梦山...'''
        Label(self, text=a).grid(row=1, stick=W, pady=10)
        # Label(self, text=b).grid(row=2, stick=W, pady=10)
        # Label(self, text=c).grid(row=3, stick=W, pady=10)
        # Label(self, text=d).grid(row=4, stick=W, pady=10)



