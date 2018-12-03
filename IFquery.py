import urllib.request
import os
import base64
import random
import 代理ID
from bs4 import BeautifulSoup
import re

def searchjournal(searchname):
    代理ID.dailiip()

    data = {}
    data['searchname'] = searchname
    data['searchissn']= ''
    data['searchfield']= ''
    data['searchimpactlow']='' 
    data['searchimpacthigh']='' 
    data['searchscitype']= ''
    data['view']= 'search'
    data['searchcategory1']='' 
    data['searchcategory2']= ''
    data['searchjcrkind']= ''
    data['searchopenaccess']='' 
    data['searchsort']= 'relevance'

    url = 'http://www.letpub.com.cn/index.php?page=journalapp&view=search'
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')

    useragent_list = ['Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
                      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
                      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    useraggent_choose = useragent_list[random.randint(0,4)]
    header = {
        'User-Agent':useraggent_choose,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.letpub.com.cn',
        'Origin': 'http://www.letpub.com.cn',
        'Referer': 'http://www.letpub.com.cn/index.php?page=journalapp&view=search',
        'Save-Data': 'on',
        'Upgrade-Insecure-Requests': 1,
    }
    req = urllib.request.Request(url,data=data,headers=header)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        part1 = soup.find('table',class_='table_yjfx')
        issn_pattern = r"(\d{4}\-\d{4})"
        part2 = part1.find('td',string=re.compile(issn_pattern))
        part_th = part2.parent
        print(part2)
        print(part_th)
        IF = part1.find('td',string=re.compile(r"(\d{0,3}\.\d{3})"))
        jcr_part = part1.find('td',string=re.compile(r"(\d?区{1})"))
        print(IF,jcr_part)
        return IF.text,jcr_part.text
    except Exception as e:
        print('error',e)
        html = ''



if __name__ == '__main__':
    inputword = input('请输入杂志名')
    searchjournal(inputword)


