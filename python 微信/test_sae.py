# -*- coding: utf-8 -*-
# /usr/bin/env python

import sys, urllib, httplib, time, hashlib, random
import requests
from requests.adapters import HTTPAdapter
import chardet

reload(sys)
sys.setdefaultencoding('utf-8')

# 配置
interface_url = 'http://mylrc.sinaapp.com:80'  # 注意不能加http://
interface_path = '/'
Token = 'shortdistance_token'

messages = {
    # 用户关注消息
    'subscribe': '''<xml><ToUserName><![CDATA[your name]]></ToUserName>
    <FromUserName><![CDATA[tester name]]></FromUserName>
    <CreateTime>123456789</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    <EventKey><![CDATA[EVENTKEY]]></EventKey>
    </xml>''',

    # 用户发送文本信息
    'text': '''<xml><URL><![CDATA[http://mylrc.sinaapp.com]]></URL>
    <ToUserName><![CDATA[o6_w3xNUgHiRT21ul0UxBrrgLFAY]]></ToUserName>
    <FromUserName><![CDATA[gh_533d2bcc7c04]]></FromUserName>
    <CreateTime>1450973564</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[hi@world]]></Content>
    <MsgId>1234567890123456</MsgId></xml>'''
}


def Post(Url, data):
    s = requests.Session()
    #s.mount(Url, HTTPAdapter(max_retries=2))

    s.headers.update(
        {"Content-type": "text/xml",
         "Content-Length": "%d" % len(data),
         })

    timestamp = int(time.time())
    nonce = random.randint(1, 100000)
    signature = makeSignature(Token, timestamp, nonce)
    params = urllib.urlencode({'signature': signature, 'timestamp': timestamp, 'nonce': nonce})
    suburl = interface_path + "?" + params

    try:
        if Url.find('https') == 0 and Url.index('https') == 0:
            r = s.post("%s" % Url + suburl, data=data, verify=False)
        else:
            r = s.post("%s" % Url + suburl, data=data)
        #print r.headers

        content_type = chardet.detect(r.content)['encoding']
        if content_type:
            return r.status_code, r.content.decode(str(content_type)).encode('gbk')
        else:
            return r.status_code, r.content
    except Exception, e:
        return -1, e.message


def makeSignature(Token, timestamp, nonce):
    '''生成签名'''
    try:
        Token = int(Token)
    except Exception, e:
        pass

    sorted_arr = map(str, sorted([Token, timestamp, nonce]))

    sha1obj = hashlib.sha1()
    sha1obj.update(''.join(sorted_arr))
    hash = sha1obj.hexdigest()

    return hash


def listAction():
    print("======Supported actions:======")
    for i in messages.keys():
        print(i)
    print("==============================")


if __name__ == '__main__':
    retcode, retstr = Post(interface_url, messages['text'])
    print retcode, retstr
