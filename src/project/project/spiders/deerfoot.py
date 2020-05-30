# -*- coding: utf-8 -*-
import scrapy


class DeerfootSpider(scrapy.Spider):
    name = 'deerfoot'
    start_urls = ['http://www.deerfootinn.com/']

    def parse(self, response):
        pass
