# -*- coding: utf-8 -*-
import scrapy
import re
from arxiv.items import *
from bs4 import BeautifulSoup


class ArxivSpider(scrapy.Spider):
    name = 'arXiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['https://arxiv.org/list/astro-ph/1904?show=10000']
    #start_urls = ['https://arxiv.org/abs/1904.09130']

    def parse(self, response):
        regular = re.compile(r'/abs/\d{4}.\d{5}')
        lis = response.text
        for href in regular.findall(lis):
            try:
                url = 'https://arxiv.org'+href
                print(url)
                yield scrapy.Request(url,callback=self.parse_essay)
            except:
                continue

    def parse_essay(self, response):
        essay = response.text
        soup = BeautifulSoup(essay,'html.parser')
        item = ArxivItem()
        item['title'] = soup.title.contents[0]
        item['abstract'] = soup.blockquote.contents[1]
        print(item['title'])
        yield item
