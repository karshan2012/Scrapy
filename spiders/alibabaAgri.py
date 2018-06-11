# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
import asyncio

class AlibabaAgrySpider(scrapy.Spider):
    name = 'alibabaAgry'
    cnt = 0
    start_urls = []
    def __init__(self, **kwargs):
        #self.start_urls=['https://www.alibaba.com/Agriculture-Machinery-Equipment_pid100009395?spm=a2700.7724856.scGlobalHomeHeader.47.16e3606bhq4J8b']
        #self.start_urls=[]
        for i in range(20,25):
            self.start_urls.append('https://www.alibaba.com/catalogs/products/CID100009395----------------------------G--------------------------Agriculture-Machinery-Equipment/'+str(i))
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
        item = response.xpath('//*[starts-with(@class, "title")]//@href').extract()
        #print(item)
        for i in item:
            with (yield from self.sem):
                yield Request(url=i, callback = self.parse_url)        
        pass

    def parse_url(self, response):
        titles = [(response.xpath('//*[starts-with(@class, "ma-title")]//h1//text()').extract()[0]).replace(",","")]
        if len(response.xpath('//*[starts-with(@class, "ma-ref-price")]//text()').extract()) == 4:
            price_currency = [response.xpath('//*[starts-with(@class, "ma-ref-price")]//text()').extract()[0].replace(",","")]
            price_start = [response.xpath('//*[starts-with(@class, "ma-ref-price")]//text()').extract()[1].replace(",","")]
            price_end = [response.xpath('//*[starts-with(@class, "ma-ref-price")]//text()').extract()[3].replace(",","")]
        elif len(response.xpath('//*[starts-with(@class, "ma-ref-price")]//text()').extract()) != 4:
            price_currency = 'NA'
            price_start = '0'
            price_end = '0'
        
        min_order = [(response.xpath('//*[starts-with(@class, "ma-min-order")]//text()').extract()[0]).replace(",","")]
        
        if len(response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()) == 2:
            supply_ability = [re.sub('\s+',' ',response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()[0].replace(",",""))]
            port = [re.sub('\s+',' ',response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()[1].replace(",",""))]
        elif len(response.xpath('//*[starts-with(@class, "ma-brief-item-val")]//text()').extract()) != 2:
            supply_ability = "NA"
            port = "NA"
        
        img = response.xpath('//*[starts-with(@class, "thumb")]//@src').extract()
        if img is None:
            img = response.xpath('//*[starts-with(@class, "pic")]//@src').extract()
        image = ''
        for i in img:
            url_appender = ''
            if i not in 'http':
                url_appender = 'http:'
            image = image + url_appender+ i + ' '

	#Give the extracted content row wise
        for items in zip(titles,price_currency,price_start,price_end,min_order,supply_ability,port,img):
            scraped_info = {
                'Item' : titles,
                'Price Currency' : price_currency,
                'Price Start' : price_start,
                'Price End' : price_end,
                'Minimum Order' : min_order,
                'Supply Ability' : supply_ability,
                'Port' : port,
                'Url' : response.request.url,
                'Image' : image,
            }
            yield scraped_info
        pass
