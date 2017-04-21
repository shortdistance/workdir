# encoding=utf-8

import wave
import urllib, urllib2, pycurl
import base64
import json
import os
"""
App ID: 9141359

API Key: LrBehqRBdTxEexBMiZKtm4DN

Secret Key: 61189cdfec2457f4e2b1a9c614a12083
"""

def get_token():
    apiKey = "LrBehqRBdTxEexBMiZKtm4DN"
    secretKey = "61189cdfec2457f4e2b1a9c614a12083"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']


def dump_res(buf):
    print (buf)


## post audio to server
def use_cloud(token):
    fp = wave.open('2016-12-29_04_57_53.wav', 'rb')  # 录音文件名
    ##已经录好音的语音片段
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "zhangleiyyy123"  # 你的产品id
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&amp;token=' + token
    print srv_url
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))  # curl doesn't support unicode
    # c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)  # must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()  # pycurl.perform() has no return val


if __name__ == "__main__":
    token = get_token()
    # 获得token
    use_cloud(token)
    # 进行处理，然后
