# -*- coding: utf-8 -*-
import scrapy
import re
from arxiv.items import *
from bs4 import BeautifulSoup


class ArxivSpider(scrapy.Spider):
    name = 'arXiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['https://arxiv.org/abs/1904.09130']

    def parse(self, response):
        essay = response.text
        soup = BeautifulSoup(essay,'html.parser')
        item = ArxivItem()
        item['title'] = soup.title.contents[0]
        item['abstract'] = soup.blockquote.contents[1]
        print(item['title'])
        yield item
