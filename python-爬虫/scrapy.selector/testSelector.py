#coding:utf-8
from scrapy import Selector

doc = '''
 <div>
     <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
sel = Selector(text=doc, type="html")
print sel.css('li a::attr(href)').extract()
print sel.xpath('//li//@href').extract()   #返回元素link

print sel.css('li::attr(class)').extract()
print sel.xpath('//li//@class').extract()   #返回元素

print sel.css('a[href*=link]::attr(href)').extract()
print sel.xpath('//a[contains(@href, "link")]/@href').extract()

print sel.css('div ul li[class*=item]::attr(class)').extract()
print sel.xpath('//li[contains(@class,"item")]/@class').extract()

print sel.css('div ul li[class*=item] a[href*=link]::attr(href)').extract()
print sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()

print sel.xpath('//a[contains(@href, "link")]/text()').re(r'(.*)\s+item')
print sel.xpath('//a[contains(@href, "link")]/text()').re_first(r'(.*)\s+item')