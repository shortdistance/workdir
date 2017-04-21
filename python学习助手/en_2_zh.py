#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# Python -V: Python 2.6.6
# filename:GoogleTranslation1.2.py

__author__ = "Yinlong Zhao (zhaoyl[at]sjtu[dot]edu[dot]cn)"
__date__ = "$Date: 2013/04/21 $"

import re
import urllib
import urllib2
import os

import tag


# urllib:
# urllib2: The urllib2 module defines functions and classes which help in opening
# URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.



def translate(text):
    ''''' 
    模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果  
    此行为直接返回结果 
    '''
    return _get_translate_text(_get_html(text))


def _get_html(text):
    ''''' 
    获取翻译后的网页 
    '''
    # text 输入要翻译的英文句子
    text_1 = text
    # 'langpair':'en'|'zh-CN'从英语到简体中文
    values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': text_1, 'langpair': "'en'|'zh-CN'"}
    #values = {'from':}
    url = 'http://translate.google.com.hk/translate_t'
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    # 模拟一个浏览器
    browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
    req.add_header('User-Agent', browser)
    # 向谷歌翻译发送请求
    response = urllib2.urlopen(req)
    # 读取返回页面
    html = response.read()
    return html


def _get_translate_text(html):
    ''''' 
    根据网页内容，提取翻译文本 
    '''
    # 从返回页面中过滤出翻译后的文本
    # 使用正则表达式匹配
    # 翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
    # .*? non-greedy or minimal fashion
    # (?<=...)Matches if the current position in the string is preceded
    # by a match for ... that ends at the current position
    p = re.compile(r"(?<=TRANSLATED_TEXT=)(.*?);INPUT_TOOL_PATH")
    m = p.search(html)
    # text_2=m.group(0).strip(';')
    # return text_2
    return m.group(1)


def _get_source_and_translate_mix_text(source_text, translate_text):
    ''''' 
    根据原文本和翻译后的文本进行混合，保持翻译文本在每行的文本下面 
    '''
    if source_text is None:
        return None
    result = []
    source_lines = source_text.splitlines()
    translate_lines = translate_text.splitlines()
    #    print os.linesep + str(len(source_lines)) + 'source_lines:' + ''.join(source_lines)
    #    print os.linesep + str(len(translate_lines)) + 'translate_lines:' + ''.join(translate_lines)
    for source, translate in zip(source_lines, translate_lines):
        result.append(os.linesep + source + ' ' * (80 - len(source)) + '译：' + translate)
    return ''.join(result)


def test_and_save(orignal_text):
    ''''' 
    测试并且本地文件保存记录  
    '''
    add_tag_text = tag.add_tag(orignal_text)
    print '添加tag的文本：', add_tag_text

    # 保存结果
    filename = 'test_result.txt'
    fp = open(filename, 'w')

    fp.write('原先的文本：' + orignal_text)
    fp.write('\n' + '$' * 50 + '\n')

    html = _get_html(add_tag_text)

    text_remove_tag = tag.remove_tag(_get_translate_text(html))
    fp.write('提取出来的翻译结果为：')
    fp.write(text_remove_tag)

    text_mix = _get_source_and_translate_mix_text(tag.remove_tag(add_tag_text), text_remove_tag)
    fp.write('整理后的结果：' + text_mix)

    fp.close()
    return text_mix


def get_translate_mix_text(orignal_text):
    ''''' 
    获取翻译后并且混合的文本  
    '''
    add_tag_text = tag.add_tag(orignal_text)
    html = _get_html(add_tag_text)
    text_remove_tag = tag.remove_tag(_get_translate_text(html))
    text_mix = _get_source_and_translate_mix_text(tag.remove_tag(add_tag_text), text_remove_tag)
    return text_mix
