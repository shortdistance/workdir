#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: YuanLin
# Created: 2015-07-25 13:32 CST


from tornado import web
from tornado import template
import json
from bson import json_util
import logging


class BaseHandler(web.RequestHandler):

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

    @property
    def db(self):
        return self.application.db

    @property
    def rdc(self):
        return self.application.rdc

    @property
    def loader(self):
        return template.Loader(self.application.template)

    def render_error(self, code, msg):
        data = {"code": code, "detail": msg}
        self.write_json(data)

    def load_body(self):
        try:
            data = json.loads(self.request.body)
        except Exception, e:
            logging.error(e)
            return None
        return data

    def write_json(self, data):
        """
        处理响应请求的json数据
        更改为异步I/O的方式读写
        """
        msg = json.dumps(data,  default=json_util.default)
        self.write(msg)

