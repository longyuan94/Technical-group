# -*- encoding=utf8 -*-
__author__ = "BJB0011"
from airtest.core.api import  *
auto_setup(__file__)

# 脚本功能：主界面遍历
main_button = (Template(r"tpl1649164077310.png", record_pos=(-0.414, -0.904), resolution=(1080, 2400)), Template(r"tpl1649629696467.png", record_pos=(-0.415, -0.661), resolution=(1080, 2400)), Template(r"tpl1649164113413.png", record_pos=(-0.417, -0.482), resolution=(1080, 2400)), Template(r"tpl1649164136636.png", record_pos=(-0.417, -0.323), resolution=(1080, 2400)), Template(r"tpl1649164147094.png", record_pos=(-0.417, -0.169), resolution=(1080, 2400)),Template(r"tpl1649629738599.png", record_pos=(-0.413, -0.026), resolution=(1080, 2400)),Template(r"tpl1649164254853.png", record_pos=(-0.417, 0.146), resolution=(1080, 2400)), Template(r"tpl1649164268308.png", record_pos=(0.406, -0.631), resolution=(1080, 2400)), Template(r"tpl1649164342578.png", record_pos=(0.404, -0.467), resolution=(1080, 2400)), Template(r"tpl1649164353873.png", record_pos=(0.406, -0.299), resolution=(1080, 2400)), Template(r"tpl1649164365014.png", record_pos=(0.409, -0.134), resolution=(1080, 2400)), Template(r"tpl1649164374644.png", record_pos=(0.409, 0.033), resolution=(1080, 2400)), Template(r"tpl1649164386401.png", record_pos=(0.404, 0.201), resolution=(1080, 2400)),Template(r"tpl1649235973459.png", record_pos=(-0.016, 0.645), resolution=(1080, 2400)),Template(r"tpl1649629833125.png", record_pos=(-0.381, 0.849), resolution=(1080, 2400)),Template(r"tpl1649629855557.png", record_pos=(-0.215, 0.855), resolution=(1080, 2400)),Template(r"tpl1649629865996.png", record_pos=(0.003, 0.873), resolution=(1080, 2400)),Template(r"tpl1649629874691.png", record_pos=(0.219, 0.861), resolution=(1080, 2400)),Template(r"tpl1649629883529.png", record_pos=(0.387, 0.845), resolution=(1080, 2400)),Template(r"tpl1649236747682.png", record_pos=(0.44, 1.024), resolution=(1080, 2400)))
button_name = ["头像","排行榜","好友","段位","邮件","茶馆","战队","商城","招募有礼","首充","免费抽奖","战令","福利中心","赏春踏雪","身份场","赛事","对战","万象","好友房","聊天"]
back_button = [Template(r"tpl1649164104659.png", record_pos=(0.415, -0.579), resolution=(1080, 2400)), Template(r"tpl1649164152445.png", record_pos=(-0.401, 0.886), resolution=(1080, 2400)), Template(r"tpl1649234917497.png", record_pos=(0.361, -0.331), resolution=(1080, 2400)), Template(r"tpl1649164087398.png", record_pos=(0.18, 0.3), resolution=(1080, 2400))]
other_button = [Template(r"tpl1649164212403.png", record_pos=(0.418, -0.98), resolution=(1080, 2400)),Template(r"tpl1649233035961.png", record_pos=(-0.002, 0.003), resolution=(1080, 2400)),Template(r"tpl1649164163074.png", record_pos=(0.196, 0.114), resolution=(1080, 2400))]


# 检测主界面按钮
def checkmbtn(butt,buttname):
    if exists(butt):
        print("点击%s" % buttname)   
        touch(butt)
        sleep(1)
    else:
        pass
    
# 检测返回按钮
def checkbbtn():
    for j in back_button:
        if exists(j):
            print("点击返回按钮")   
            touch(j)
            break
            sleep(1)
        else:
            pass
        
# 检测茶馆授权      
def checktbtn(butt,buttname):
    if exists(butt):
        print("点击%s" % buttname)        
        touch(butt)
        sleep(1)
        if exists(other_button[2]):
            print("授权允许进入茶馆")
            touch(other_button[2])
            sleep(1)
            touch(other_button[0])

# 遍历主界面上的所有功能按钮
for i in range(len(main_button)):
    if i == 5 :
        checktbtn(main_button[i],button_name[i])
    else:
        checkmbtn(main_button[i],button_name[i])
    checkbbtn()
    if i == 15 :
        checkbbtn()

# 关闭游戏        
touch(other_button[0])





