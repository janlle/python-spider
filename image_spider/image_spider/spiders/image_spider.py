# !/usr/bin/python
# encoding:utf-8

import scrapy
from image_spider.items import ImageSpiderItem


class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    allowed_domain = ['lab.scrapyd.cn/']
    start_url = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        # 实例化item
        item = ImageSpiderItem()
        # 得到的是一个集合即多张图片
        image_urls = response.css(".post img::attr(src)").extract()
        item['image_url'] = image_urls
        yield item
        pass
