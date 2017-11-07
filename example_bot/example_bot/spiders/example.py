from scrapy.spiders import BaseSpider
from example_bot.items import ExampleDotComItem

class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ['http://www.example.com']

    def parse(self, response):
        title = response.xpath('/html/body/div/h1/text()').extract()[0]
        description = response.xpath('/html/body/div/p[1]/text()').extract()[0]
        return ExampleDotComItem(title=title, description=description)