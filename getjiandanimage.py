import urllib.request
import os
import base64
import random

def url_open(url):
    useragent_list = ['Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
                      'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                      'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
                      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    useraggent_choose = useragent_list[random.randint(0,4)]
    header = {
        'User-Agent':useraggent_choose,
    }
    req = urllib.request.Request(url,headers=header)

    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('righttext') + 43
    b = html.find('#', a)
    print(html[a:b])
    return(html[a:b])


def find_img(url):
    html = url_open(url).decode('utf-8')
    img_address = []

    a = html.find('img-hash')
    while a != -1:
        b = html.find('</span>', a, a+255)
        if b != -1:
            img_hash = html[a+10:b]
            realurl = base64.b64decode(img_hash).decode('utf-8')
            renewurl = 'http:' + realurl
            print(renewurl)
            img_address.append(renewurl)
        else:
            b = a + 9

        a = html.find('img-hash', b)

    return img_address


def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_img(folder=r'OOXX', pages=10):
    try:
        os.mkdir(folder)
        os.chdir(folder)
    except FileExistsError:
        os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_url = url + 'page-' + str(page_num) + '#comments'
        page_num -= 1
        print(page_url)
        img_address = find_img(page_url)
        save_imgs(folder,img_address)


if __name__ == '__main__':
    download_img()
