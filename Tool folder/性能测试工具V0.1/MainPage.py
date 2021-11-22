from tkinter import *
from view import *  # 菜单栏对应的各个子页面


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 450))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.installPage = InstallFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        # self.settingPage = SeetingFrame(self.root)
        self.seniorPage = SeniorFrame(self.root)  # 高级页面
        self.helpPage = HelpFrame(self.root)
        self.inputPage.pack()  # 默认显示基础功能界面
        menubar = Menu(self.root)
        menubar.add_command(label='基础功能', command=self.inputData)
        menubar.add_command(label='安装apk', command=self.installData)
        menubar.add_command(label='monkey', command=self.queryData)
        menubar.add_command(label='log日志', command=self.countData)
        menubar.add_command(label='性能测试', command=self.aboutDisp)
        # menubar.add_command(label='设置', command=self.setting)
        menubar.add_command(label='高级', command=self.senior)
        menubar.add_command(label='帮助', command=self.helpMe)

        self.root['menu'] = menubar  # 设置菜单栏

    def inputData(self):
        self.inputPage.pack()
        self.installPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    def installData(self):
        self.inputPage.pack_forget()
        self.installPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.installPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.installPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.installPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    # def setting(self):#设置页面
    #     self.inputPage.pack_forget()
    #     self.queryPage.pack_forget()
    #     self.countPage.pack_forget()
    #     self.aboutPage.pack_forget()
    #     self.settingPage.pack()
    #     self.helpPage.pack_forget()
    #     self.installPage.pack_forget()
    #     self.seniorPage.pack_forget()  # 不显示高级页面

    def helpMe(self):  # 帮助页面
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack()
        self.installPage.pack_forget()
        self.seniorPage.pack_forget()  # 不显示高级页面

    def senior(self):  # 高级页面
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        # self.settingPage.pack_forget()
        self.helpPage.pack_forget()
        self.installPage.pack_forget()
        self.seniorPage.pack()  # 显示高级页面

