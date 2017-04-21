#-*- coding:utf-8 -*-

from xml.dom import minidom
import os
import re

import chardet

def get_charset(s):
    return chardet.detect(s)['encoding']

def replaceXmlEncoding(filepath, oldEncoding='gbk', newEncoding='utf-8'):
    f = open(filepath, mode='r')
    content = f.read()
    content = re.sub(oldEncoding, newEncoding, content)
    f.close()

    f = open(filepath, mode='w')
    f.write(content)
    f.close()


def AnalyseXML(xmlfile):
    if not os.path.isfile(xmlfile):
        return []
  
    #replaceXmlEncoding(xmlfile)  
    fp = open(xmlfile, 'r')
    s = fp.read()
    old_charset = get_charset(s)
    print old_charset    

    file_xml = open(xmlfile,"r").read()
    file_xml = file_xml.replace('<?xml version="1.0" encoding="gbk"?>','<?xml version="1.0" encoding="utf-8"?>')

    print file_xml.decode(old_charset).encode('gbk')
    doc  = minidom.parseString(file_xml)
  
    #doc = minidom.parse(xmlfile)
  
    # get root element: <employees/>
    root = doc.documentElement
  
    # get all children elements: <entry/> <entry/>
    entrys = root.getElementsByTagName("entry")
  
    i = 0
    for entry in entrys:
        i = i + 1
        print("---------------------%d----------------------" % i)
        # element name : entry
        print (entry.nodeName)

        # element xml content : <employee><name>windows</name><age>20</age></employee>
        # basically equal to toprettyxml function
        # print entry.toxml()
    
        requestNode = entry.getElementsByTagName("request")[0].toxml()       
        print requestNode.decode(old_charset1).encode('gbk')
    
        #print (nameNode.nodeName + ":" + nameNode.childNodes[0].nodeValue)
        responseNode = entry.getElementsByTagName("response")[0].toxml()        
        print responseNode.decode(old_charset2).encode('gbk')

    
        #print (ageNode.nodeName + ":" + ageNode.childNodes[0].nodeValue)
    
        print("-------------------------------------------")

if __name__ == '__main__':
    AnalyseXML('C:\\Users\\raychang\\Desktop\\123.xml')


'''
import xml.etree.ElementTree as ET

#读取xml文件
def load_xml_file(fileName):
    root = ET.parse(fileName).getroot()
    print root

    #获取所有list节点
    all_entrys = root.findall("entry")
    print all_entrys
    #遍历list节点的子元素
    for entry in all_entrys:
        print entry
        #得到head节点的文本
        requestStr = entry.find('request').text
        #得到name节点的文本
        responseStr = entry.find('response').text
        print requestStr,  responseStr
        

if __name__ == '__main__':
    load_xml_file('C:\\Users\\raychang\\Desktop\\123.xml')
'''