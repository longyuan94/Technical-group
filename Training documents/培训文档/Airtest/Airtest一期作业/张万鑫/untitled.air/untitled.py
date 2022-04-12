# -*- encoding=utf8 -*-
__author__ = "丶天上的太阳"

from airtest.core.api import *

auto_setup(__file__)
# 打开微信
start_app("com.tencent.mm")
sleep(2)
#向下拉出小程序
swipe([492, 284],[516, 1836])
sleep(3)
touch(Template(r"tpl1649410726529.png", record_pos=(0.026, -0.813), resolution=(1080, 2400)))
sleep(1)
#点击搜索
touch(Template(r"tpl1649410763886.png", record_pos=(-0.263, -0.97), resolution=(1080, 2400)))
sleep(2)
#输入英雄杀
text("英雄杀")
sleep(1)
#点击英雄杀
touch(Template(r"tpl1649410921539.png", record_pos=(-0.313, -0.735), resolution=(1080, 2400)))
sleep(2)
touch(Template(r"tpl1649412227152.png", record_pos=(0.009, 0.833), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649412296497.png", record_pos=(0.004, -0.728), resolution=(1080, 2400)))
sleep(1)
touch(Template(r"tpl1649412317933.png", record_pos=(-0.387, 0.889), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649412632787.png", record_pos=(-0.391, 0.889), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649412645669.png", record_pos=(-0.407, -0.226), resolution=(1080, 2400)))
if exists(Template(r"tpl1649412711232.png", record_pos=(-0.015, -0.156), resolution=(1080, 2400))):
    touch(Template(r"tpl1649412971888.png", record_pos=(0.352, -0.126), resolution=(1080, 2400)))
else:
    print("没有异常情况公告")
sleep(1.0)
touch(Template(r"tpl1649413181008.png", record_pos=(0.0, 0.654), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649413246975.png", record_pos=(-0.002, 0.296), resolution=(1080, 2400)))
if exists(Template(r"tpl1649413280177.png", record_pos=(-0.006, -0.689), resolution=(1080, 2400))):
    touch(Template(r"tpl1649413333718.png", record_pos=(0.365, -0.656), resolution=(1080, 2400)))
else:
    print("没有更新公告")
    touch(Template(r"tpl1649413380252.png", record_pos=(0.009, 0.667), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649413395215.png", record_pos=(0.024, 0.252), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649413492748.png", record_pos=(-0.385, 0.881), resolution=(1080, 2400)))






