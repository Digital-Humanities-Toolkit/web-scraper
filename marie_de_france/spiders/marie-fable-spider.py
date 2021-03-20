import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PoemItem(scrapy.Item):
    poem_title = scrapy.Field()
    poem_text = scrapy.Field()


class PoemSpider(CrawlSpider):
    name = "fables"
    allowed_domains = ["fr.m.wikisource.org"]
    start_urls = [
        "https://fr.m.wikisource.org/wiki/Poésies_de_Marie_de_France_(Roquefort)"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=("Poésies_de_Marie_de_France_(Roquefort)")),
            callback="parse_item",
        ),
    )

    def parse_item(self, response):
        item = PoemItem()
        item["poem_title"] = response.xpath("//h1/text()").get()
        item["poem_text"] = response.css(".poem").xpath("//p/text()").getall()

        return item
