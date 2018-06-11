# -*- coding: utf-8 -*-
import scrapy


class RedditbotcopySpider(scrapy.Spider):
    name = 'redditbotcopy'
    #allowed_domains = ['https://dir.indiamart.com/impcat/aluminum-led-bulb.html']
    allowed_domains = []
    start_urls = ['https://dir.indiamart.com/impcat/aluminum-led-bulb.html/']

    def parse(self, response):
	#Extracting the content using css selectors
        titles = response.css('.lcname::text').extract()
        votes = response.css('.lcname::attr(href)').extract()
        #times = response.css('time::attr(title)').extract()
        #comments = response.css('.comments::text').extract()

	#Give the extracted content row wise
        for item in zip(titles, votes):
            #print(item)
            href = item[1]+"enquiry.html"
            cntct = "yo"
            yield response.follow(href, callback=self.parse_company)
            #print(contact)
            #yield scrapy.Request(href, callback=self.parse)
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                #'contact' : cntct,
                #'contact' : yield response.follow(href, self.parse_company)
                #'created_at' : item[2],
                #'comments' : item[3],
            }
            yield scraped_info
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
