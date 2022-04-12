# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
start_app("com.tencent.mm")
sleep(4)
# 下拉出现微信小程序
swipe([550, 300],[550, 1318])
touch(Template(r"tpl1649403100334.png", record_pos=(-0.33, -0.519), resolution=(1080, 2400)))
sleep(4.0)
touch(Template(r"tpl1649403761269.png", record_pos=(-0.416, -0.906), resolution=(1080, 2400)))
sleep(1.0)
touch([663, 937])
sleep(1.0)
touch(Template(r"tpl1649404160406.png", record_pos=(-0.304, -0.931), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649404183215.png", record_pos=(0.06, 0.642), resolution=(1080, 2400)))
sleep(2.0)
touch(Template(r"tpl1649404204178.png", record_pos=(0.211, 0.642), resolution=(1080, 2400)))
sleep(2.0)
touch(Template(r"tpl1649404223683.png", record_pos=(0.416, -0.578), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649404237805.png", record_pos=(-0.411, -0.714), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649404266085.png", record_pos=(-0.01, 0.875), resolution=(1080, 2400))):
    touch(Template(r"tpl1649404281444.png", record_pos=(-0.394, 0.878), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('没点上')
    sleep(1.0)
touch(Template(r"tpl1649404487034.png", record_pos=(-0.411, -0.551), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649410958676.png", record_pos=(-0.002, 0.651), resolution=(1080, 2400))):
    print('youl')
    touch(Template(r"tpl1649404561406.png", record_pos=(0.417, -0.577), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('wu')
    sleep(1.0)
touch(Template(r"tpl1649404647866.png", record_pos=(-0.411, -0.393), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649404670779.png", record_pos=(0.001, 0.887), resolution=(1080, 2400))):
    touch(Template(r"tpl1649404694322.png", record_pos=(-0.393, 0.884), resolution=(1080, 2400)))
else:
    print('还是没点上')
    sleep(1.0)
touch(Template(r"tpl1649404745238.png", record_pos=(-0.409, -0.234), resolution=(1080, 2400)))
sleep(2.0)
if exists(Template(r"tpl1649404878603.png", record_pos=(0.41, -0.804), resolution=(1080, 2400))):
    touch(Template(r"tpl1649404799124.png", record_pos=(-0.009, 0.706), resolution=(1080, 2400)))
    sleep(2.0)
else:
    touch(Template(r"tpl1649404894637.png", record_pos=(-0.394, 0.881), resolution=(1080, 2400)))
    sleep(1.0)
touch(Template(r"tpl1649404931502.png", record_pos=(0.409, -0.695), resolution=(1080, 2400)))
sleep(2.0)
swipe([562, 1436],[562, 613])
sleep(1.0)
touch(Template(r"tpl1649405097448.png", record_pos=(0.236, 0.881), resolution=(1080, 2400)))
sleep(2.0)
touch(Template(r"tpl1649405118331.png", record_pos=(0.39, 0.874), resolution=(1080, 2400)))
sleep(2.0)
touch(Template(r"tpl1649405144239.png", record_pos=(-0.394, 0.878), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649405164955.png", record_pos=(0.409, -0.533), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649405226386.png", record_pos=(-0.39, -0.382), resolution=(1080, 2400))):
    touch(Template(r"tpl1649405236763.png", record_pos=(0.456, -0.535), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('垃圾')
    sleep(1.0)
touch(Template(r"tpl1649405287028.png", record_pos=(0.406, -0.364), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649405340262.png", record_pos=(-0.012, 0.434), resolution=(1080, 2400))):
    touch(Template(r"tpl1649405348222.png", record_pos=(0.368, -0.327), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('gg')
    sleep(1.0)
touch(Template(r"tpl1649405402268.png", record_pos=(0.409, -0.197), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649405466982.png", record_pos=(0.008, 0.881), resolution=(1080, 2400))):
    touch(Template(r"tpl1649405476111.png", record_pos=(-0.393, 0.881), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('wu')
    sleep(1.0)
touch(Template(r"tpl1649405525004.png", record_pos=(0.449, 1.028), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649405548838.png", record_pos=(-0.251, -0.575), resolution=(1080, 2400))):
    touch(Template(r"tpl1649405558363.png", record_pos=(-0.411, -0.578), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1649405581061.png", record_pos=(-0.342, 0.856), resolution=(1080, 2400)))
    sleep(2.0)
    text("nihao")
    sleep(2.0)
    touch(Template(r"tpl1649405648525.png", record_pos=(0.348, 0.858), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1649405665003.png", record_pos=(0.455, -0.579), resolution=(1080, 2400)))
else:
    print('gun')
    sleep(1.0)
touch(Template(r"tpl1649405699127.png", record_pos=(0.0, 0.825), resolution=(1080, 2400)))
sleep(1.0)
touch(Template(r"tpl1649405735192.png", record_pos=(-0.257, -0.737), resolution=(1080, 2400)))
sleep(1.0)
if exists(Template(r"tpl1649405748791.png", record_pos=(-0.003, 0.885), resolution=(1080, 2400))):
    touch(Template(r"tpl1649405757997.png", record_pos=(-0.394, 0.875), resolution=(1080, 2400)))
    sleep(1.0)
    touch(Template(r"tpl1649405757997.png", record_pos=(-0.394, 0.875), resolution=(1080, 2400)))
    sleep(1.0)
else:
    print('g')




    












    


















