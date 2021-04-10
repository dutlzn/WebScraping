import requests 
import json 
'''
拖动滚轮，会局部刷新
AJAX 
'''
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    # UA 伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    param = {
        'type': '24',
        'interval_id' : '100:90',
        'action' : '',
        'start' : '1',
        'limit' : '60',
    }

    response = requests.get(
        url = url, 
        headers = headers, 
        params = param)
    

    dict_obj = response.json()
    fp = open('douban_movie.json', 'w', encoding='UTF-8')
    json.dump(obj = dict_obj, fp=fp, ensure_ascii=False)
    print("爬取结束")

    
