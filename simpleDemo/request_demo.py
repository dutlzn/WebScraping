# 爬取搜狗首页的页面数据
import requests 
if __name__ == '__main__':
    # 指定URL
    url = "https://www.sogou.com"
    # 发起请求
    response = requests.get(url = url)
    # 获取相应数据
    page_text = response.text
    # 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as f:
        f.write(page_text)
    print("爬取数据结束")