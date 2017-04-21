#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *
from fabric.api import env,run,put,get
from os import path
from re import findall 
from sys import argv
from fabric.context_managers import hide
from time import sleep


#操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
    'testserver': ['developer@172.16.9.144:22'],
    'realserver': ['station@172.16.9.216:22'],
}

env.passwords = {
    'developer@172.16.9.144:22': '123456',
    'station@172.16.9.216:22': 'station',
}

#env.password = '这里不要用这种配置了，不可能要求密码都一致的，明文编写也不合适。打通所有ssh就行了'

@roles('testserver')
def task1():
    run('ls -l | wc -l')

@roles('realserver')
def task2():
    run('ls ~/temp/ | wc -l')

def dotask():
    execute(task1)
    execute(task2)