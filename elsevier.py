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

#收集页面信息
def search_c():
    part_l = soup.find_all('div', class_='result-item-content')
    article_msg = {}
    for each_p in part_l:
        title_l = each_p.h2.text.strip().split()
        # 文章标题
        title = ' '.join(title_l)
        # 下载链接
        d_link = each_p.find('a', class_='download-link')['href']
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
    except http.client.IncompleteRead:
        html = ''
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
    input_keywords = input('请输入搜索的英文关键词')
    input_pages = input('请输入想要下载的文件数量')
    url = 'https://www.sciencedirect.com/'
    browser = webdriver.Chrome()
    #最大化窗口
    # browser.maximize_window()
    browser.get(url)
    cookies = browser.get_cookies()

    try:
        locator = (By.ID,"close")
        ele = WebDriverWait(browser,10).until(EC.presence_of_element_located(locator))
        browser.find_element_by_id('close').click()
    except:
        pass

    browser.find_element_by_name('qs').send_keys(input_keywords)
    browser.find_element_by_name('qs').send_keys(Keys.ENTER)
    get_page = 0
    while get_page < input_pages:
        pagesource = browser.page_source
        soup = BeautifulSoup(pagesource, 'lxml')
        article_dict = search_c() #获取a标签连接并返回字典数据
        for each_a in article_dict:
            fakeurl = article_dict[each_a]['pdflink'] #在chrome打开所有连接
            writetitle = article_dict[each_a]['title'].replace('\\','-')
            js = 'window.open("'+fakeurl+'");'
            browser.execute_script(js)
            elsevier_handler = browser.current_window_handle
            handles = browser.window_handles
            handles.remove(elsevier_handler)
            getrealpdf(writetitle,handles[0])
            browser.switch_to.window(elsevier_handler)
            sleep(2)
        browser.find_element_by_class_name('pagination-link next-link').click()
        get_page += len(article_dict)
    browser.quit()
