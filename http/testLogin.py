#!/usr/bin/python  
#coding:utf-8

import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  
hosturl = 'http://127.0.0.1:11001/'   
posturl = 'http://127.0.0.1:11001/Login'  
  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
h = urllib2.urlopen(hosturl) 

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',  
           'Referer' : 'http://127.0.0.1:11001/'}  
postData = { "Email":"admin@admin.com","Password":"admin"}
  
postData = urllib.urlencode(postData)  
  
request = urllib2.Request(posturl, postData, headers)  
print request.get_data()
response = urllib2.urlopen(request)  
text = response.read()  
print text  