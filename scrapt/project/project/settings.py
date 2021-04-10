# Scrapy settings for project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'project'

SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'

USER_AGENT = 'fashionWebScraping'
# 遵守 rebots.txt 规则
ROBOTSTXT_OBEY = True
# 参阅 https://doc.scrapy.org/en/latest/topics/settings.html
# 下载延迟
# 另请参阅 autothrottle 的设置和文档
# 这样可以避免对服务器造成太大的压力
DOWNLOAD_DELAY = 1
# 重写默认的请求报头：
DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'tr',
}
# 配置项目管道
# 参阅 https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = '/Users/erdemisbilen/Angular/fashionWebScraping/images_scraped'

