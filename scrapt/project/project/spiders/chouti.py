import scrapy
from scrapy.selector import Selector

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        # print(response)
        # print(response.url)
        # # print(response.text)

        # # 找到文档中所有a标签
        # hxs = Selector(response=response).xpath("//a") 
        # print(len(hxs))
        # # for i in hxs:
        # #     print(i)

        # hxs = Selector(response=response).xpath('//div[@class="link-con"]/div[contains(@class,"link-item")]')
        # print(hxs[0])
        # print(len(hxs))

        # for obj in hxs:
        #     a = obj.xpath('.//a[@class="link-title link-statistics"]/text()').extract_first()
        #     print(a)

        # 选择器
        '''
        // 表示子孙中
        .// 当前对象的子孙中
        / 儿子
        /div 儿子中的div标签
        /div[@id="i1"] 儿子中的div标签且id=i1
        obj.extract() 列表中每一个对象转换字符串 => []
        obj.extract_first() 列表中每一个对象转换字符串 => 列表第一个元素
        //div/text() 获取某个标签的文本
        '''


        # 获取页面所有的页码
        # hxs = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # for item in hxs:
        #     print(item)

