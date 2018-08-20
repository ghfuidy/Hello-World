# import requests
# import random

# useragent_list = ['Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
#                   'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#                   'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
# useraggent_choose = useragent_list[random.randint(0, 4)]
# headers = {
#     'User-Agent': useraggent_choose,
# }

# proxies = {
#     "http": "http://223.202.204.194:80",
#     # "https": "60.184.13.231:53128",
# }

# response = requests.get('https://www.whatismyip.net/',
#                         proxies=proxies, headers=headers)
# print(response.text)

# -*- coding: UTF-8 -*-
# from urllib import request
# if __name__ == "__main__":
#   #访问网址
#   url = 'http://www.whatismyip.com.tw/'
#   #这是代理IP
#   ip = '206.81.13.127:8080'
#   #设置代理ip访问方式，http和https
#   proxy = {'http':ip,'https':ip}
#   #创建ProxyHandler
#   proxy_support = request.ProxyHandler(proxy)
#   #创建Opener
#   opener = request.build_opener(proxy_support)
#   #添加User Angent
#   opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')]
#   #安装OPener
#   request.install_opener(opener)
#   #使用自己安装好的Opener
#   response = request.urlopen(url)
#   #读取相应信息并解码
#   html = response.read().decode("utf-8")
#   #打印信息
#   print(html)



        