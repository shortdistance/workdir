#-*- coding:utf-8 -*-
#使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}


retStr = pickle.dumps(data1)

print pickle.loads(retStr)