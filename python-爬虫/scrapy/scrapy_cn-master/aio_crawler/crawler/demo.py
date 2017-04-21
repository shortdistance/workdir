#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: YuanLin
# Created: 2015-07-25 13:01 CST

import aiohttp
import asyncio


def get_body(url):
    res = yield from aiohttp.request("GET", url)
    return (yield from res.read())

if __name__ == '__main__':
    loop = ayscio.get_event_loop()
    raw_html = loop.run_until_complete(get_body('scu.qfboys.com'))
    print raw_html

