# -*- coding: utf-8 -*-
import scrapy
import re
from time import time
from datetime import datetime
from scrapy.selector import Selector
from trains.items    import TrainItem


class TrainSpider(scrapy.Spider):
    name = "Train"
    allowed_domains = ["tis.zsr.sk"]
    start_urls = (
        'http://tis.zsr.sk/elis/pohybvlaku',
    )

    def parse(self, response):
        selector = Selector(response)
        trains = selector.css('.accordionHeader')
        for train in trains:
            trainItem = TrainItem()
            
            spans = train.css('span::text').extract()
            
            trainItem['name'] = spans[0].encode("utf-8").strip()
            
            trainItem['time'] = datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:00')
            
            delayInfo = spans[1].encode("utf-8")
            delayInfo = delayInfo[11:-1]
            
            if delayInfo.endswith('išiel včas'):
                trainItem['delay'] = 0
                trainItem['station'] = delayInfo[:-13].strip()
            else:
                res = re.search('(.+)(?: mešká )([0-9]+) (?:minútu|minút|minútu)', delayInfo)
                
                trainItem['delay'] = res.group(2)
                trainItem['station'] = res.group(1).strip()
            
            yield trainItem
