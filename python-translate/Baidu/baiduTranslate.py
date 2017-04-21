# -*- coding: utf-8 -*-
import string
import re, os
import json
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 调用baidu翻译api
def trans_baidu(src):
    ApiKey = "XXXXXXXXXXXXXXXXXXX"  # 百度开发者apikey
    turl = "http://openapi.baidu.com/public/2.0/bmt/translate?client_id=" + ApiKey + "&q=" + src + "&from=auto&to=zh"

    try:
        req = urllib2.Request(turl)
        con = urllib2.urlopen(req).read()
    except Exception, e:
        raise e
    else:
        decoded = json.loads(con)
        dst = str(decoded["trans_result"][0]["dst"])
        return dst


def main():
    while True:
        word = raw_input('Input the word you want to search:')
        print "translate.........."
        target = trans_baidu(word)
        print target


if __name__ == '__main__':
    main()