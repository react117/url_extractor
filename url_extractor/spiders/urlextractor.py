# -*- coding: utf-8 -*-
from url_extractor.items import UrlExtractorItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import scrapy


class UrlextractorSpider(CrawlSpider):
    # The name of the spider
    name = "urlextractor"

    # The domains that are allowed (links to other domains are skipped)
    # allowed_domains = ["fundrazr.com"]
    # allowed_domains = ["data-blogger.com"]
    allowed_domains = ["anandabazar.com"]

    # The URLs to start with
    # start_urls = ["http://fundrazr.com/"]
    # start_urls = ["https://www.data-blogger.com/"]
    start_urls = ["https://www.anandabazar.com"]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(
            canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = UrlExtractorItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        # Return all the found items
        return items
