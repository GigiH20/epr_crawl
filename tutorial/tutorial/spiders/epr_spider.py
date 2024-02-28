import scrapy
from tutorial.items import EprScrapyItem

class EprSpider(scrapy.Spider):
    name = 'epr'
    allowed_domains = ['epr.monre.gov.vn']
    start_urls = [
        "https://epr.monre.gov.vn/vi/"
    ]

    def parse(self, response):
        data = response.css('article.news-item')

        for element in data:
            item = EprScrapyItem()
            item['title'] = element.css('h3 a::text').getall()
            slug = element.css('h3 a::attr(href)').getall()
            item['slug'] = ['https://epr.monre.gov.vn/vi/' + s for s in slug]
            item['description'] = element.css('a.description::text').getall()
            thumbnails = element.css('div.thumb-art::attr(style)').get()
            item['thumbnail'] = thumbnails.split('/')[-1]  
            yield item