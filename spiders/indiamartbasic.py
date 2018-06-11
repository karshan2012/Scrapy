# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

class IndiamartbasicSpider(scrapy.Spider):
    name = 'indiamartbasic'
    def __init__(self, **kwargs):
        self.start_urls=['https://dir.indiamart.com/impcat/aluminum-led-bulb.html']
        print(self.start_urls)
        self.pages = []
        self.urls = {}
        allowed_domains = []
        super().__init__(**kwargs)

    def parse(self, response):
        #item = response.xpath('//*[starts-with(@class, "pnm ldf cur")]/@href').extract()
        print(len(response.xpath('//*[starts-with(@class, "pnm ldf cur")]/@href').extract()))
        item=['https://www.indiamart.com/proddetail/led-bulb-7016961148.html',
'https://www.indiamart.com/proddetail/led-bulb-9-watt-14818424562.html',
'https://www.indiamart.com/proddetail/led-bulb-4589553491.html']

        for i in item:
            yield Request(url=i, callback = self.parse_url)        
        pass

    def parse_url(self, response):
        titles = [response.xpath('//*[starts-with(@class, "pDn6 mt10")]//text()').extract()[1]]
        price = [response.xpath('//*[starts-with(@class, "prc-tip")]//text()').extract()[0].replace("Rs ","").replace("/","")]
        response_rate = [response.xpath('//*[starts-with(@class, "f12 pDn4")]//text()').extract()[2]]
        nature_of_business = [response.xpath('//*[starts-with(@class, "pDn4 f12")]//text()').extract()[1]]
        delivery_location = [response.xpath('//*[starts-with(@class, "pDn4 f12")]//text()').extract()[3]]
        year_of_establishment = [response.xpath('//*[starts-with(@class, "dtt fsbb-5 pr l20") and span="Year of Establishment"]//span//text()').extract()[1]]
        legal_status_of_firm = [response.xpath('//*[starts-with(@class, "dtt fsbb-5 pr l20") and span="Legal Status of Firm"]//span//text()').extract()[1]]
        no_of_employees = [response.xpath('//*[starts-with(@class, "dtt fsbb-5 pr l20") and span="Number of Employees"]//span//text()').extract()[1]]
        indiamart_member_since = [response.xpath('//*[starts-with(@class, "dtt fsbb-5 pr l20") and span="IndiaMART Member Since"]//span//text()').extract()[1]]
        permanent_account_number = [response.xpath('//*[starts-with(@class, "dtt fsbb-5 pr l20") and span="Permanent Account Number (PAN)"]//span//text()').extract()[1]]
        company_name = response.xpath('//*[starts-with(@class, "clr15")]//text()').extract()
        address = response.xpath('//*[starts-with(@class, "dtt l20 f14 color9")]//span//text()').extract()
        contact_person = [response.xpath('//*[starts-with(@class, "pt8 on")]//text()').extract()[1]]
        contact_number = response.xpath('//*[starts-with(@class, "duet c2")]//text()').extract()
        website = response.xpath('//*[starts-with(@class, "color9 tdu")]//text()').extract()

        
	#Give the extracted content row wise
        for items in zip(titles,price,response_rate,nature_of_business,delivery_location,year_of_establishment,legal_status_of_firm,no_of_employees,indiamart_member_since,permanent_account_number,company_name,address,contact_person,contact_number,website):
            scraped_info = {
                'Item' : items[0],
                'Price' : items[1],
                'Response Rate' : items[2],
                'Nature Of Business' : items[3],
                'Devivery Location' : items[4],
                'Year of Establishment' : items[5],
                'Legal status of Firm' : items[6],
                'No of Employees' : items[7],
                'Indiamart member since' : items[8],
                'PAN' : items[9],
                'Company Name' : items[10],
                'Address' : items[11],
                'Contact Person' : items[12],
                'Contact Number' : items[13],
                'Website' : items[14],
            }
            yield scraped_info
        pass
