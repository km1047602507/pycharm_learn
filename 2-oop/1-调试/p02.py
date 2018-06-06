'''
张继科吧：
主页：https://tieba.baidu.com/f?ie=utf-8&kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&fr=search
第1页:https://tieba.baidu.com/f?kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&ie=utf-8&pn=0
2:https://tieba.baidu.com/f?kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&ie=utf-8&pn=50
3:https://tieba.baidu.com/f?kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&ie=utf-8&pn=100
4:https://tieba.baidu.com/f?kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&ie=utf-8&pn=150
5:https://tieba.baidu.com/f?kw=%E5%BC%A0%E7%BB%A7%E7%A7%91&ie=utf-8&pn=200

解决方法：
1.准备构建参数字典
    kw  ie  pn
2.使用parse构建完整url
3.使用for循环下载

'''
from urllib import request,parse
if __name__ == '__main__':
    qs ={
        "kw":"张继科",
        "ie":"utf-8",
        "pn":0
    }
    urls = []
    baseurl = "http://tieba.baidu.com/f?"
    for i in range(10):
        pn = i * 50
        qs['pn'] = str(pn)
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        print(html)