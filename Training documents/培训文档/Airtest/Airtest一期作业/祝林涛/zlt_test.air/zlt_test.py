# -*- encoding=utf8 -*-
__author__ = "lukaszhu"

from airtest.core.api import *

auto_setup(__file__)
using("Test_demo.air")
#继承Test_demo里面的login方法
from Test_demo import login

#调用登录方法
login()

#=====================================================================================================================
# 点击聊天框
if exists(Template(r"tpl1649684424307.png", record_pos=(0.437, 0.851), resolution=(810, 1440))):
    touch(Template(r"tpl1649684424307.png", record_pos=(0.437, 0.851), resolution=(810, 1440)))
    sleep(5)
    print("打开了聊天界面")
    touch(Template(r"tpl1649685016524.png", record_pos=(0.449, -0.621), resolution=(810, 1440)))
    print("关闭了聊天界面")
    sleep(2)
#邮箱界面遍历
if exists(Template(r"tpl1649685287915.png", record_pos=(-0.41, -0.127), resolution=(810, 1440))):
        touch(Template(r"tpl1649685287915.png", record_pos=(-0.41, -0.127), resolution=(810, 1440)))
        print("打开邮件界面，邮件里有可领取的奖励")    
        sleep(2)
        touch(Template(r"tpl1649686278436.png", record_pos=(-0.394, 0.706), resolution=(810, 1440)))
elif exists(Template(r"tpl1649685962969.png", record_pos=(-0.417, -0.128), resolution=(810, 1440))):
        touch(Template(r"tpl1649685962969.png", record_pos=(-0.417, -0.128), resolution=(810, 1440)))
        print("打开邮件界面，邮件里没有可领取的奖励~~")
        sleep(2)
        touch(Template(r"tpl1649686278436.png", record_pos=(-0.394, 0.706), resolution=(810, 1440)))
#段位界面遍历
if exists(Template(r"tpl1649686313362.png", record_pos=(-0.414, -0.289), resolution=(810, 1440))):
    touch(Template(r"tpl1649686313362.png", record_pos=(-0.414, -0.289), resolution=(810, 1440)))
    print("打开了段位界面")
    sleep(2)
    touch(Template(r"tpl1649686349237.png", record_pos=(0.228, 0.699), resolution=(810, 1440)))
    print("进入赛季界面")
    sleep(2)
    #循环滑到段位界面顶端
    while not exists(Template(r"tpl1649686593310.png", record_pos=(-0.36, -0.338), resolution=(810, 1440))):
        
        swipe([428,658],[428,858])
        print("滑啊滑~~~")
        continue
    print("滑到顶了")
    sleep(2)
    touch(Template(r"tpl1649686278436.png", record_pos=(-0.394, 0.706), resolution=(810, 1440)))
    
