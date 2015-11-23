# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrainItem(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()
    delay = scrapy.Field()
    station = scrapy.Field()
    pass
