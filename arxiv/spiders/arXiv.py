# -*- coding: utf-8 -*-
import scrapy
from arxiv.items import ArxivItem
from bs4 import BeautifulSoup


class ArxivSpider(scrapy.Spider):
    name = 'arXiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['https://arxiv.org/abs/1904.09130']

    def parse(self, response):
        script = response.text
        item = ArxivItem()
        item['name'] = BeautifulSoup(script,'html.parser')
        print(item['name'].title.contents[0])
        yield item
