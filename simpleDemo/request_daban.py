import requests
import json

if __name__ == '__main__':
    url = 'https://dmfw.mca.gov.cn/9095/stname/count'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    data = {
        'type': 'place',
        'stName': '达坂',
        'placeTypeCode':'',
        'placeTypeCodeLen': '0',
        'code':'',
        'year': '2018',
        'adminCodeLen': '0',
        'searchType': '模糊',
    }

    response = requests.post(url=url, data=data, headers=headers).text

    with open(r'D:\scrapyfile\1.txt', 'w', encoding='utf-8') as f:
        f.write(response)
