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
sleep(1)
# 点击搜素框
touch(Template(r"tpl1647400826568.png", record_pos=(-0.267, -0.969), resolution=(1080, 2400)))
sleep(1)
# 输入英雄杀
text("英雄杀")
sleep(1)
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
    touch(Template(r"tpl1648102481547.png", record_pos=(0.458, -0.573), resolution=(810, 1440)))

touch(Template(r"tpl1648102960419.png", record_pos=(-0.41, -0.612), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103012323.png", record_pos=(0.41, -0.623), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103035487.png", record_pos=(-0.415, -0.442), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1648103053564.png", record_pos=(-0.386, 0.702), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103068685.png", record_pos=(-0.41, -0.293), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103087292.png", record_pos=(-0.39, 0.699), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103119095.png", record_pos=(-0.409, -0.133), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103136675.png", record_pos=(-0.39, 0.706), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103150692.png", record_pos=(-0.415, 0.033), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103188813.png", record_pos=(-0.165, 0.095), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103204507.png", record_pos=(-0.41, 0.194), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103227211.png", record_pos=(-0.39, 0.707), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103245786.png", record_pos=(-0.001, 0.648), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103267097.png", record_pos=(-0.001, -0.36), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103282271.png", record_pos=(-0.395, 0.711), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103294089.png", record_pos=(-0.396, 0.706), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103310696.png", record_pos=(0.404, -0.601), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1648103328123.png", record_pos=(0.086, 0.702), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1648103343832.png", record_pos=(-0.391, 0.714), resolution=(810, 1440)))
sleep(1)
def cyl(a,b):
    touch(a)
    sleep(2)
    touch(b)
    sleep(1) 
cyl(Template(r"tpl1648104418139.png", record_pos=(0.412, -0.422), resolution=(810, 1440)),Template(r"tpl1648104436433.png", record_pos=(0.451, -0.563), resolution=(810, 1440)))
cyl(Template(r"tpl1648104525416.png", record_pos=(0.399, -0.252), resolution=(810, 1440)),Template(r"tpl1648104532308.png", record_pos=(0.36, -0.358), resolution=(810, 1440)))
cyl(Template(r"tpl1648104563826.png", record_pos=(0.407, -0.096), resolution=(810, 1440)),Template(r"tpl1648104573418.png", record_pos=(0.459, -0.567), resolution=(810, 1440)))
cyl(Template(r"tpl1648104595757.png", record_pos=(0.405, 0.07), resolution=(810, 1440)),Template(r"tpl1648104620286.png", record_pos=(-0.398, 0.701), resolution=(810, 1440))) 
cyl(Template(r"tpl1648104638014.png", record_pos=(0.406, 0.243), resolution=(810, 1440)),Template(r"tpl1648104649240.png", record_pos=(0.456, -0.572), resolution=(810, 1440)))
cyl(Template(r"tpl1648104668488.png", record_pos=(0.225, 0.646), resolution=(810, 1440)),Template(r"tpl1648104677690.png", record_pos=(-0.39, 0.702), resolution=(810, 1440)))






