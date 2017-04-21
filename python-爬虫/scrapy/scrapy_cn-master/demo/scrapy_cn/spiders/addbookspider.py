#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
#from urlparse import urljoin
from scrapy_cn.items import ScrapyCnItem
from scrapy import log
#from scrapy.contrib.loader import ItemLoader

class AddbookSpider(Spider):
    """Crawl <book.douban.com>
       crawling only one page
       save data to db and json with utf-8
    """
    name = "onepage"
    base_domain = "book.douban.com"
    start_urls = [
            "http://book.douban.com/tag/Programming"
            ]

    def parse(self, response):
        doc = Selector(response)
        item = ScrapyCnItem()
        sect = doc.xpath("//li[@class='subject-item']")
        for s in sect:
            title = s.xpath(".//div[@class='info']//a/@title").extract()
            href = s.xpath(".//div[@class='info']//a/@href").extract()
            img = s.xpath(".//div[@class='pic']//img/@src").extract()
            desc = s.xpath(".//div[@class='info']/p/text()").extract()
            item["title"] = [t.encode('utf-8') for t in title]
            item["img"] = [i.encode('utf-8') for i in img]
            item["desc"] = [d.encode('utf-8') for d in desc]
            yield item


class MultiPageSpider(Spider):
    """Crawl <book.douban.com>
       Crawl multipages
    """
    name = "multipage"
    base_domain = "book.douban.com"
    start_urls = [
            "http://book.douban.com/tag/Programming"
            ]

    def parse(self, response):
        """Many method you can crawl multipages
           here we use callbacks with pagination items.
        """
        doc = Selector(response)
        item = ScrapyCnItem()
        section = doc.xpath("//li[@class='subject-item']")
        next_link = doc.xpath("//div[@class='paginator']//span[@class='next']//a/@href").extract()
        url = self.next_link(next_link)
        for s in section:
            title = s.xpath(".//div[@class='info']//a/@title").extract()
            href = s.xpath(".//div[@class='info']//a/@href").extract()
            img = s.xpath(".//div[@class='pic']//img/@src").extract()
            desc = s.xpath(".//div[@class='info']/p/text()").extract()
            item["title"] = [t.encode('utf-8') for t in title]
            item["img"] = [i.encode('utf-8') for i in img]
            item["desc"] = [d.encode('utf-8') for d in desc]
            yield item
        if url:
            yield Request(url, callback=self.parse, dont_filter=True)

    def next_link(self, url):
        if not url:
            return None
        if isinstance(url, list):
            if len(url)==0:
                return None
            in_link = url[0]
            if self.base_domain in in_link:
                return in_link
            link = unicode("http://{domain}{uri}").format(domain=self.base_domain, uri=in_link)
            return link
