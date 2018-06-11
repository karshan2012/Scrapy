# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
import asyncio

class FullolxSpider(scrapy.Spider):
    name = 'fullolx'
    def __init__(self, location='', category='', **kwargs):
        self.start_urls=['https://www.olx.in/%s/%s/' % (location,category)]
        print(self.start_urls)
        self.pages = []
        self.urls = {}
        allowed_domains = []
        self.sem = asyncio.Semaphore(1)
        super().__init__(**kwargs)

    def parse(self, response):
	#Extracting the content using css selectors
        titles = response.xpath('//*[starts-with(@class, "block br3 brc8 large tdnone lheight24")]//span//text()').extract()
        for i in titles:
            last_index = i
        for j in range(2,int(last_index)):
            self.pages.append(''.join(str(e) for e in self.start_urls)+'?page='+str(j))
        print(self.pages)

        for k in self.pages:
            yield  Request(url=k, callback = self.parse_page)
        pass

    def parse_page(self, response):
        item = response.xpath('//*[starts-with(@class, "marginright5 link linkWithHash detailsLink")]/@href').extract()
        for i in item:
            with (yield from self.sem):
                yield Request(url=i, callback = self.parse_url)        
        pass

    def parse_url(self, response):
        titles = response.xpath('//*[starts-with(@class, "brkword")]//text()').extract()
        adid = response.xpath('//*[starts-with(@class, "pdingleft10 brlefte5")]//text()').extract()
        locality = response.xpath('//*[starts-with(@class, "c2b small")]//text()').extract()
        model = response.xpath('//*[starts-with(@class, "brkword")]//text()').extract()
        price = response.xpath('//*[starts-with(@class, "xxxx-large margintop7 inlblk not-arranged")]//text()').extract()
        details = response.xpath('//*[starts-with(@class, "details")]//text()').extract()
        adidd=''
        for i in adid:
            adidd = adidd + " " + re.sub('\s+',' ',str(i))
        adidd = tuple([adidd])
        detailss = ''
        for j in details:
            detailss = detailss + " " + re.sub('\s+',' ',str(j))
        detailss = tuple([detailss])

	#Give the extracted content row wise
        for items in zip(titles,adidd,locality,model,price,detailss):
            item_new = re.sub('\s+',' ',str(items[0]))
            adid_new = re.sub('\s+',' ',str(items[1]))
            locality_new = re.sub('\s+',' ',str(items[2]))
            model_new = re.sub('\s+',' ',str(items[3]))
            price_new = re.sub('\s+',' ',str(items[4]))
            details_new = re.sub('\s+',' ',str(items[5]))
            
            #print(item_new)
            #print(adid_new)
            #print(locality_new)
            #print(model_new)
            #print(price_new)
            #print(details_new)
            scraped_info = {
                'Item' : item_new,
                'Price' : price_new,
                'Ad ID' : adid_new,
                'Location' : locality_new,
                'Model' : model_new,
                'Details' : details_new,
            }
            yield scraped_info
        pass
