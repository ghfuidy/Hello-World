import requests
import urllib.request
import re
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from 代理ID import dailiip
from lxml import etree


headers = {
    'User-Agent':UserAgent().random
}

word_dict = []

def index():
    # word = ['','_1''_2','_3','_4']
    word = ['']
    # for num in range(10912614,10912633+1,1):
    for num in range(10912603,10912612+1,1):
        for down_page in word:
            baseurl = 'http://cet4-6.xdf.cn/201905/{}{}.html'.format(num,down_page)

            req = urllib.request.Request(baseurl, headers=headers)
            dailiip()
            try:
                response = urllib.request.urlopen(req,timeout=20)
                html = response.read().decode('utf-8')

            except:
                html=''
                print('html is nothing')
            
            assert isinstance(html,str), \
                'html must be str'
            clean(html)

def clean(html):
    soup = BeautifulSoup(html,'lxml')
    wordlist = soup.find('div',class_='air_con f-f0')

    if wordlist:
       fullword = wordlist.find_all('p')
       for each in fullword:
            # print(each.string)
            info_dict = {}
            try:
                reobj = re.search(r'[a-z]+',each.string)
                word = reobj.group()
                endstate = reobj.end()
                try:
                    # Interpretation = re.search(r'[a-z]+\.(.+)\(',each.string).group()
                    Interpretation = each.string[endstate:-1]
                    # Interpretation = Interpretation[0:-1]
                    print(Interpretation)
                except:
                    Interpretation = 'None'
                    # Interpretation = re.search(r'[^a-z]+[a-z|A-Z]+',each.string).group()
                # try: 
                #     wordroot = re.search(r'(\([^\s]+\))',each.string).group()
                # except:
                #     wordroot = 'None'
                wordroot = 'None'
            except:
                print(each.string + 'appear unexcepted error')
            info_dict['word'] = word
            info_dict['Interpretation'] = Interpretation
            info_dict['Wordroot'] = wordroot
            word_dict.append(info_dict)
    
    # pagenum = etree.HTML(html).xpath("////div[@class='article']/div[@class='ch_conpage hdd']/ul/li[1]/a")
    # print(pagenum)
    

# def xpaathclean(html):
#     wordlist = html.xpaath()

if __name__ == '__main__':
    index()
    with open('D://python_example//helloworld_python//HTML//六级常考词汇.json', 'w', encoding ='utf-8') as topfilm:
        filmdata = json.dumps(word_dict,ensure_ascii=False)
        topfilm.write(filmdata)