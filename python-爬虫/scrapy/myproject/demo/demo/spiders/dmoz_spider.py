from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Society/Philosophy/Aesthetics/",
        "http://www.dmoz.org/Sports/Football/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)