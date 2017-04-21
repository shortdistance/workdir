#-*- coding:utf-8 -*-
import urllib

#print urllib.getproxies()

#print urllib.localhost()
#print urllib.thishost()
help(urllib)
#proxies = {'http': 'http://zhangleid:1qaz2wsx@172.16.9.20:8088'}
#print urllib.urlopen('http://www.baidu.com', proxies=proxies).read()
'''
splitquery(url)
splittag(url)
splittype(url)

'''

'''
print urllib.ftperrors()
print urllib.splitquery('http://www.baidu.com?uname=zhanglei&pw=1aaa')
print urllib.splittag('http://www.baidu.com?uname=zhanglei&pw=1aaa')
print urllib.splittype('http://www.baidu.com?uname=zhanglei&pw=1aaa')

#print urllib.urlencode('~haha')
print urllib.unquote('http://172.16.9.106:9001+/svn/POD_JLMob_CRM6.0/4%e7%bc%96%e7%a0%81%e5%8f%8a%e5%8d%95%e5%85%83%e6%b5%8b%e8%af%95/46%e6%ba%90%e4%bb%a3%e7%a0%81/%e5%bc%80%e5%8f%91%e7%8e%af%e5%a2%83/crm6.0/').decode('utf-8')
print urllib.unquote_plus('http://172.16.9.106:9001+/svn/POD_JLMob_CRM6.0/4%e7%bc%96%e7%a0%81%e5%8f%8a%e5%8d%95%e5%85%83%e6%b5%8b%e8%af%95/46%e6%ba%90%e4%bb%a3%e7%a0%81/%e5%bc%80%e5%8f%91%e7%8e%af%e5%a2%83/crm6.0/').decode('utf-8')
'''
'''
print urllib.quote('~()@#a b$^')
print urllib.quote_plus('~()@#a b$^')
print urllib.pathname2url('c:\\usr\\bin\\local')

print urllib.splitattr('http://www.baidu.com/music;uname=zhanglei;pw=1aaa')
'''
url = '//172.21.0.106:9001/svn/qmd'
print urllib.splithost(url)

url = '172.21.0.106:9001'
print urllib.splitnport(url, -1)
print urllib.splitport(url)

user = 'zhangleid:1qaz2wsx'
print urllib.splitpasswd(user)

print urllib.splitquery('/path?query')

print urllib.splittag('/path#tag')

print urllib.splittype('type:opaquestring')

print urllib.splitvalue('attr=value')

print urllib.splituser('user:passwd@host:port')

print urllib.urlencode({ 'name': 'dark-bull', 'age': 200 })  


'''
import urllib
def callbackfunc(blocknum, blocksize, totalsize):
    #回调函数
    #@blocknum: 已经下载的数据块
    #@blocksize: 数据块的大小
    #@totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent
url = 'http://www.sina.com.cn'
local = 'd:\\sina.html'
print urllib.urlretrieve(url, local, callbackfunc)
urllib.urlcleanup()

'''
    

#help(urllib.URLopener)
#help(urllib.FancyURLopener)

proxies = {'http': 'http://zhangleid:1qaz2wsx@172.16.9.20:8088'}
openurl = urllib.FancyURLopener(proxies)
url = 'http://www.sohu.com'
fp = openurl.open(url)
print fp.read()