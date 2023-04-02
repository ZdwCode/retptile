# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_src = scrapy.Field()
    info_href = scrapy.Field()
    introduction = scrapy.Field()
    image_path = scrapy.Field()
