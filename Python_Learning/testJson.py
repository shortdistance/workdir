#-------------------------------------------------------------------------------
# Name:        模块3
# Purpose:
#
# Author:      raychang
#
# Created:     22/09/2014
# Copyright:   (c) raychang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
from time import mktime
try:
    import simplejson as json
except ImportError:
    import json

class DateTimeEncoder(json.JSONEncoder):
    # 对 JSONEncoder 进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

d=datetime.datetime.now()
print json.dumps(d, cls = DateTimeEncoder)
# 使用 cls 指定编码器的名称