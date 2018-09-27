import 代理ID
import json
import re
import urllib.parse
from bs4 import BeautifulSoup
import os
from time import sleep

def getxueshuData(keyword,sort):
    page_num = 0
    next_status = True
    full_article = {}
    while next_status:
        base_url = 'http://xueshu.baidu.com/s'
        params = {
            'wd':keyword,
            'pn':page_num,
            'tn':'SE_baiduxueshu_c1gjeupa',
            'sc_f_para':'sc_tasktype={firstSimpleSearch}',
            'sc_hit':1,
            'ie':'utf-8',
            'sort':sort
        } 
        full_url = base_url+ '?' + urllib.parse.urlencode(params)
        # 代理ID.dailiip()
        html = 代理ID.openurl(full_url).decode('utf-8')
        with open('helloworld_python/HTML/baiduxueshu.html','wb') as baiduscholar:
            baiduscholar.write(html.encode('utf-8'))
        soup = BeautifulSoup(html,'lxml')
        search_consequence = soup.find("span",class_='nums')
        search_num = re.search(r'[\d,]+',str(search_consequence)).group()
        print(search_num)
        search_list = soup.find_all('div',class_='result sc_default_result xpath-log')
        for each in search_list:
            ###each.div.h3.a.text ： 用来提取文章题目
            a_title = each.div.h3.a.text
            sc_authors = each.find_all('a',{'data-click':"{'button_tp':'author'}"})
            a_authors = ''
            sc_author = []
            for author in sc_authors:
                sc_author.append(author.text)
                a_authors = ','.join(sc_author)
            sc_time = each.find('span',class_='sc_time')
            a_time = sc_time.text.strip()
            a_publish = sc_time.find_previous('span').text.strip()
            str_each = str(each)
            a_abstract_s = str_each.find('c_abstract')
            a_abstract_f = str_each.find('<div class="sc_allversion">',a_abstract_s)
            if a_abstract_f == -1:
                a_abstract_f = str_each.find('</div>',a_abstract_s)
            a_abstract = str_each[a_abstract_s+12:a_abstract_f].strip().replace('<em>','').replace('</em>','')
            if sc_time.find_previous('span') == each.div.div.span:
                a_publish = '无'
            if sc_time.find_next('span').a:
                a_number = sc_time.find_next('span').a.text.strip()
            else:
                a_number= re.search(r'\d+',str(sc_time.find_next('span').text)).group()
            print(a_title,'\n',a_time,'\n',a_number)
            sc_article = {
                'title       ':a_title,
                'author':a_authors,
                'time':a_time,
                'reference':a_number,
                'publish':a_publish,
                'abstract':a_abstract
            }
            full_article[a_title] = sc_article
        if page_num < 100:
            page_num += 10
            next_status = True
        else:
            next_status = False
        sleep(10)
    return full_article

def savedata(name,data):
    folder=r'D:\学习资料\百度学术'
    try:
        os.mkdir(folder)
        os.chdir(folder)
    except FileExistsError:
        os.chdir(folder)
    with open(folder+'\\'+name+'.json','w',encoding ='utf-8') as f:
        searchData = json.dumps(data,ensure_ascii=False)
        f.write(searchData)

if __name__ == '__main__':
    research_opition = input('请输入搜索关键词，多个关键词以逗号连接')
    keyword = '+'.join(research_opition.split())
    search_sort = ''
    ###相关性：空。时间：sc_time
    scholarDATA = getxueshuData(research_opition,search_sort)
    savedata(keyword,scholarDATA)