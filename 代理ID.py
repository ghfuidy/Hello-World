import urllib.request
import re
import random
import json
import time


def openurl(url):
    useragent_list = ['Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
                      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
                      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    useraggent_choose = useragent_list[random.randint(0, 4)]
    headers = {
        'User-Agent': useraggent_choose,
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def getIPlist():
    html = openurl('http://www.xicidaili.com/').decode('utf-8')
    iplist = []

    start_position = 0
    print('开始搜集')
    ip = re.search(
        r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])', html[start_position:])
    while ip:
        start_position += ip.end()
        port_a = html.find('<td>', start_position) + 4
        port_b = html.find('</td>', port_a)
        port = html[port_a:port_b]
        fullip = ip.group() + ':' + port
        ipstyle = re.search(r'HTTPS|HTTP', html[start_position:])
        if ipstyle and ipstyle.group() == 'HTTPS':
            iplist.append(fullip)
        ip = re.search(
            r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])', html[start_position:])
    print('搜集结束')
    # print(iplist)
    return iplist


def ip_search():
    html = openurl('https://www.whatismyip.net/').decode('utf-8')
    a = html.find('<tr><td>Hostname:') + 33
    b = html.find('"><span class="shorter">')
    print(html[a:b])


def change_ip(targetIP):
    proxy_support = urllib.request.ProxyHandler({'https': targetIP})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


def dailiip():
    # ip_search()
    checktime()
    with open(r'D:\CODE\python_test\iplist.json', 'r+') as data:
        listdata = json.load(data)
        iplist = listdata['HTTPS']
    rad_ip = random.randint(0, len(iplist)-1)
    change_ip(iplist[rad_ip])
    # ip_search()


def checktime():
    try:
        with open(r'D:\CODE\python_test\iplist.json', 'rb') as jsonlist:
            r = json.load(jsonlist)
            if r:
                now = time.time()
                datatime = r['datatime']
                if now - datatime >= 86400:
                    print('数据过期')
                    r['datatime'] = now
                    iplist = getIPlist()
                    r['HTTPS'] = iplist
                    w = json.dumps(r)
                    with open(r'D:\CODE\python_test\iplist.json', 'w') as jsonWrite:
                        jsonWrite.write(w)
                else:
                    print('间隔未到')
                    pass
            else:
                print('file has nothing')
    except Exception as f:
        now = time.time()
        r = {}
        r['datatime'] = now
        iplist = getIPlist()
        r['HTTPS'] = iplist
        w = json.dumps(r)
        with open(r'D:\CODE\python_test\iplist.json', 'w') as jsonWrite:
            jsonWrite.write(w)


if __name__ == '__main__':
    # dailiip()
    change_ip('101.132.122.230:3128')
    ip_search()
    # iplist = getIPlist()
    # rad_ip = random.randint(0,len(iplist))
    # print(rad_ip)
    # change_ip(iplist[rad_ip])
    # ip_search()
