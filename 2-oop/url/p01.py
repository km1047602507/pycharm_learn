from urllib import request

if __name__ == '__main__':
    url = "http://ts.zhaopin.com/jump/index_new.html?utm_source=other&utm_medium=cnt&utm_term=&utm_campaign=121122526&utm_provider=zp&sid=121122526&site=u243985234.c1019396294.g1925498928.k1060370187.pq"
    rsp = request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    print(html)
