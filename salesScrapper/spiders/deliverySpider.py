import scrapy


class DeliveryScrapper(scrapy.Spider):
    name = 'Delivery'

    def start_requests(self):
        urls = [
            'https://www.delivery-club.ru/moscow/promo'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pass