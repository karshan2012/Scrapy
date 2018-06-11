# Scrapy

scrapy shell
fetch('https://www.moneycontrol.com/stocks/hist_stock_result.php?sc_id=RI&pno=10&hdn=daily&fdt=2000-01-01&todt=2018-06-01')
view(response)
response.xpath('//*[starts-with(@class, "tblchart")]').extract() 
