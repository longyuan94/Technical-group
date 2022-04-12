# -*- encoding=utf8 -*-
__author__ = "leolong"

from airtest.core.api import *

auto_setup(__file__)
# 打开微信
start_app("com.tencent.mm")
sleep(4)
# 下拉出现微信小程序
swipe([550, 300],[550, 1318])
# 点击搜索窗口
touch(Template(r"tpl1647400735651.png", record_pos=(0.002, -0.82), resolution=(1080, 2400)))
sleep(4)
# 点击搜素框
touch(Template(r"tpl1647400826568.png", record_pos=(-0.267, -0.969), resolution=(1080, 2400)))
sleep(4)
# 输入英雄杀
text("英雄杀")
sleep(4)
# 点击英雄杀
touch(Template(r"tpl1647400901850.png", record_pos=(-0.307, -0.583), resolution=(1080, 2400)))
sleep(2)
touch(Template(r"tpl1647400982823.png", record_pos=(-0.184, -0.656), resolution=(1080, 2400)))
sleep(3)
if exists(Template(r"tpl1647401033023.png", record_pos=(0.194, 0.907), resolution=(1080, 2400))):
    touch(Template(r"tpl1647401033023.png", record_pos=(0.194, 0.907), resolution=(1080, 2400)))
else:
    print("未出现授权弹窗")
sleep(2)

if exists(Template(r"tpl1647401270018.png", record_pos=(-0.005, 0.057), resolution=(1080, 2400))):
    touch(Template(r"tpl1647401289092.png", record_pos=(-0.206, 0.319), resolution=(1080, 2400)))

sleep(5)
if exists(Template(r"tpl1647401355214.png", record_pos=(-0.019, -0.006), resolution=(1080, 2400))):
    touch([559, 1564])
    sleep(2)
    if exists(Template(r"tpl1647401402933.png", record_pos=(-0.002, 0.629), resolution=(1080, 2400))):
        touch(Template(r"tpl1647401402933.png", record_pos=(-0.002, 0.629), resolution=(1080, 2400)))
        sleep(2)
        touch([520, 1399])
        if exists(Template(r"tpl1647401480576.png", record_pos=(0.017, 0.069), resolution=(1080, 2400))):
            touch(Template(r"tpl1647401504162.png", record_pos=(0.37, -0.233), resolution=(1080, 2400)))
        else:
            print("未出现首场战斗界面")
    else:
        print("已经领取赠礼")
else:
    print("不是回归账号")

if exists(Template(r"tpl1647401480576.png", record_pos=(0.017, 0.069), resolution=(1080, 2400))):
    touch(Template(r"tpl1647401504162.png", record_pos=(0.37, -0.233), resolution=(1080, 2400)))
else:
    print("未出现首场战斗界面")
  

if exists(Template(r"tpl1647401875202.png", record_pos=(-0.401, -0.338), resolution=(1080, 2400))):
    touch(Template(r"tpl1647401900164.png", record_pos=(0.456, -0.535), resolution=(1080, 2400)))
    sleep(5)
touch(Template(r"tpl1647951462497.png", record_pos=(-0.414, -0.611), resolution=(810, 1440)))
sleep(5)
touch(Template(r"tpl1647951544435.png", record_pos=(-0.384, 0.7), resolution=(810, 1440)))
touch(Template(r"tpl1647951565178.png", record_pos=(-0.406, -0.449), resolution=(810, 1440)))
sleep(5)
touch(Template(r"tpl1647951589978.png", record_pos=(0.414, -0.621), resolution=(810, 1440)))
sleep(5)
touch(Template(r"tpl1647951606238.png", record_pos=(-0.412, -0.305), resolution=(810, 1440)))
sleep(5)
touch(Template(r"tpl1647951626842.png", record_pos=(-0.391, 0.691), resolution=(810, 1440)))
sleep(5)
touch(80,600)
sleep(5)
touch(Template(r"tpl1647951730509.png", record_pos=(-0.391, 0.702), resolution=(810, 1440)))








    


        

