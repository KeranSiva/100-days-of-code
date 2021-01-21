# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class GinwebscrapingItem(scrapy.Item):
    # # Allgemeine Produkt Details
    # produkt_name = Field()
    # preis_original = Field()
    # preis_sale = Field()
    # volume_liter = Field()
    # artikel_number = Field()
    # ean_number = Field()
    # gewicht = Field()
    # menge_vorhanden = Field()

    # # Geschmackliche Details
    # herkunft = Field()
    # region = Field()
    # botanicals = Field()
    # geschmack = Field()
    # sorte  = Field()
    # alkoholgehalt = Field()
    # bio_siegel = Field()
    # bio_kontrollnummer = Field()
    # unternehmer = Field()

    
    # #items to store links
    # image_link = Field()
    # product_link=Field()

    # #item for company name
    # company = Field()

    pass

class ImgData(Item):
    
    #image pipline items to download product images
    image_urls = scrapy.Field()
    images = scrapy.Field()
