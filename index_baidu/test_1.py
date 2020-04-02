import requests
import json

#search 是搜索指数 news是咨询指数
Choose='search'
#控制排名数量
NUB=10
#控制排名类型
demeid=2

def main():
    if Choose=='news':
        url='http://insight.baidu.com/base/' + Choose + '/rank/general?pageSize='+str(NUB) + '&source=0&toFixed=1&filterType=1&dateType=20200323~20200329&dimensionid='+str(demeid)+'&rateType=1000'
    elif Choose=='search':
        url='http://insight.baidu.com/base/' + Choose + '/rank/list?pageSize=' + str(
            NUB) + '&source=0&toFixed=1&filterType=1&dateType=20200323~20200329&dimensionid='+str(demeid)+'&rateType=1000'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    resp=requests.get(url,headers=headers)
    resp.encoding = ('utf-8')
    if resp.status_code==200:
        res_text=resp.text
        js_str=json.loads(res_text)['data']['results']['current']
        for js in js_str:
            print(js['rank'],js['item'],)
        # print(js_str)
    else:
        print('获取失败')


if __name__ == '__main__':
    main()
