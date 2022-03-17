# -*- encoding=utf8 -*-
__author__ = "leolong"

__title__ = "启动APP的封装"

from airtest.core.api import *


auto_setup(__file__)


# clear_app("jp.gungho.rao")
'''游戏登录模块的测试脚本'''
#点击包名为jp.gungho.rao的app
# 打开仙境传说应用
start_app("jp.gungho.rao")
sleep(10)

# 判断是否有更新，有的话，就点击确认更新

if exists(Template(r"tpl1636960927634.png", threshold=0.8, record_pos=(0.088, 0.072), resolution=(2400, 1080))):
    touch(Template(r"tpl1636960927634.png", record_pos=(0.088, 0.072), resolution=(2400, 1080)))
    sleep(10)

else:
    print("未发现更新内容")

# 等待公告界面的出现，没有就退出循环等待并提示进入公告界面，出现就退出该循环
while  True:
    if exists(Template(r"tpl1636961273888.png", record_pos=(-0.001, -0.005), resolution=(2400, 1080))):


       #sleep是等待的意思（下方是等待10秒）  
        sleep(3)

        break

# 进入登录界面
print("进入有公告界面")
sleep(1)

# 点击确认，关闭公告弹窗界面
touch(Template(r"tpl1636963000107.png", record_pos=(0.017, 0.169), resolution=(2400, 1080)))
sleep(1)

# 判断是否出现【Touch Game Start】按钮，出现就点击
if exists(Template(r"tpl1636963041125.png", record_pos=(0.017, 0.16), resolution=(2400, 1080))):
    touch(Template(r"tpl1636963041125.png", record_pos=(0.017, 0.16), resolution=(2400, 1080)))
#     判断是否出现首次登录协议窗口，出现就一步步同意，直到关闭界面
    if exists(Template(r"tpl1636963064720.png", record_pos=(0.015, 0.001), resolution=(2400, 1080))):
        touch(Template(r"tpl1636963098824.png", record_pos=(0.078, 0.088), resolution=(2400, 1080)))
        sleep(1)
        wait(Template(r"tpl1636963168156.png", record_pos=(0.019, -0.001), resolution=(2400, 1080)))
        sleep(1)
        touch(Template(r"tpl1636963203883.png", record_pos=(0.016, 0.093), resolution=(2400, 1080)))
        sleep(2)
#     没有就提示没有登录协议界面
    else:
        print("没有登录协议界面")
#未出现【Touch Game Start】按钮就提示已经登录过账号了
else:
    print("已经登录过账号了")
sleep(3)
# 选区操作

if exists(Template(r"tpl1636963241217.png", record_pos=(0.02, 0.166), resolution=(2400, 1080))):
    #点击选区
    touch(Template(r"tpl1646876701435.png", record_pos=(0.02, 0.122), resolution=(2400, 1080)))
    sleep(2)
    #定位到刘旭-965服务器
    swipe([839, 704],[839, 269])
    sleep(2)
    touch(Template(r"tpl1646879526570.png", record_pos=(-0.15, -0.028), resolution=(2400, 1080)))
    sleep(2)
    touch(Template(r"tpl1646879564518.png", record_pos=(-0.005, 0.052), resolution=(2400, 1080)))
#  点击登录按钮
touch(Template(r"tpl1636963241217.png", record_pos=(0.02, 0.166), resolution=(2400, 1080)))
sleep(5)
# 判断是否有角色选择界面，有的话就进行角色创建
if exists(Template(r"tpl1636963361772.png", record_pos=(-0.022, -0.015), resolution=(2400, 1080))):
    sleep(1)
    touch(Template(r"tpl1636963397970.png", record_pos=(-0.04, 0.192), resolution=(2400, 1080)))
    sleep(2)
    touch(Template(r"tpl1636963426284.png", record_pos=(0.313, 0.194), resolution=(2400, 1080)))
# 已创建账号的，就提示该界面不出现
else:
    print("已经创建账号，该界面不出现")
# 已经有账号的用户，直接点击开始游戏
if exists(Template(r"tpl1636964337231.png", record_pos=(0.396, 0.19), resolution=(2400, 1080))):
    touch(Template(r"tpl1636964337231.png", record_pos=(0.396, 0.19), resolution=(2400, 1080)))
# 如果界面上没有就截图，进入了什么界面，自行判断错误
else:
    snapshot(msg="其他错误，查看报错界面.")

sleep(10)

# 进入游戏主城界面
while True:
    if exists(Template(r"tpl1646880278786.png", record_pos=(0.39, 0.145), resolution=(2400, 1080))):

        sleep(10)
        print("进入游戏主城界面")
        break
stop_app("jp.gungho.rao")







           





