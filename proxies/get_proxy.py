'''
代理获取模块
'''
import requests
from lxml import etree

class Got_Proxie():
    #定义一个方法获取前五页66ip的代理
    def got_proxie_ip66(self,pages=5):
        base_url='http://www.66ip.cn/{}.html'
        urls=[base_url.format(page) for page in range(1,pages+1)]
        #这个网站不加请求头也能爬
        for url in urls:
            resp=requests.get(url=url)
            if resp.status_code==200:
                resp_html=etree.HTML(resp.text)
                resp_ip = resp_html.xpath('//div[contains(@class,"containerbox")]//table//tr/td[1]/text()')
                del resp_ip[0]
                resp_port = resp_html.xpath('//div[contains(@class,"containerbox")]//table//tr/td[2]/text()')
                del resp_port[0]
                for i in range(len(resp_port)):
                    proxie=resp_ip[i]+':'+resp_port[i]
                    yield proxie
            else:
                print(resp.status_code)
                print('获取页面失败')
