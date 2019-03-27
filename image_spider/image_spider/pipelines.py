# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImageSpiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            yield Request(image_url)
