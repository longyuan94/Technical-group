#!/usr/bin/env python
# encoding: utf-8


import time
import sys
import pytest
import pykka
import pathlib
from player import Player



class Main:
    def __init__(self,account:str='test01',server_id:int=1):
        self.server_id = server_id
        self._account = account
        if self._account:
            __ref = Player.start(self._account, f'SERVER_{self.server_id}')
            self.proxy = __ref.proxy()
        else:raise NameError('输入的账号名不符合')
    @property
    def account(self):
        return self._account
    @account.setter
    def account(self,value):
        if not isinstance(value,str) :
            raise NameError('账号名字为字符串类型')
        if len(value) < 1 or len(value) > 6 :
            raise NameError('账号名字长度不能大于6小于1')
        self._account = value

    def __call__(self, remote_fun:str='',*remote_args,remote_count:int=1):
        if isinstance(remote_fun,str):
            for _ in range(remote_count):
                self.proxy.remote_msg(remote_fun,remote_args)
        else:raise TypeError('调用方法名为字符串格式')

    def stop(self):
        self.proxy.on_stop()


'''登录指定账号'''
send = Main(account='player800',server_id=2)

time.sleep(2)
print('send -> send(func,*args)')
# send('game_store_refresh_goods')
BASE_DIR = pathlib.Path(__file__).parent




# 收集玩家实例
PLAYERDICT = pykka.ActorRegistry.get_by_class_name('Player')
'''登录多个指定账号'''
def players(min_num=1,max_num=None):
    name = 'player'
    for i in range(min_num,max_num):
        send = Main(f'{name}{i}',server_id=2)
        # print(f'{name}{i}')
        yield send




