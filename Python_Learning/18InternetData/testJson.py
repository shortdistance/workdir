#-*- coding:utf-8 -*-

import json
import StringIO

data1 = {'b':789,'c':456,'a':123} 
fp = StringIO.StringIO()

json.dump(data1,fp,sort_keys=True,indent=4,ensure_ascii=False,separators=(',',':'))
print fp.read()
fp.close()

'''
d1 = json.dumps(data1,sort_keys=True,indent=4,ensure_ascii=False,separators=(',',':')) 
print d1


d2 = json.loads(d1)
print d2

'''
