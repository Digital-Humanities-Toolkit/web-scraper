import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# command to run: scrapy runspider emily_dickinson/spiders/wikipedia-emily-spider.py -o emily_dickinson_wikipedia.json


class PoemItem(scrapy.Item):
    poem_title = scrapy.Field()
    poem_text = scrapy.Field()


class PoemSpider(CrawlSpider):
    name = "poems"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems"]

    rules = (
        Rule(
            LinkExtractor(allow=("List_of_Emily_Dickinson_poems")),
            callback="parse_item",
        ),
    )

    def parse_item(self, response):
        item = PoemItem()
        item["poem_title"] = response.xpath("//h1/text()").get()
        item["poem_text"] = response.xpath("//poem/text()").getall()

        return item
