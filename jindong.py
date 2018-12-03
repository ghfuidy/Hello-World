#!/usr/bin/env python
# author: Cedric Porter [ Stupid ET ] 
# contact me: cedricporter@gmail.com

from urllib.request import urlopen
import threading
import re
import queue

f = open('data.txt', 'w')   # output file
g_c = 0                     # counter, for telling us the process
g_done = False              # end flag
g_mutex = threading.Lock()  # mutex

def get_info(url):
    '''abstracts product info '''
    p = re.compile('<tr><td .*?>(.*?)</td><td>(.*?)</td></tr>')
    text = urlopen(url).read()
    info = []
    
    for t, v in p.findall(text):
        info.append((t, v))

    return info

def get_urls(page_url):
    '''gets product urls from a page'''
    p = re.compile(r"<div class='p-name'><a target='_blank' href='(.*?)'>", re.S)
    text = urlopen(page_url).read().decode('utf-8')

    urls = []
    for url in p.findall(text):
        urls.append(url)

    return urls

def get_page_urls():
    '''creates urls of the pages'''
    page_urls = []
    for i in range(1, 23):
        page_urls.append('http://www.360buy.com/products/670-671-672-0-0-0-0-0-0-0-1-1-%d.html'% i)
    return page_urls

def product_worker(product_url_queue):
    '''thread of product worker, downloads product info'''
    global g_mutex, f, g_c, g_done
    while not g_done or product_url_queue.qsize() > 0:
        url = product_url_queue.get()
        try:
            info = get_info(url)
        except Exception as e:
            product_url_queue.put(url)
            print(e)
            continue

        g_mutex.acquire()
        print('==>',g_c)
        g_c += 1
        for t, v in info:
            f.write(t + ':::' + v + '\n')
        f.write('\n#####\n')
        f.flush()
        g_mutex.release()

def page_urls_worker(product_url_queue, page_url):
    '''thread function of page urls worker, downloads page urls'''
    for product_url in get_urls(page_url):
        product_url_queue.put(product_url)
        print('.')

def main():
    global g_done
    threading_pool = []
    q = queue.Queue()
    num_product_worker = 50

    for i in range(num_product_worker):
        th = threading.Thread(target=product_worker, args=(q,))
        threading_pool.append(th)
        th.start()

    page_urls_worker_pool = []
    for page_url in get_page_urls():
        pth = threading.Thread(target=page_urls_worker, args=(q, page_url))
        pth.start()
        page_urls_worker_pool.append(pth)

    for th in page_urls_worker_pool:
        threading.Thread.join(th)

    g_done = True

    for th in threading_pool:
        threading.Thread.join(th)


if __name__=='__main__':
    main()
