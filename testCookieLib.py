import urllib2
import cookielib
cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
opener.open('http://www.baidu.com')
print cookie
