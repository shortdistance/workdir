# -*- coding:utf8 -*-
import requests
import urllib2, urllib

import re
import sys
import json
from requests.adapters import HTTPAdapter
import chardet
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


def Get(Url):
    s = requests.Session()
    s.headers.update(
        {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
            'Connection': 'Keep-Alive', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})

    try:
        if Url.find('https') == 0 and Url.index('https') == 0:
            r = s.get('%s' % Url, verify=False)
        else:
            r = s.get('%s' % Url)

        #print r.status_code
        if r.status_code == 200:
            content_type = chardet.detect(r.content)['encoding']
            #print content_type
            soup = BeautifulSoup(r.content, from_encoding=content_type)

            #print soup.encode('gb18030')
            return 200, soup.encode('gb18030')

        else:
            return r.status_code, r.content

    except Exception, e:
        print 404, None


def Post(Url, data):
    s = requests.Session()
    s.headers.update(
        {
            'User-Agent': 'Mozilla/4.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN',
        })
    try:
        if Url.find('https') == 0 and Url.index('https') == 0:
            r = s.post("%s" % Url, data=data, verify=False)
        else:
            r = s.post("%s" % Url, data=data)

        if r.status_code == 200:
            content_type = chardet.detect(r.content)['encoding']

            soup = BeautifulSoup(r.content, from_encoding=content_type)
            return 200, soup.encode('gb18030')

        else:
            return r.status_code, r.content

    except Exception, e:
        print 404, None


class SharkSearcher():
    def __init__(self):
        pass

    def process_lrc(self, lrc):
        # rid of the beginning blank & replace the '<br />' with '\n'
        lrc = '\n'.join(lrc.strip().split('<br />'))
        return lrc

    def name_match(self, s, t):
        # check if s contain t.
        for ch in t:
            if s.find(t) == -1:
                return False
        return True

    def feed(self, args):
        myurl = 'http://www.xiami.com/search?key=' + '+'.join(args)
        print myurl
        # pretent to be IE. ^O^
        status_code, html = Get(myurl)
        if status_code == 200:
            song_urls = []
            try:
                pattern = r'<td class="song_name">\s*<a href="([\s\S]+?)" target="_blank" title="([\s\S]+?)">'
                result = re.findall(pattern, html)
                # 0 --- href ;    1 --- song name ;
                for i in range(len(result)):
                    song_urls.append(result[i][0])

            except BaseException:
                return None

            #print song_urls
            try:
                pattern = r'<li class="clearfix">([\s\S]+?)</li>'
                for song_url in song_urls:
                    #print song_url.replace('song', 'lrc')
                    status_code, html_lrc = Get(song_url.replace('song', 'lrc'))
                    print status_code, html_lrc.decode('gb18030').encode('utf-8')
                    lrc = re.findall(pattern, html_lrc.decode('gb18030').encode('utf-8'))[0]
                    print song_url, lrc
                    if lrc:
                        print '~~~~~~~~',lrc
                        break
            except BaseException:
                return None
            return self.process_lrc(lrc)
        else:
            return None


error_msg = u'查理没用...查不到...\nbtw,您听歌的品味真独特.\n您确认格式正确?(歌名@歌手名)\n好啦还是人家太弱了啦...TAT'
if __name__ == '__main__':

    Content = u'绿光@孙燕姿'
    args = Content.split('@')
    shark = SharkSearcher()

    try:
        Content = shark.feed(args)
        if Content == None:
            Content = error_msg
    except BaseException:
        Content = error_msg

    print Content.replace('</br>', '').replace('<br/> <br>', '\n').replace('									', '')
