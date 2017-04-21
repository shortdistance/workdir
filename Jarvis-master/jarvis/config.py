# -*-coding:utf-8 -*-
from util import Family_Services

en_us = "en-US"
zh_cn = "zh-CN"
my_language = zh_cn
GOOGLE_SPEECH_RECOGNITION_API_KEY = None

JARVIS_COGNATES = [u"贾维斯", u"贾克斯"]
XIAOBING_COGNATES = [u'小冰', u'小兵', u'小斌', u'小彬', u'小宾', u'小萍', u'小滨', u'小明', u'小屏', u'小平', u'小并']
STOP_LISTENING_COGNATES = [u"走开", u"闭嘴", u'别说话']
YES_SIR = u'是,主人'
UNKOWN_ACTION = u'没有定义指令'

ACTION_LIST = [
    {'in_msg': u'开灯', 'out_msg': u'灯打开了', 'command': Family_Services.turnOnTheLight},
    {'in_msg': u'关灯', 'out_msg': u'灯关闭了', 'command': Family_Services.turnOffTheLight},
    {'in_msg': u'咖啡机加热', 'out_msg': u'正在加热', 'command': Family_Services.heatCoffee},
    {'in_msg': u'打开电视', 'out_msg': u'正在打开电视', 'command': Family_Services.openTheTV},
    {'in_msg': u'打开浏览器', 'out_msg': u'正在打开浏览器', 'command': Family_Services.openBrowser},
    {'in_msg': u'打开窗帘', 'out_msg': u'正在打开窗帘', 'command': Family_Services.openWindowCurtain},
    {'in_msg': u'唱一首歌', 'out_msg': u'好的，马上开始', 'command': Family_Services.singASong},
]
