# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
import asyncio

class MoneyControlSpider(scrapy.Spider):
    name = 'moneycontrol'
    cnt = 0
    start_urls = []
    def __init__(self, **kwargs):
        #self.start_urls=['https://www.alibaba.com/Agriculture-Machinery-Equipment_pid100009395?spm=a2700.7724856.scGlobalHomeHeader.47.16e3606bhq4J8b']
        #self.start_urls=[]
        for i in range(12,1,-1):
            self.start_urls.append('https://www.moneycontrol.com/stocks/hist_stock_result.php?sc_id=RI&pno='+str(i)+'&hdn=daily&fdt=2000-01-01&todt=2018-06-09')
        print(self.start_urls)
        #for k in self.start_urls:
         #   yield  Request(url=k, callback = self.parse_url)
        self.pages = []
        self.urls = {}
        allowed_domains = []
        self.sem = asyncio.Semaphore(1)
        super().__init__(**kwargs)

    '''def parse(self, response):
	#Extracting the content using css selectors
        for k in self.start_urls:
            yield  Request(url=k, callback = self.parse_url)
        pass'''

    '''def parse_page(self, response):
        item = response.xpath('//*[starts-with(@class, "title")]//@href').extract()
        #print(item)
        for i in item:
            with (yield from self.sem):
                yield Request(url=i, callback = self.parse_url)        
        pass'''

    def parse(self, response):
        titles = response.xpath('//table[@class="tblchart"]//td')
        date = []
        opeen = []
        high = []
        low = []
        close = []
        volume = []
        high_low = []
        opeen_close = []
        j = 0
        for i in range(0,len(titles),8):
            scraped_info = {                                      
                'Date' : titles[i].select('.//text()').extract()[0],
                'Open' : titles[i+1].select('.//text()').extract()[0],
                'High' : titles[i+2].select('.//text()').extract()[0],
                'Low' : titles[i+3].select('.//text()').extract()[0],
                'Close' : titles[i+4].select('.//text()').extract()[0],
                'Volume' : titles[i+5].select('.//text()').extract()[0],
                'High-Low' : titles[i+6].select('.//text()').extract()[0],
                'Open-Close' : titles[i+7].select('.//text()').extract()[0],
            }
            yield scraped_info
            #print("\n")
        #Give the extracted content row wise
        '''for items in zip(date,opeen,high,low,close,volume,high_low,opeen_close):
            scraped_info = {
                'Date' : date,
                'Open' : opeen,
                'High' : high,
                'Low' : low,
                'Close' : close,
                'Volume' : volume,
                'High-Low' : high_low,
                'Open-Close' : opeen_close,
            }
            yield scraped_info'''
        pass
