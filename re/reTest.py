#-*-coding:utf-8-*-
__author__ = 'raychang'

import re
'''
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)

if m:
    print m.group(0), '\n', m.group(1)
else:
    print 'not match'
'''

#s1 = 'ip:[10.161.250.24] pa[CRM6/page/npage/score/s1250/s1250main.html] s[com_sitech_score_atom_inter_IScoreParamAoSvc_queryScoreParamList] [59]'

s2 = 'Quotes to Scrape'
m2 = re.match(r"(\w+) to (\w+)", s2)

if m2:
    print m2.group(0)
    print m2.group(1)
    print m2.group(2)
else:
    print 'not match'