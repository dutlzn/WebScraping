import requests 
import json
'''
局部刷新 AJAX 
NETWORK XHR
'''
if __name__ == '__main__':
    # UA 伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': 'dog'
    }
    response = requests.post(
        url = url,
        data = data,
        headers = headers
    )
    # json 返回一个obj
    dict_obj = response.json()
    print(dict_obj)
    

    fp = open('./dog.json', 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False) # 中文不允许ascii
    print("数据查询结束")