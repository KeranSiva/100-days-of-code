import scrapy


class DebuggerSpider(scrapy.Spider):
    name = 'debugger'
    allowed_domains = ['wacholder-express.de']
    start_urls = ['https://wacholder-express.de/gin/?p=1']

    def parse(self, response):
        pass
