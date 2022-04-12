# -*- encoding=utf8 -*-
__author__ = "wb-xiejun"

from airtest.core.api import *

auto_setup(__file__)
auto_setup(__file__)
# 打开微信
start_app("com.tencent.mm")
sleep(4)
# 下拉出现微信小程序
swipe([550, 300],[550, 1318])
# 点击搜索窗口
touch(Template(r"tpl1647421894621.png", record_pos=(0.378, -0.327), resolution=(810, 1440)))

sleep(5.0)
# 点击搜素框
touch(Template(r"tpl1647421923871.png", record_pos=(0.443, -0.805), resolution=(810, 1440)))

sleep(4.0)
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
sleep(3)
touch(Template(r"tpl1647940420905.png", record_pos=(-0.41, -0.811), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940468480.png", record_pos=(0.241, -0.072), resolution=(810, 1440)))
touch(Template(r"tpl1647940598297.png", record_pos=(-0.301, -0.831), resolution=(810, 1440)))

sleep(2)
touch(Template(r"tpl1647940537168.png", record_pos=(0.416, -0.623), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940576569.png", record_pos=(-0.107, -0.837), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1647940537168.png", record_pos=(0.416, -0.623), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940663444.png", record_pos=(-0.414, -0.601), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1647940537168.png", record_pos=(0.416, -0.623), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940681914.png", record_pos=(-0.415, -0.447), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940715092.png", record_pos=(-0.394, 0.709), resolution=(810, 1440)))

sleep(1)
touch(Template(r"tpl1647940781733.png", record_pos=(-0.414, -0.078), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940715092.png", record_pos=(-0.394, 0.709), resolution=(810, 1440)))

sleep(1)
touch(Template(r"tpl1647940816985.png", record_pos=(-0.412, 0.035), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1647940835458.png", record_pos=(-0.151, 0.093), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940855435.png", record_pos=(-0.41, 0.188), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940715092.png", record_pos=(-0.394, 0.709), resolution=(810, 1440)))

sleep(1)
touch(Template(r"tpl1647940884025.png", record_pos=(0.406, -0.599), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940715092.png", record_pos=(-0.394, 0.709), resolution=(810, 1440)))

sleep(1)
touch(Template(r"tpl1647940910376.png", record_pos=(0.407, -0.419), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940939008.png", record_pos=(0.452, -0.577), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940956862.png", record_pos=(0.407, -0.258), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647940986244.png", record_pos=(0.363, -0.364), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647941009813.png", record_pos=(0.409, -0.042), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647941031510.png", record_pos=(0.452, -0.578), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647941045821.png", record_pos=(0.406, 0.077), resolution=(810, 1440)))

sleep(4)
if exists(Template(r"tpl1647941151012.png", record_pos=(0.006, -0.088), resolution=(810, 1440))):
    touch(Template(r"tpl1647941178662.png", record_pos=(0.0, 0.312), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647940715092.png", record_pos=(-0.394, 0.709), resolution=(810, 1440)))

sleep(1)
touch(Template(r"tpl1647941209254.png", record_pos=(0.406, 0.293), resolution=(810, 1440)))
sleep(3)
touch(Template(r"tpl1647941235637.png", record_pos=(0.456, -0.578), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1647941256548.png", record_pos=(0.396, -0.811), resolution=(810, 1440)))




