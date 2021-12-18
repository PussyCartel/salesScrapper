import scrapy
from salesScrapper.items import DeliveryItem


class DeliveryScrapper(scrapy.Spider):
    name = 'Delivery'

    def start_requests(self):
        urls = [
            'https://www.delivery-club.ru/moscow/promo'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = DeliveryItem()
        pay_attention_block = response.css('div.special-promotion-card__wrapper')
        product_name = pay_attention_block.css('div.special-promotion-card__text::text').getall()
        product_company = pay_attention_block.css('div.special-promotion-card__name::text').getall()

        for i in range(len(product_name)):
            product_name[i] = product_name[i][:53]
            product_company[i] = product_company[i][:53]

        item['product_name'] = product_name
        item['product_company'] = product_company
        return item

