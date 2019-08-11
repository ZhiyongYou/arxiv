# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
from bs4 import BeautifulSoup

class ArxivPipeline(object):
    def process_item(self, item, spider):
        reg = re.compile(r'(WFCTA|LHAASO|Hillas)')
        match_value = {'WFCTA':2,'LHAASO':1,'Hillas':2}
        Relativity = 0

        soup = item['name']
        match = reg.finditer(soup.blockquote.contents[1])

        for matched in match:
            if matched:
                Relativity += match_value[matched.group(0)]

        if Relativity:
            with open("essay.txt",'a') as fp:
                fp.write("Relativity:")
                fp.write('%d' % Relativity)
                fp.write("\nTitle:"+soup.title.contents[0] + "\nAbstract:" + soup.blockquote.contents[1] + "\n")

