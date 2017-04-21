#!/usr/bin/env python
# encoding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: YuanLin

from mongokit import *
import datetime
import hashlib

__all__ = ['Project', 'Linkbase']

connection = Connection()

@connection.register
class Project(Document):
    __database__ = 'crawlto'
    __collection__ = 'project'

    structure = {
            'name':unicode,
            'desc':unicode,
            'created':datetime.datetime,
            'author':unicode,

            # Use to select spiders type and create an spider obj.
            'setup':{
                'seed':unicode,
                'method':unicode,
                'format':unicode,
                'ring_type':unicode
            },

            'handle':{
                'next':{},
                'end':{},
                'expired':{},
                'update':{}
            },

            # Parse factory that can set for particular pages.
            'parse':{
                'ring':unicode,
                'regex':unicode,
                'xpath':unicode,
            }
    }
    required_fields = ['name', 'created']
    default_values = {'created':datetime.datetime.utcnow}

@connection.register
class Linkbase(Document):
    __database__ = 'crawlto'
    __collection__ = 'linkbase'

    structure = {
            'link':unicode,
            'active':bool,
            'pagerank':int,
            'type':unicode,
            'created':datetime.datetime,
            'updated':datetime.datetime,
    }
    required_fields = ['link', 'created', 'type', 'pagerank', 'active']
    default_values = {'created':datetime.datetime.utcnow}
