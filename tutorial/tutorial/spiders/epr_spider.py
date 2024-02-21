import scrapy
import json
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
            item['thumbnail'] = element.css('div.thumb-art::attr(style)').getall()

            yield item

        # Export data to JSON file with titles and index
        self.export_to_json(response)

    # def export_to_json(self, response):
    #     data = response.css('article.news-item')

    #     result = [dict((key, value) for key, value in EprScrapyItem(item).items()) for item in data]

    #     # Save data to a JSON file with line breaks
    #     with open('output.json', 'w', encoding='utf-8') as json_file:
    #         json.dump(result, json_file, indent=2, ensure_ascii=False)
