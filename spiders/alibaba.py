# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
import asyncio

class AlibabaSpider(scrapy.Spider):
    name = 'alibaba'
    def __init__(self, **kwargs):
        self.start_urls=['https://www.alibaba.com//Home-Textile-Product-Machinery_pid4304?spm=a2700.8270666-43.201612262000.38.2ebd2f91vqk1pf']
        for i in range(2,271):
            self.start_urls = self.start_urls + ['https://www.alibaba.com/catalogs/products/CID4304----------------------------G--------------------------Home-Textile-Product-Machinery/'+str(i)]
        print(self.start_urls)
        self.pages = []
        self.urls = {}
        allowed_domains = []
        self.sem = asyncio.Semaphore(1)
        super().__init__(**kwargs)

    def parse(self, response):
	#Extracting the content using css selectors
        for k in self.start_urls:
            yield  Request(url=k, callback = self.parse_page)
        pass

    def parse_page(self, response):
        item = response.xpath('//*[starts-with(@class, "util-valign-ctn ")]/@href').extract()
        for i in item:
            with (yield from self.sem):
                yield Request(url=i, callback = self.parse_url)        
        pass

    def parse_url(self, response):
        titles = response.xpath('//*[starts-with(@class, "ma-title")]//h1//text()').extract()
        price = response.xpath('//*[starts-with(@class, "ma-reference-price")]//span//text()').extract()
        supply_ability = [re.sub('\s+',' ',response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()[0])]
        port = [re.sub('\s+',' ',response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()[1])]

	#Give the extracted content row wise
        for items in zip(titles,price,supply_ability,port):
            scraped_info = {
                'Item' : titles,
                'Price' : price,
                'Supply Ability' : supply_ability,
                'Port' : port,
            }
            yield scraped_info
        pass
