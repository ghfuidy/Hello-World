# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:40:51 2019

@author: ASUS
"""

import requests  #网络请求库
from lxml import etree #数据清洗库
from fake_useragent import UserAgent #随机ua

#公共变量
headers = {
        'User-Agent':UserAgent().random
}
#文件IO对象
fp = open('./novel.txt','a',encoding='utf-8')
#获取源码
def index():
    for num in range(0,226,25):
        base_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T".format(num)
        response = requests.get(base_url,headers=headers)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        clean(html)

#数据清洗
def clean(html):
    moive_name = html.xpath('//div[@class="info"]/h2/a/text()')
    ratings = html.xpath('//div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
    writers = html.xpath('///div[@class="info"]/div[@class="pub"]/text()')
    

    for i in moive_name:
        i.replace("\n",'')
        if i == "\n\n  ":
            moive_name.remove("\n\n  ")
    print('ratings',ratings)
    # print(writers)
    
 
#列表的长度
    lens = len(moive_name)
    print(moive_name)
    print(lens,len(ratings),len(writers))
    i = 0
    while i < lens:
        book_names = moive_name[i]
        rating = ratings[i]
        writer = writers[i]
        # print(book_names,writer)
        # book_info = '电影名：'+book_names+'  评分:'+rating+' 作者:'+writer
#       print('书名：',book_names,' 评分:',rating,' 作者:',writer)
        book_info = '小说{}  评分:{} 作者: {}\n'.format(book_names,rating,writer)
        i += 1
        sto_info(book_info)
        
        
   
#数据存储
def sto_info(book_info):
    # 存储数据
    fp.write(book_info+'\n')
if __name__ == '__main__':
    index()
    fp.close()



