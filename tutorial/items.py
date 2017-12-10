# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#item用scrapy.item.Item类创建，并且用scrapy.item.Field 对象来定义属性（可以理解成类似于ORM映射关系）
from scrapy import Item,Field
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class doubanItem(Item):
    title = Field()
    movieInfo = Field()
    star =Field()
    quote =Field()




