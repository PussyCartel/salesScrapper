# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeliveryItem(scrapy.Item):
    product_name = scrapy.Field()
    product_company = scrapy.Field()
