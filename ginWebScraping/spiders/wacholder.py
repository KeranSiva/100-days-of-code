import scrapy
from ginWebScraping.items import GinwebscrapingItem
from ginWebScraping.items import ImgData
from scrapy.http import Request

import csv


class WacholderSpider(scrapy.Spider):
    name = 'wacholder'
    allowed_domains = ['wacholder-express.de']
    start_urls = ['http://wacholder-express.de/']

    def start_requests(self):
        with open ("./csvFiles/url.csv", "rU") as file:
            reader = csv.DictReader(file)

            for row in reader:
                url = row['url']
                link_urls = [url.format(i) for i in range(1, 39)]

                for link_url in link_urls:
                    print(link_url)
                    request = Request(link_url, callback=self.parse_product_pages, meta ={'type': row['type']})

                    yield request





    def parse_product_pages(self, response):

        #item = GinwebscrapingItem()


		# Get the HTML block where all the products are listed
		# <div> HTML element with the "listing--container" class name
		product_list = response.css('.listing--container')
        products = product_list.css('.product--box')


        gin = products[0].css('.product--title')






        pass


