#-*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print root._children