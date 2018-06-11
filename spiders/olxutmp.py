# -*- coding: utf-8 -*-
import scrapy
import re


class OlxutmpSpider(scrapy.Spider):
    name = 'olxutmp'
    #allowed_domains = ['https://dir.indiamart.com/impcat/aluminum-led-bulb.html']
    allowed_domains = []
    start_urls = ["https://www.olx.in/item/honda-cb-25874-kms-2013-year-ID1kGBOP.html#8ea17fe036",
                  "https://www.olx.in/item/2008-bajaj-platina-16500-kms-ID1kGJ03.html#159789021f"]

    def parse(self, response):
	#Extracting the content using css selectors
        titles = response.xpath('//*[starts-with(@class, "brkword")]//text()').extract()
        adid = response.xpath('//*[starts-with(@class, "pdingleft10 brlefte5")]//text()').extract()
        locality = response.xpath('//*[starts-with(@class, "c2b small")]//text()').extract()
        model = response.xpath('//*[starts-with(@class, "brkword")]//text()').extract()
        price = response.xpath('//*[starts-with(@class, "xxxx-large margintop7 inlblk not-arranged")]//text()').extract()
        details = response.xpath('//*[starts-with(@class, "details")]//text()').extract()
        #print(titles + " ==> "+ str(titles) )
        adidd=''
        for i in adid:
            adidd = adidd + " " + re.sub('\s+',' ',str(i))
        adidd = tuple([adidd])
        #print(adidd)
        detailss = ''
        for j in details:
            detailss = detailss + " " + re.sub('\s+',' ',str(j))
        detailss = tuple([detailss])
        #print(detailss)
        #print(locality + " ==> "+ str(locality) )
        #print(model + " ==> "+ str(model) )
        #print(price + " ==> "+ str(price) )
        #print(details + " ==> "+ str(details) )
        #votes = response.css('.lcname::attr(href)').extract()
        #times = response.css('time::attr(title)').extract()
        #comments = response.css('.comments::text').extract()

	#Give the extracted content row wise
        for items in zip(titles,adidd,locality,model,price,detailss):
            item_new = re.sub('\s+',' ',str(items[0]))
            adid_new = re.sub('\s+',' ',str(items[1]))
            locality_new = re.sub('\s+',' ',str(items[2]))
            model_new = re.sub('\s+',' ',str(items[3]))
            price_new = re.sub('\s+',' ',str(items[4]))
            details_new = re.sub('\s+',' ',str(items[5]))
            
            print(item_new)
            print(adid_new)
            print(locality_new)
            print(model_new)
            print(price_new)
            print(details_new)
            scraped_info = {
                'Item' : item_new,
                'Price' : price_new,
                'Ad ID' : adid_new,
                'Location' : locality_new,
                'Model' : model_new,
                'Details' : details_new,
                #'comments' : item[3],
            }
            yield scraped_info
            #href = item[1]+"enquiry.html"
            #cntct = "yo"
            #yield response.follow(href, callback=self.parse_company)
            #print(contact)
            #yield scrapy.Request(href, callback=self.parse)
            #create a dictionary to store the scraped info
            #scraped_info = {
                #'title' : item[0],
                #'vote' : item[1],
                #'contact' : cntct,
                #'contact' : yield response.follow(href, self.parse_company)
                #'created_at' : item[2],
                #'comments' : item[3],
            #}
            #yield scraped_info
            #print(scraped_info)

	#yield or give the scraped info to scrapy
        #yield scraped_info

        pass

    def parse_company(self, response):
        yield {'contact' : response.xpath("//*[starts-with(@id, \"map-div\")]/div[1]").css('::text').extract() }
        #print(response.xpath("//*[starts-with(@id, \"map-div\")]/div[1]").css('::text').extract())
        #yield response.xpath("//*[starts-with(@id, \"map-div\")]/div[1]").css('::text').extract()
        #def extract_with_css(query):
        #    return response.css(query).extract()   
