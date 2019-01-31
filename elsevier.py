from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import 代理ID
import urllib.request
import http.cookiejar
import random
import http.client
import json
import re

##通过文章名来查看jcr分区和影响因子
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
        response = urllib.request.urlopen(req,timeout=20)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        part1 = soup.find('table',class_='table_yjfx')
        issn_pattern = r"(\d{4}\-\d{4})"
        part2 = part1.find('td',string=re.compile(issn_pattern))
        part_th = part2.parent
        IF = part_th.find('td',string=re.compile(r"(\d{0,3}\.\d{3})"))
        jcr_part = part_th.find('td',string=re.compile(r"(\d?区{1})"))
        journalname = IF.find_previous_sibling('td')
        IF_l = [IF.text,jcr_part.text,journalname.a.text]
    except Exception as e:
        print('error',e)
        html = ''
        IF_l = []
    print(IF_l)
    return IF_l


#收集页面信息
def search_c():
    part_l = soup.find_all('div', class_='result-item-content')
    article_msg = {}
    for each_p in part_l:
        title_l = each_p.h2.text.strip().split()
        # 文章标题
        title = ' '.join(title_l)
        # 下载链接
        try:
            d_link = each_p.find('a', class_='download-link')['href']
        except Exception as spexp:
            print(spexp)
            d_link = ''
        d_linkfull = 'https://www.sciencedirect.com' + d_link
        # 发布时间和期刊
        p_book_l = each_p.div.ol.text.split()
        p_book = ' '.join(p_book_l)
        # 文章作者
        authors_l = each_p.find(
            'ol', class_=['Authors hor undefined', 'Authors hor reduce-list']).text.split()
        authors = ' '.join(authors_l)
        article_list = {'title': title,
                        'pdflink': d_linkfull,
                        'publish': p_book,
                        'authors': authors}
        article_msg[title] = article_list
    return article_msg

#将cookie访问定义为一个函数
def visiturl(geturl):
    useragent_list = ['Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
                        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
                        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    useraggent_choose = useragent_list[random.randint(0, 4)]
    headers = {
        'User-Agent': useraggent_choose,
    }
    cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
    handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    opener = urllib.request.build_opener(handler)  # 通过handler来构建opener
    urllib.request.install_opener(opener)
    request = urllib.request.Request(geturl,headers=headers)
    response = urllib.request.urlopen(request)
    try:
        html = response.read()
        print('html is OK')
    except http.client.IncompleteRead:
        html = ''
        print('html is empty')
    return html

#通过浏览器转到pdf页面，并获取真实连接，并关闭网页
def getrealpdf(pdftitle,gethandler):
    browser.switch_to_window(gethandler)
    try:
        locator = (By.ID,"plugin")
        WebDriverWait(browser,10).until(EC.presence_of_element_located(locator))
        realurl = browser.current_url
    except TimeoutError:
        print(pdftitle,'-------------is error')
    browser.close()
    print(realurl)
    print(pdftitle)
    savePDF(pdftitle,realurl)
    return realurl

#保存PDF到指定文件夹
def savePDF(title,pdfurl):
    pdfhtml = visiturl(pdfurl)
    with open(r'D:\学习资料\百度学术'+'\\'+ title +'.pdf', 'wb') as pdfFile:
        pdfFile.write(pdfhtml)
#http.client.IncompleteRead

# with open(r'helloworld_python\HTML\ai.html', 'r', encoding='utf-8') as aihtml:
#     pagesource = aihtml.read()
if __name__ == '__main__':
    input_keywords = input('请输入搜索的英文关键词，格式如(Mo%20SPS):')
    input_pages = input('请输入想要下载的文件数量')
    url = 'https://www.sciencedirect.com/search?qs='+input_keywords + '&show=25&sortBy=relevance' 
    browser = webdriver.Chrome()
    #最大化窗口
    # browser.maximize_window()
    browser.get(url)
    cookies = browser.get_cookies()

    get_page = 0
    search_result = {}
    search_result_keyword = {}
    while get_page < int(input_pages):
        try:
            locator = (By.ID,"footer")
            ele = WebDriverWait(browser,10).until(EC.presence_of_element_located(locator))
            pagesource = browser.page_source
        except:
            pass
        soup = BeautifulSoup(pagesource, 'lxml')
        article_dict = search_c() #获取a标签连接并返回字典数据
        ####获取文章链接，并下载，记录保存状态
        # for each_a in article_dict:
        #     fakeurl = article_dict[each_a]['pdflink'] #在chrome打开所有连接
        #     writetitle = article_dict[each_a]['title'].replace('\\','-').replace('/','-')
        #     js = 'window.open("'+fakeurl+'");'
        #     browser.execute_script(js)
        #     elsevier_handler = browser.current_window_handle
        #     handles = browser.window_handles
        #     handles.remove(elsevier_handler)
        #     realpdfURL = getrealpdf(writetitle,handles[0])
        #     new_a_dict = article_dict[each_a]
        #     new_a_dict['realpdfURL'] = realpdfURL  #将新url赋给字典
        #     new_a_dict['readstatus'] = 'True' #赋给字典文件保存的状态
        #     new_a_dict['fileaddress'] = r'D:\学习资料\百度学术'+'\\'+ writetitle +'.pdf'
        #     search_result_keyword[article_dict[each_a]['title']] = new_a_dict
        #     browser.switch_to.window(elsevier_handler)
        #     sleep(2)


        for each_a in article_dict:
            pb_journal = article_dict[each_a]['publish'].split(',')[0]
            print(pb_journal)
            IF_list = searchjournal(pb_journal)
            new_a_dict = article_dict[each_a]
            if IF_list:
                new_a_dict['journalname'] = IF_list[2]
                new_a_dict['impactfactor'] = IF_list[0]
                new_a_dict['JCR'] = IF_list[1]
            else:
                new_a_dict['journalname'] = 'null'
                new_a_dict['impactfactor'] = 'null'
                new_a_dict['JCR'] = 'null'               
            search_result_keyword[article_dict[each_a]['title']] = new_a_dict
        get_page += len(article_dict)
        browser.get(url + '&offset=' + str(get_page))
    search_result[input_keywords] = search_result_keyword
    with open('D://python_example//helloworld_python//HTML//'+input_keywords+'.json', 'w', encoding ='utf-8') as topfilm:
        filmdata = json.dumps(search_result,ensure_ascii=False)
        topfilm.write(filmdata)
    browser.quit()