#!usr/bin/python
# -*- coding:utf-8 -*-


import pykka
import time
import ijson,json
import traceback as tb
from protocol import protoFile
from message import *
from setting import sundry_config,GetLog


class RecvActor(pykka.ThreadingActor):
    def __init__(self, player=None, sock=None):
        super(RecvActor, self).__init__()
        self.player = player
        self.socket = sock

    def on_stop(self):
        print("RecvActor stop")

    @GetLog(level='error')
    def on_failure(self, exception_type, exception_value, traceback):
        logging.error(f'RecvActor fail -> {exception_type, exception_value, tb.print_tb(traceback)}')

    def on_loop(self):
        data = self.socket.recv()
        data = list(ijson.items(data,''))[0]
        # 创建协议类对象
        proto_id,proto_bin = data['cmd'],data
        print('recv -> ',proto_id,proto_bin)
        proto_module = protoFile
        proto_cls = getattr(proto_module, str(proto_id).capitalize())
        proto_cls_ins = proto_cls()
        if hasattr(proto_cls_ins, 'response'):
            getattr(proto_cls_ins,'response')(proto_bin)
            self.player.send_msg(MSG_PROTO, (proto_id, proto_cls_ins))
            self.player.all_decode_data.put_nowait((proto_id,proto_cls_ins))
        else:
            # 发过去的是实例化类
            self.player.send_msg(MSG_PROTO, (proto_id, proto_cls_ins))
            '''协议测试用，不用要注释掉'''
            self.player.all_decode_data.put_nowait((proto_id,proto_bin))
        self.actor_ref.tell({'msg': 'loop'})

    def on_start(self):
        self.on_loop()

    def on_receive(self, msg):
        self.on_loop()
        # sleep一下不然耗性能，单个玩家可以用0.01
        time.sleep(0.1)

class SendActor(pykka.ThreadingActor):
    def __init__(self, player=None, sock=None):
        super(SendActor, self).__init__()
        self.player = player
        self.socket = sock
        self.wpe = 1
    @GetLog(level='error')
    def on_failure(self, exception_type, exception_value, traceback):
        logging.error('SendActor fail => ', exception_type, exception_value, tb.print_tb(traceback))

    def on_stop(self):
        print('SendActor stop')

    def on_start(self):
        self.on_heart()

    def on_heart(self):
        self.player.sys_count += 1
        if self.player.sys_count >= 590:
            self.actor_ref.tell({MSG_PROTO: {'cmd': 'hall_heart'}})
            self.player.sys_count = 0
        # 心跳这里时间会阻塞1毫秒
        self.actor_ref.tell({MSG_HEART:{'msg':'loop'}})
        time.sleep(0.1)


    def on_receive(self, msg):
        '''
        msg[MSG_PROTO] 打包好的协议数据
        发送包有参数的为元组类型，没有参数则直接发送协议
        '''
        if MSG_PROTO in msg.keys() and msg[MSG_PROTO]:
            proto_id, proto_bin = msg[MSG_PROTO]['cmd'],msg[MSG_PROTO]
            proto_header = {
                'cmd': proto_id,
                'sessionId': self.wpe,
                'ts':int(time.time()*1000),
            }
            proto_header.update(proto_bin)
            buff = json.dumps(proto_header)
            self.socket.send(buff)
        elif msg[MSG_HEART]:
            pass
        else:
            print('发过来空数据了')
        if self.wpe is 120:
            self.wpe = 0
        else:
            self.wpe = self.wpe + 1
        self.on_heart()


class HandlerBase:
    def __init__(self,player):
        self.player = player

    # 传送数据到打包actor
    def send_msg(self, data=None):
        self.player.send_actor.tell({MSG_PROTO: data})
    # 传送数据到任务actor
    def task_msg(self, data=None):
        self.player.task_actor.tell({MSG_TASK:data})
    # 传送数据到活动actor
    def activity_msg(self,msg_type=None,data=None):
        self.player.activity_actor.tell({
            'msg':msg_type,
            'data':data})

    def send_gm(self,*args):
        '''
        设置玩家gm,输入类型指定为（*args:tuple) -> tuple  ->指定返回类型
        self.send_gm('set_hp 100')
        '''
        for case in list(args):
            self.send_msg(Game_gm_action().request(gm_type=None,gm_json_param=case))


