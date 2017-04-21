#-------------------------------------------------------------------------------
# Name:        ģ��3
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
    # �� JSONEncoder ������չ
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

d=datetime.datetime.now()
print json.dumps(d, cls = DateTimeEncoder)
# ʹ�� cls ָ��������������