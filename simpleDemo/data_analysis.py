import requests 
import json 

'''
爬取糗事百科中图片
'''
if __name__ == '__main__' :
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    url = 'https://pic.qiushibaike.com/system/pictures/12415/124156185/medium/S0QSW2LLWZHZ7N8F.jpg'
    '''
    content 二进制
    json 对象
    text 字符串
    '''
    img_data = requests.get(url=url).content

    with open('D:\scrapyfile\qiutu.jpg', 'wb') as f: 
        f.write(img_data)

    '''
    使用通用爬虫对url对应的一整张页面进行爬取
    '''

    url = 'https://www.qiushibaike.com/imgrank/'
    page_text = requests.get(url=url, headers=headers).text 

    # 使用聚焦爬虫 将页面中所有的图片进行解析/提取
    