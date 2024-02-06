import scrapy
from tutorial.items import EprScrapyItem

class EprSpider(scrapy.Spider):
    name = 'epr'
    allowed_domains = ['epr.monre.gov.vn']
    start_urls = [
        'https://epr.monre.gov.vn/vi/'
    ]

    def parse(self, response):
        data = response.css('article.news-item')

        for element in data:
            item = EprScrapyItem()
            item['title'] = element.css('h3 a::text').getall()
            slug = element.css('h3 a::attr(href)').getall()
            item['slug'] = ['https://epr.monre.gov.vn/vi/' + s for s in slug]
            item['description'] = element.css('a.description::text').getall()
            # item['thumnail'] = element.css('div.thumb-art::attr(style)').getall()
                              
            yield item
        # Kiểm tra và theo dõi các trang tiếp theo nếu có
        # next_page = response.css('a.next::attr(href)').extract_first()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
