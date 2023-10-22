import scrapy

class CODALSpider(scrapy.Spider):
    name = 'BOOKScraper'
    start_urls = ['http://books.toscrape.com/']
    def parse(self,response):
        for item in response.xpath("//article[@class='product_pod']"):

            yield {  
                     
                     
                    #  "ProductYear"  : item.xpath('/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a/text()').getall()
                     "ProductYear"  : item.css('a::text').get(),
                     "Price" : item.css("p.price_color::text").get(),
                     "Url" : item.css("a::attr(href)").get()
                     
                     }


            
            


from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    "USER_AGENT" : 'Mozilla/5.0',
    'FEED_FORMAT' :'csv',
    "FEED_URI":'output_1.csv'
})

c.crawl(CODALSpider)
c.start()
