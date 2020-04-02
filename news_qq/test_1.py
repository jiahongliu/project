import requests
import json

PAGE=0

def main():
    #更改page即可
    url='https://pacaio.match.qq.com/irs/rcd?cid=137&token=d0f13d594edfc180f5bf6b845456f3ea&id=&ext=top&page='+str(PAGE)
    headers={
        # 'Referer': 'https://new.qq.com/ch/comic/?rnd=1375',
        # 'Sec-Fetch-Mode':'no-cors',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',

    }
    resp=requests.get(url,headers=headers)
    if resp.status_code==200:
        js_text=resp.text
        js_str=json.loads(js_text)['data']
        for js in js_str:
            print(js['title'])

    else:
        print('爬取失败')


if __name__ == '__main__':
    main()