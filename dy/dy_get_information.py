import requests
import re
from lxml import etree
import urllib3
urllib3.disable_warnings()

user_id=2137048276015006

def change_font(value):
    #通过FontCreator 定义映射
    dict_num = {
        'ue618': '1',
        'ue602': '1',
        'ue60e': '1',
        'ue603': '0',
        'ue616': '0',
        'ue60d': '0',
        'ue604': '3',
        'ue611': '3',
        'ue61a': '3',
        'ue605': '2',
        'ue610': '2',
        'ue617': '2',
        'ue606': '4',
        'ue619': '4',
        'ue60c': '4',
        'ue607': '5',
        'ue60f': '5',
        'ue61b': '5',
        'ue61f': '6',
        'ue608': '6',
        'ue612': '6',
        'ue61e': '9',
        'ue615': '9',
        'ue609': '9',
        'ue60a': '7',
        'ue61c': '7',
        'ue613': '7',
        'ue60b': '8',
        'ue61d': '8',
        'ue614': '8',
    }
    new_lis = []
    new_font = (list(map(lambda x: x.encode('unicode_escape'), value)))
    for i in new_font:
        try:
            new_lis.append(dict_num[str(i)[4:-1:]])
        except:
            new_lis.append(str(i)[2:-1:])
        continue
    dd=''.join(new_lis).strip()
    return dd

def getter(user_id):
    url = 'https://www.iesdouyin.com/share/user/' + str(user_id)
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    }
    resp=requests.get(url,headers=headers,verify=False)
    if resp.status_code==200:
        user_infor={}
        html=etree.HTML(resp.text)
        user_infor['name']=str(html.xpath('//p[@class="nickname"]/text()')[0])
        user_infor['introduct'] = str(html.xpath('//p[@class="signature"]/text()')[0]).replace('\n','')
        dyID=str(html.xpath('string(//p[@class="shortid"])')).split()
        del dyID[0]
        user_infor['dyID']=change_font(''.join(dyID))
        user_infor['focus_on_num']=change_font(str(html.xpath('string(//*[@id="pagelet-user-info"]/div[2]/div[2]/p[2]/span[1]/span[1])')).replace(' ',''))
        user_infor['fans_num']=change_font(str(html.xpath('string(//*[@id="pagelet-user-info"]/div[2]/div[2]/p[2]/span[2]/span[1])').replace(' ','')))
        user_infor['zan_num']=change_font(str(html.xpath('string(//*[@id="pagelet-user-info"]/div[2]/div[2]/p[2]/span[3]/span[1])').replace(' ','')))
        user_infor['works_num']=change_font(str(html.xpath('string(//*[@id="pagelet-user-info"]/div[3]/div/div[1]/span)').replace(' ','')))
        user_infor['like_num']=change_font(str(html.xpath('string(//*[@id="pagelet-user-info"]/div[3]/div/div[2]/span)')).replace(' ',''))
        return user_infor
    else:
        return '页面获取失败 响应码:%s',resp.status_code

def main():
    print(getter(user_id=user_id))

if __name__ == '__main__':
    main()