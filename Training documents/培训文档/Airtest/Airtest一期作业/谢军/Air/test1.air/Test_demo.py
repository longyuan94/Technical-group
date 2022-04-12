# -*- encoding=utf8 -*-
__author__ = "xiejun"

from airtest.core.api import *

auto_setup(__file__)
# 打开微信
start_app("com.tencent.mm")
sleep(4)
# 下拉出现微信小程序
swipe([550, 300],[550, 1318])
# 点击搜索窗口
touch(Template(r"tpl1647421894621.png", record_pos=(0.378, -0.327), resolution=(810, 1440)))

sleep(3)
# 点击搜素框
touch(Template(r"tpl1647421923871.png", record_pos=(0.443, -0.805), resolution=(810, 1440)))

sleep(4)
touch(Template(r"tpl1647421951699.png", record_pos=(-0.29, -0.799), resolution=(810, 1440)))
sleep(2.0)

# 输入英雄杀
text("英雄杀")
sleep(3)
# 点击英雄杀
touch(Template(r"tpl1647421984292.png", record_pos=(-0.4, -0.644), resolution=(810, 1440)))

sleep(8)
if exists(Template(r"tpl1647401033023.png", record_pos=(0.194, 0.907), resolution=(1080, 2400))):
    touch(Template(r"tpl1647401033023.png", record_pos=(0.194, 0.907), resolution=(1080, 2400)))
else:
    print("未出现授权弹窗")
sleep(4)

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

    


        

