import scrapy


class BoldrumsetsSpider(scrapy.Spider):
    name = "BolDrumsets"
    allowed_domains = ["www.bol.com"]
    start_urls = ["http://www.bol.com/"]

    def parse(self, response):
        pass
