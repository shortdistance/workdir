# -*- coding:utf-8 -*-
import requests
import json

global s
s = requests.session()

url = 'http://www.tuling123.com/openapi/api'
apiKey = 'bde2cee3b7f94af5abc0cf49f0d70840'


def talk(content):
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": apiKey, "info": content}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    code = j['code']
    if code == 100000:
        ret_content = j['text']
        re_url = None
    elif code == 200000:
        ret_content = j['text']
        re_url = j['url']
    elif code == 302000:
        if len(j['list']) > 0:
            ret_content = j['text'] + j['list'][0]['info']
            re_url = j['list'][0]['detailurl']
        else:
            ret_content = j['text']
            re_url = None
    elif code == 308000:
        if len(j['list']) > 0:
            ret_content = j['text'] + j['list'][0]['info']
            re_url = j['list'][0]['detailurl']
        else:
            ret_content = j['text']
            re_url = None
    else:
        ret_content = u'这货还没学会怎么回复这句话'
        re_url = None
    return ret_content, re_url


if __name__ == '__main__':
    msg = u'今天的日期'
    print talk(msg)
