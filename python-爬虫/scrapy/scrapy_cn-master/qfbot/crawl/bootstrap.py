#!/usr/bin/env python
# encoding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: YuanLin

from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import Crawler
#from model import Spider
from scrapy import log, signals
from .spiders import crawlspider

import datetime
import json
from billiard import Process

class CrawlStack(Process):
    _crawl_running = 0

    def add_crawler(self):
        self._crawl_rinning += 1

    def remove_crawler(self):
        self._crawl_rinning -= 1
        if not self._crawl_running > 0:
            reactor.stop()

    def __init__(self, name):
        super(CrawlStack, self).__init__(self)
        self.name = name

    def _setup(self, project):
        spider = crawlspider.LinkSpider(project)
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.configure()
        crawler.crawl(spider)
        self.add_crawler()

    def _crawl_detail(self, project):
        pass

    def run(self):
        self._setup(self.name)
        log.start()
        reactor.run()

    def _done_link_ring(self, spider):
        pass

    def _done_detail_ring(self, spider):
        pass
