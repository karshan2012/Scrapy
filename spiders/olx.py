# -*- coding: utf-8 -*-
import scrapy


class OlxSpider(scrapy.Spider):
    name = 'olx'
    #allowed_domains = ['https://dir.indiamart.com/impcat/aluminum-led-bulb.html']
    allowed_domains = []
    #start_urls = ['https://dir.indiamart.com/impcat/aluminum-led-bulb.html/']
    start_urls = [
       "https://www.olx.in/mumbai/motorcycles/?page=2",
       "https://www.olx.in/mumbai/motorcycles/?page=3",
       "https://www.olx.in/mumbai/motorcycles/?page=4",
       "https://www.olx.in/mumbai/motorcycles/?page=5",
       "https://www.olx.in/mumbai/motorcycles/?page=6",
       "https://www.olx.in/mumbai/motorcycles/?page=7",
       "https://www.olx.in/mumbai/motorcycles/?page=8",
       "https://www.olx.in/mumbai/motorcycles/?page=9",
       "https://www.olx.in/mumbai/motorcycles/?page=10",
       "https://www.olx.in/mumbai/motorcycles/?page=11",
       "https://www.olx.in/mumbai/motorcycles/?page=12",
       "https://www.olx.in/mumbai/motorcycles/?page=13",
       "https://www.olx.in/mumbai/motorcycles/?page=14",
       "https://www.olx.in/mumbai/motorcycles/?page=15",
       "https://www.olx.in/mumbai/motorcycles/?page=16",
       "https://www.olx.in/mumbai/motorcycles/?page=17",
       "https://www.olx.in/mumbai/motorcycles/?page=18",
       "https://www.olx.in/mumbai/motorcycles/?page=19",
       "https://www.olx.in/mumbai/motorcycles/?page=20",
       "https://www.olx.in/mumbai/motorcycles/?page=21",
       "https://www.olx.in/mumbai/motorcycles/?page=22",
       "https://www.olx.in/mumbai/motorcycles/?page=23",
       "https://www.olx.in/mumbai/motorcycles/?page=24",
       "https://www.olx.in/mumbai/motorcycles/?page=25",
       "https://www.olx.in/mumbai/motorcycles/?page=26",
       "https://www.olx.in/mumbai/motorcycles/?page=27",
       "https://www.olx.in/mumbai/motorcycles/?page=28",
       "https://www.olx.in/mumbai/motorcycles/?page=29",
       "https://www.olx.in/mumbai/motorcycles/?page=30",
       "https://www.olx.in/mumbai/motorcycles/?page=31",
       "https://www.olx.in/mumbai/motorcycles/?page=32",
       "https://www.olx.in/mumbai/motorcycles/?page=33",
       "https://www.olx.in/mumbai/motorcycles/?page=34",
       "https://www.olx.in/mumbai/motorcycles/?page=35",
       "https://www.olx.in/mumbai/motorcycles/?page=36",
       "https://www.olx.in/mumbai/motorcycles/?page=37",
       "https://www.olx.in/mumbai/motorcycles/?page=38",
       "https://www.olx.in/mumbai/motorcycles/?page=39",
       "https://www.olx.in/mumbai/motorcycles/?page=40",
       "https://www.olx.in/mumbai/motorcycles/?page=41",
       "https://www.olx.in/mumbai/motorcycles/?page=42",
       "https://www.olx.in/mumbai/motorcycles/?page=43",
       "https://www.olx.in/mumbai/motorcycles/?page=44",
       "https://www.olx.in/mumbai/motorcycles/?page=45",
       "https://www.olx.in/mumbai/motorcycles/?page=46",
       "https://www.olx.in/mumbai/motorcycles/?page=47",
       "https://www.olx.in/mumbai/motorcycles/?page=48",
       "https://www.olx.in/mumbai/motorcycles/?page=49",
       "https://www.olx.in/mumbai/motorcycles/?page=50",
       "https://www.olx.in/mumbai/motorcycles/?page=51",
       "https://www.olx.in/mumbai/motorcycles/?page=52",
       "https://www.olx.in/mumbai/motorcycles/?page=53",
       "https://www.olx.in/mumbai/motorcycles/?page=54",
       "https://www.olx.in/mumbai/motorcycles/?page=55",
       "https://www.olx.in/mumbai/motorcycles/?page=56",
       "https://www.olx.in/mumbai/motorcycles/?page=57",
       "https://www.olx.in/mumbai/motorcycles/?page=58",
       "https://www.olx.in/mumbai/motorcycles/?page=59",
       "https://www.olx.in/mumbai/motorcycles/?page=60",
       "https://www.olx.in/mumbai/motorcycles/?page=61",
       "https://www.olx.in/mumbai/motorcycles/?page=62",
       "https://www.olx.in/mumbai/motorcycles/?page=63",
       "https://www.olx.in/mumbai/motorcycles/?page=64",
       "https://www.olx.in/mumbai/motorcycles/?page=65",
       "https://www.olx.in/mumbai/motorcycles/?page=66",
       "https://www.olx.in/mumbai/motorcycles/?page=67",
       "https://www.olx.in/mumbai/motorcycles/?page=68",
       "https://www.olx.in/mumbai/motorcycles/?page=69",
       "https://www.olx.in/mumbai/motorcycles/?page=70",
       "https://www.olx.in/mumbai/motorcycles/?page=71",
       "https://www.olx.in/mumbai/motorcycles/?page=72",
       "https://www.olx.in/mumbai/motorcycles/?page=73",
       "https://www.olx.in/mumbai/motorcycles/?page=74",
       "https://www.olx.in/mumbai/motorcycles/?page=75",
       "https://www.olx.in/mumbai/motorcycles/?page=76",
       "https://www.olx.in/mumbai/motorcycles/?page=77",
       "https://www.olx.in/mumbai/motorcycles/?page=78",
       "https://www.olx.in/mumbai/motorcycles/?page=79",
       "https://www.olx.in/mumbai/motorcycles/?page=80",
       "https://www.olx.in/mumbai/motorcycles/?page=81",
       "https://www.olx.in/mumbai/motorcycles/?page=82",
       "https://www.olx.in/mumbai/motorcycles/?page=83",
       "https://www.olx.in/mumbai/motorcycles/?page=84",
       "https://www.olx.in/mumbai/motorcycles/?page=85",
       "https://www.olx.in/mumbai/motorcycles/?page=86",
       "https://www.olx.in/mumbai/motorcycles/?page=87",
       "https://www.olx.in/mumbai/motorcycles/?page=88",
       "https://www.olx.in/mumbai/motorcycles/?page=89",
       "https://www.olx.in/mumbai/motorcycles/?page=90",
       "https://www.olx.in/mumbai/motorcycles/?page=91",
       "https://www.olx.in/mumbai/motorcycles/?page=92",
       "https://www.olx.in/mumbai/motorcycles/?page=93",
       "https://www.olx.in/mumbai/motorcycles/?page=94",
       "https://www.olx.in/mumbai/motorcycles/?page=95",
       "https://www.olx.in/mumbai/motorcycles/?page=96",
       "https://www.olx.in/mumbai/motorcycles/?page=97",
       "https://www.olx.in/mumbai/motorcycles/?page=98",
       "https://www.olx.in/mumbai/motorcycles/?page=99",
       "https://www.olx.in/mumbai/motorcycles/?page=100",
       "https://www.olx.in/mumbai/motorcycles/?page=101",
       "https://www.olx.in/mumbai/motorcycles/?page=102",
       "https://www.olx.in/mumbai/motorcycles/?page=103",
       "https://www.olx.in/mumbai/motorcycles/?page=104",
       "https://www.olx.in/mumbai/motorcycles/?page=105",
       "https://www.olx.in/mumbai/motorcycles/?page=106",
       "https://www.olx.in/mumbai/motorcycles/?page=107",
       "https://www.olx.in/mumbai/motorcycles/?page=108",
       "https://www.olx.in/mumbai/motorcycles/?page=109",
       "https://www.olx.in/mumbai/motorcycles/?page=110",
       "https://www.olx.in/mumbai/motorcycles/?page=111",
       "https://www.olx.in/mumbai/motorcycles/?page=112",
       "https://www.olx.in/mumbai/motorcycles/?page=113",
       "https://www.olx.in/mumbai/motorcycles/?page=114",
       "https://www.olx.in/mumbai/motorcycles/?page=115",
       "https://www.olx.in/mumbai/motorcycles/?page=116",
       "https://www.olx.in/mumbai/motorcycles/?page=117",
       "https://www.olx.in/mumbai/motorcycles/?page=118",
       "https://www.olx.in/mumbai/motorcycles/?page=119",
       "https://www.olx.in/mumbai/motorcycles/?page=120",
       "https://www.olx.in/mumbai/motorcycles/?page=121",
       "https://www.olx.in/mumbai/motorcycles/?page=122",
       "https://www.olx.in/mumbai/motorcycles/?page=123",
       "https://www.olx.in/mumbai/motorcycles/?page=124",
       "https://www.olx.in/mumbai/motorcycles/?page=125",
       "https://www.olx.in/mumbai/motorcycles/?page=126",
       "https://www.olx.in/mumbai/motorcycles/?page=127",
       "https://www.olx.in/mumbai/motorcycles/?page=128",
       "https://www.olx.in/mumbai/motorcycles/?page=129",
       "https://www.olx.in/mumbai/motorcycles/?page=130",
       "https://www.olx.in/mumbai/motorcycles/?page=131",
       "https://www.olx.in/mumbai/motorcycles/?page=132",
       "https://www.olx.in/mumbai/motorcycles/?page=133",
       "https://www.olx.in/mumbai/motorcycles/?page=134",
       "https://www.olx.in/mumbai/motorcycles/?page=135",
       "https://www.olx.in/mumbai/motorcycles/?page=136",
       "https://www.olx.in/mumbai/motorcycles/?page=137",
       "https://www.olx.in/mumbai/motorcycles/?page=138",
       "https://www.olx.in/mumbai/motorcycles/?page=139",
       "https://www.olx.in/mumbai/motorcycles/?page=140",
       "https://www.olx.in/mumbai/motorcycles/?page=141",
       "https://www.olx.in/mumbai/motorcycles/?page=142",
       "https://www.olx.in/mumbai/motorcycles/?page=143",
       "https://www.olx.in/mumbai/motorcycles/?page=144",
       "https://www.olx.in/mumbai/motorcycles/?page=145",
       "https://www.olx.in/mumbai/motorcycles/?page=146",
       "https://www.olx.in/mumbai/motorcycles/?page=147",
       "https://www.olx.in/mumbai/motorcycles/?page=148",
       "https://www.olx.in/mumbai/motorcycles/?page=149",
       "https://www.olx.in/mumbai/motorcycles/?page=150",
       "https://www.olx.in/mumbai/motorcycles/?page=151",
       "https://www.olx.in/mumbai/motorcycles/?page=152",
       "https://www.olx.in/mumbai/motorcycles/?page=153",
       "https://www.olx.in/mumbai/motorcycles/?page=154",
       "https://www.olx.in/mumbai/motorcycles/?page=155",
       "https://www.olx.in/mumbai/motorcycles/?page=156",
       "https://www.olx.in/mumbai/motorcycles/?page=157",
       "https://www.olx.in/mumbai/motorcycles/?page=158",
       "https://www.olx.in/mumbai/motorcycles/?page=159",
       "https://www.olx.in/mumbai/motorcycles/?page=160",
       "https://www.olx.in/mumbai/motorcycles/?page=161",
       "https://www.olx.in/mumbai/motorcycles/?page=162",
       "https://www.olx.in/mumbai/motorcycles/?page=163",
       "https://www.olx.in/mumbai/motorcycles/?page=164",
       "https://www.olx.in/mumbai/motorcycles/?page=165",
       "https://www.olx.in/mumbai/motorcycles/?page=166",
       "https://www.olx.in/mumbai/motorcycles/?page=167",
       "https://www.olx.in/mumbai/motorcycles/?page=168",
       "https://www.olx.in/mumbai/motorcycles/?page=169",
       "https://www.olx.in/mumbai/motorcycles/?page=170",
       "https://www.olx.in/mumbai/motorcycles/?page=171",
       "https://www.olx.in/mumbai/motorcycles/?page=172",

   ]

    def parse(self, response):
	#Extracting the content using css selectors
        s = response.xpath('//*[starts-with(@class, "marginright5")]').extract()
        print(s)
        #titles = response.css('.lcname::text').extract()
        #votes = response.css('.lcname::attr(href)').extract()
        #times = response.css('time::attr(title)').extract()
        #comments = response.css('.comments::text').extract()

	#Give the extracted content row wise
        for item in s:
            #print(item)
            #a,b=item.split(' class=')
            yield { 'url' : item }
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
