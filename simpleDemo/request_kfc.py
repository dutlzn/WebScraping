import requests
import json
'''
Content-Type: text/plain; charset=utf-8 ====> response.text
json ====> response.json
'''
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
    request_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    param = {
        'cname' : '',
        'pid': '',
        'keyword': '北京' ,
        'pageIndex': '1' ,
        'pageSize': '100',
    }

    # UA 伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    response = requests.post(url = request_url, headers = headers, data=param)

    with open('./kfc.txt', 'w', encoding='UTF-8') as f: 
        f.write(response.text)

    print("over")
