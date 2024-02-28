import scrapy
from tutorial.items import EprScrapyItem


class EprSpider(scrapy.Spider):
    name = 'epr'
    allowed_domains = ['epr.monre.gov.vn']
    start_urls = [
        "https://epr.monre.gov.vn/vi/tin-tuc/"  
    ]

    def parse(self, response):
        # self.logger.info('Processing link %s', response.url)
        for item_url in response.css('a.is-media-card::attr(href)').extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_item)
    def parse_item(self, response): 
        # self.logger.info('Processing item %s', response.url)
        item = EprScrapyItem()
        item['title'] = response.css("div.epr-section-menu-label__wrapper span::text").getall()
        description =  response.css("div.row em::text").extract_first()
        if description: 
            item['description'] = description
        else:
            item['description'] = response.css("div.row p::text").extract_first()
        yield item

