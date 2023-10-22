import scrapy

class YasinSpider2(scrapy.Spider):
    name = 'yasinboot'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self,response):
        for item in response.css("div.quote"):
            yield {  
                     
                     "Text"  : item.css('span.text::text').get(),
                     "auther" : item.css("small.author::text").get(),
                     "tags" : item.css("div.tags a.tag::text").getall()
                     
                     }
            


from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    "USER_AGENT" : 'Mozilla/5.0',
    'FEED_FORMAT' :'csv',
    f"FEED_URI":'output_{class}_{name}.csv'
})

c.crawl(yasinSpider2)
c.start()
