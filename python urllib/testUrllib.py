#-*- coding:utf-8 -*-
import urllib2, urllib
import sys
import re
import chardet
from bs4 import BeautifulSoup

error_msg = '查理没用...查不到...\nbtw,您听歌的品味真独特.\n您确认格式正确?(歌名@歌手名)\n好啦还是人家太弱了啦...TAT'


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
        # pretent to be IE. ^O^
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {}
        headers = {'User-Agent': user_agent}
        data = urllib.urlencode(values)
        req = urllib2.Request(myurl, data, headers)
        try:
            html = urllib2.urlopen(req).read()
            content_type = chardet.detect(html)['encoding']
            print content_type
            f = urllib2.urlopen(req).read()
            soup = BeautifulSoup(f, from_encoding='utf-8')
            print soup.encode('gb18030')

        except BaseException:
            return None
        song_urls = []
        try:
            pattern = r'<td class="song_name">\s*<a title="[\s\S]+?" class="slide_down" href="javascript:;"></a>\s*<a title="([\s\S]+?)" href="([\s\S]+?)" target="_blank"><b class="key_red">[\s\S]+?</b></a>\s*</td>'
            result = re.findall(pattern, html)
            # 0 --- song name ;   1 --- href ;
            print 'result~~~~~~~~~',  result

            for i in range(len(result)):
                if result[i][0].lower().find(args[0].lower()) != -1:
                    # if (len(args) < 2 or self.name_match(result[i][1].lower(), args[1].lower())):
                    if len(args) < 2:
                        song_urls.append(result[i][1])

        except BaseException:
            return None

        try:
            pattern = r'<div class="lrc_main">([\s\S]+?)</div>'
            req = urllib2.Request('http://www.xiami.com' + song_urls[0], data, headers)
            html = urllib2.urlopen(req).read()
            lrc = re.findall(pattern, html)[0]
        except BaseException:
            return None
        return self.process_lrc(lrc)


Content = '双节棍@周杰伦'
args = Content.split('@')
shark = SharkSearcher()

try:
    for i in range(len(args)):
        #args[i] = args[i].encode('utf8')  # pass test
        args[i] = args[i]  # pass test
    print args[i].decode('utf-8').encode('gbk')
    Content = shark.feed(args)
    if Content == None:
        Content = error_msg
    print 1
except BaseException:
    Content = error_msg
    print 2

print Content.decode('utf-8').encode('gbk')
