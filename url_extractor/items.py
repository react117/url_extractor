# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#
# Author: react117 
# Email: avikbhattacharyya.2k@gmail.com, avik@ai4bharat.org

import scrapy


class UrlExtractorItem(scrapy.Item):
    # The source URL
    url_from = scrapy.Field()

    # The destination URL
    url_to = scrapy.Field()
    