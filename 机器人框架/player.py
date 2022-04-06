#!usr/bin/python
# -*- coding:utf-8 -*-

import pykka
import requests
import websocket
import time
import traceback as tb
from setting import server_config as SERVER_LIST
from setting import GetLog
from message import *
from proto import ProtoHandler
from remote import RemoteHandler
from util import MsgSwitch, RecvActor, SendActor
from register import Account
from queue import Queue


TEST_CASE_CALL = None
class Player(pykka.ThreadingActor):
    def __init__(self, user_name='', server='SERVER_1'):
        super(Player, self).__init__()
        self.host = SERVER_LIST[server]['GAME_HOST']
        self.port = SERVER_LIST[server]['GAME_PORT']
        self.web_host = "xx.xx.xx.xx"
        self.recv_actor = None
        self.send_actor = None
        self.task_actor = None
        self.activity_actor = None
        self.socket = None
        self.proto_handler = ProtoHandler(self)
        self.remote_handler = RemoteHandler(self)
        '''测试用例调用player'''
        global TEST_CASE_CALL
        TEST_CASE_CALL = self

        self.player_id = None
        self.state_ip = ''
        self.state_port = 0
        self.state_user_id = 0
        self.state_user_name = user_name
        self.hero_info = None
        # 不要删掉
        self.sys_count = 0

        self.open_days = None
        self.scene_id = None
        self.camp = 0
        self.pos_x = None
        self.pos_y = None
        self.career = None

        self.all_decode_data = Queue()
        self.see_monster = {}
        self.see_target = {}
        self.task_count = 0
        self.dup_apply_back = None
        self.scene_leave = False
        self.stage_boss_event = False


    # 包装一下消息发送
    def send_msg(self, msg_type=None, data=None):
        '''
        :param msg_type:消息类型
        :param data: 数据
        '''
        self.actor_ref.tell({
            'msg': msg_type,
            'data': data
        })

    def remote_msg(self, method:str=None, data=None):
        """
        实时调用remote里的方法
        :param method: 方法名
        :param data: 传入的参数 元组
        :return:
        """
        self.actor_ref.tell({
            'msg': MSG_REMOTE_CMD,
            'method': method,
            'data': data
        })

    def on_start(self):
        if self.state_user_name is '':
            self.send_msg(MSG_GUEST_LOGIN)
        else:
            self.send_msg(MSG_LOGIN_INFO)

    def on_stop(self):
        """0,1,2
        shutdown方法是用来实现通信模式的，模式分三种，SHUT_RD 关闭接收消息通道，SHUT_WR 关闭发送消息通道，SHUT_RDWR 两个通道都关闭。"""
        self.recv_actor.stop()
        self.socket.close()
        self.socket.shutdown()
        # 停止消息接收进程
        # 停止消息发送进程
        self.send_actor.stop()
        # 停止新手任务
        # self.task_actor.stop()
        # 停止主线程
        self.stop()
        print('playerActor stop')


    # 打印报错消息
    @GetLog(level='fatal')
    def on_failure(self, exception_type, exception_value, traceback):
        logging.fatal(f'Player: {self.state_user_name} is down.')
        logging.fatal(f"ErrorType  => {exception_type}")
        logging.fatal(f"ErrorValue => {exception_value}")
        logging.fatal(f"TraceBack  => {tb.print_tb(traceback)}")
        self.on_stop()
    # msg是个dict类型
    def on_receive(self, msg):
        for case in MsgSwitch(msg):
            # 获取用户信息
            if case(MSG_LOGIN_INFO):
                account_info = Account(self.state_user_name).login_info()
                if account_info['code_str'] == '成功':
                    user_into = account_info['user']
                    self.create_player_params  = {
                        'rd3_token': user_into['token'],
                        'rd3_userId': user_into['userId'],
                    }
                    self.create_player_params.update(Account(self.state_user_name).data)
                    self.create_player_params.pop('password')
                    self.create_player_params['cmd'] = 'game_login'
                    self.send_msg(MSG_LOGIN)
                else:print(f'获取角色信息error, 原因: {account_info["code_str"]},{account_info["code"]}')
                break

            # 用户登录
            if case(MSG_LOGIN):
                self.socket = websocket.create_connection(f'ws://{self.host}:{self.port}/')
                self.recv_actor = RecvActor.start(self, self.socket)
                self.send_actor = SendActor.start(self, self.socket)
                self.send_actor.tell({MSG_PROTO: self.create_player_params})
                break
            # 用户创角
            if case(MSG_CREATE_PLAYER):
                create_data = {
                    'nickname': self.state_user_name,
                    'rd3_token': self.create_player_params['rd3_token'],
                    'rd3_userId': self.create_player_params['rd3_userId'],
                    'sid': self.create_player_params['sid'],
                    'token': self.create_player_params['token'],
                }
                self.send_actor.tell({MSG_PROTO: create_data})
                break

            # recv_actor接收到数据就告诉这里
            if case(MSG_PROTO):  # 服务端返回协议处理
                method, data = msg['data']
                if hasattr(self.proto_handler, method):
                    # 执行对应的方法，data类型是class
                    getattr(self.proto_handler, method)(data)
                else:
                    print("没有为协议: %s 定义处理方法, 请前往 protoFile.py 文件中定义!" % method)
                break
            # 控制台调用命令
            if case(MSG_REMOTE_CMD):
                method = msg['method']
                method = (type(method) is int and "r" + str(method)) or (type(method) is str and method)
                # 判断有没有这个方法，有就执行这个方法
                if hasattr(self.remote_handler, method):
                    getattr(self.remote_handler, method)(msg['data'])
                else:
                    print("没有为远程命令: %s 定义处理方法, 请前往 remote.py 文件中定义!" % method)
                break
