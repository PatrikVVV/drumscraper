import scrapy


class ThomandrumsetsSpider(scrapy.Spider):
    name = "ThomanDrumsets"
    allowed_domains = ["www.thomann.de"]
    start_urls = ["http://www.thomann.de/"]

    def parse(self, response):
        pass
