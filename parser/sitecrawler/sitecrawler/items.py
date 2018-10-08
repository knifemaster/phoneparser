# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SitecrawlerItem(scrapy.Item):
    model_name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
   
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
