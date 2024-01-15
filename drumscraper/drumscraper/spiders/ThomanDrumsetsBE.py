import scrapy


class ThomandrumsetsbeSpider(scrapy.Spider):
    name = "ThomanDrumsetsBE"
    allowed_domains = ["www.thomann.de"]
    start_urls = ["http://www.thomann.de/"]

    def parse(self, response):
        pass
