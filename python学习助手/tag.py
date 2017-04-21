# !/usr/bin/python    # coding=utf-8

import sys

import random
import os
import re


def _random_str(randomlength=8):
    '''''
    获取指定长度的随机字符串
    '''
    s = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    # rand = random()
    for i in range(randomlength):
        s += chars[random.randint(0, length)]
    return s


    # 使用其他字母等有可能会影响翻译的词意  其他字符会被翻译成相应的中文字符


SPLITE_TAG_TEXT = '________'  # ' splite_tag_%s ' % _random_str()


def add_tag(text):
    '''''
    给文本添加TAG
    '''
    if text is None:
        return None

    pat = re.escape(os.linesep)
    ss = re.sub(pat, SPLITE_TAG_TEXT, text)
    return ss


def remove_tag(text, replacement=os.linesep):
    '''''
    给文本去掉TAG
    '''
    if text is None:
        return None

    pat = re.escape(SPLITE_TAG_TEXT)
    result = re.sub(pat, replacement, text)
    return result


def test():
    s = sys.__doc__
    #print s
    #print '*' * 50

    ss = add_tag(s)
    print ss

    sss = remove_tag(ss)
    #print sss


if __name__ == '__main__':
    test()
