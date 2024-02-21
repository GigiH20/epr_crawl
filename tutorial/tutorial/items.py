# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class EprScrapyItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    slug = scrapy.Field()
    thumbnail = scrapy.Field()