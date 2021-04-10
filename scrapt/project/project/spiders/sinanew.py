import scrapy


class SinanewSpider(scrapy.Spider):
    name = 'sinanew'
    allowed_domains = ["baidu.com"]
    start_urls = ['https://www.bbc.com/news/blogs/the_papers']

    def parse(self, response):
        print(response)

        hxs = Selector(response=response).xpath('//li')
        print(len(hxs))

        
