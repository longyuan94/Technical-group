# -*- encoding=utf8 -*-
__author__ = "druidding"

from airtest.core.api import *

auto_setup(__file__)
touch([68,64])
sleep(2)
touch([544,584])
sleep(1)
a = Template(r"tpl1647935476010.png", record_pos=(-0.306, -0.84), resolution=(810, 1440))
b = Template(r"tpl1647935691161.png", record_pos=(-0.111, -0.832), resolution=(810, 1440))
c = [69,352]
d = Template(r"tpl1647935500540.png", record_pos=(0.414, -0.619), resolution=(810, 1440))
list1 = [a,b,c]
for i1 in list1:
    touch(i1)
    sleep(3)
    touch(d)
    sleep(1)
e = Template(r"tpl1647935753565.png", threshold=0.5, record_pos=(0.406, -0.611), resolution=(810, 1440))
f = [69,218]
g = [69,475]
h = [69,600]
i = [400,1215]
j = [715,1215]
k = Template(r"tpl1647935828723.png", record_pos=(-0.394, 0.706), resolution=(810, 1440))
list2 = [e,f,g,h,i,j]
for i2 in list2:
    touch(i2)
    sleep(5)
    touch(k)
    sleep(1)
touch([730,366])
sleep(3)
touch(Template(r"tpl1647936189985.png", record_pos=(0.452, -0.577), resolution=(810, 1440)))
sleep(1)
touch([730,500])
sleep(3)
touch(Template(r"tpl1647936287110.png", record_pos=(0.359, -0.367), resolution=(810, 1440)))
sleep(1)
touch([730,640])
sleep(3)
touch(Template(r"tpl1647936349392.png", record_pos=(0.452, -0.572), resolution=(810, 1440)))
sleep(1)
touch(Template(r"tpl1647936754019.png", record_pos=(-0.44, 0.849), resolution=(810, 1440)))
sleep(5)
touch(Template(r"tpl1647936780250.png", record_pos=(0.454, -0.616), resolution=(810, 1440)))
sleep(1)