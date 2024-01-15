import scrapy


class BoldrumsetsbeSpider(scrapy.Spider):
    name = "BolDrumsetsBE"
    allowed_domains = ["www.bol.com"]
    start_urls = ["http://www.bol.com/"]

    def parse(self, response):
        pass
