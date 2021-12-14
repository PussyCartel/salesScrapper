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
        pay_attention_block = response.css('div.special-promotion-card__wrapper')
        sale_name = pay_attention_block.css('div.special-promotion-card__text::text').getall()
        company_name = pay_attention_block.css('div.special-promotion-card__name::text').getall()
        for i in range(4):
            self.log(sale_name[i])
            self.log(company_name[i])
