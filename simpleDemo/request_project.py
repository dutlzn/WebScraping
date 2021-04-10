'''
综合训练
'''

import requests
import json
if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    # page_text = requests.get(url = url, headers=headers).text
    # with open('./huazhuangpin.html', 'w', encoding='UTF-8') as f :
    #     f.write(page_text)

    '''
    text结果和浏览器里的结果不一样 
    说明有些东西 是另外的url请求到的 XHR 

    详情页 也不一定用id 就可以加载出来， 
    也有可能是ajax请求
    http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList
    http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    '''

    # 批量获取不同企业的ID值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = [] # 存储企业的id
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
        }
        json_ids = requests.post(url = url ,headers = headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_data_list = []
    for id in id_list:
        data = {
            'id': id
        }

        detail_json = requests.post(url=url, data=data, headers=headers).json()
        all_data_list.append(detail_json)
    
    fp = open('./allData.json', 'w', encoding='UTF-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
