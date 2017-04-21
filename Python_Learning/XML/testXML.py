#-------------------------------------------------------------------------------
# Name:        ģ��
# Purpose:
#
# Author:      raychang
#
# Created:     29/09/2014
# Copyright:   (c) raychang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import xml.etree.ElementTree as ET
fp = open('C:\\Users\\raychang\\Desktop\\123.xml','r')
tree = ET.ElementTree()
tree.parse(fp)
print tree
ne = tree.findall("entry")
for n in ne:
    print n
fp.close()
root = tree.getroot()
'''
print tree.findtext('//year')
tree.write('C:\\1.txt',
encoding="gbk",
method="html")

if tree.find('.//year'):
    print 'OK'*5
'''
#print "#tag:", root.tag, "#text:", root.text, "#tail:", root.tail, "#attrib:", root.attrib
'''
for child in root:
    print child.tag, child.attrib

print root[0][0].tag,root[0][0].attrib,root[0][0].text

for neighbor in root.iter('gdppc'):
    print neighbor.text

ET.SubElement(root, 'hello')
ET.dump(root)

'''

'''
country_data_as_string = \
<?xml version="1.0" encoding="UTF-8" ?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''


'''
print country_data_as_string
try:
    root1 = ET.fromstring(country_data_as_string)
    print root1
except Exception,e:
    print e

if root1:
    print '#'*20
    ET.dump(root1)

print ET.iselement(root1)

print ET.iterparse('country_data.xml')

Co = ET.Comment(text='hello world')
print Co.text
'''
