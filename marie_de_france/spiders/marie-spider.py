import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PoemItem(scrapy.Item):
    poem_title = scrapy.Field()
    poem_text = scrapy.Field()


class PoemSpider(CrawlSpider):
    name = "poems"
    allowed_domains = ["fr.m.wikisource.org"]
    start_urls = ["https://fr.m.wikisource.org/wiki/Lais_de_Marie_de_France"]

    rules = (
        Rule(LinkExtractor(allow=("Lais_de_Marie_de_France")), callback="parse_item"),
    )

    def parse_item(self, response):
        item = PoemItem()
        item["poem_title"] = response.xpath("//h1/text()").get()
        item["poem_text"] = response.css(".poem").xpath("//p/text()").getall()

        return item
