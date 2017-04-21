#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: YuanLin
# Created: 2015-07-25 11:33 CST

"""
    当crawler执行过程中需要就绪数据时，使用此db工具
"""

from pymongo.connection import MongoClient

from .. import settings


class MongoCursor(object):

    def __init__(self):
        client = MongoClient(settings.MONGO_URI)
        self._db = client[settings.MONGO_DB]

    @property
    def crawler(self):
        return self._db

    @property
    def production(self):
        return self._db["production"]

    @property
    def sandbox(self):
        return self._db["sandbox"]

    @property
    def rawdata(self):
        return self._db["rawdata"]

    @property
    def debug(self):
        return self._db["debug"]

    @property
    def old(self):
        return self._db["old"]

    @property
    def consumer(self):
        return self._db["consumer"]

    @property
    def linkbase(self):
        return self._db['linkbase']

    @property
    def user(self):
        return self._db["user"]

conn = MongoCursor()

__all__ = ["conn"]