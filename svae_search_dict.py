import urllib.request
import json
import urllib.parse
import hashlib
import time
import random
import requests
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import StringVar, IntVar


class Application(Frame):
    root = Tk()
    searchmessage = StringVar()
    searchmessage.set('搜索结果是：')
    svaestatus = StringVar()
    searchmessage.set('无信息')

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        with open(r"D:\学习资料\书籍PDF文件\word_list.json", 'rb') as json_file:
            self.json_file = json_file
            self.jsondata = json.load(json_file)

    def createWidgets(self):
        self.search = Entry(self)
        self.search.pack()
        self.seaechButton = Button(self, text='search', command=self.searchword)
        self.seaechButton.pack()
        self.show_searchmessage = Label(self, textvariable=Application.searchmessage)
        self.show_searchmessage.pack()
        self.save_status = Label(self, textvariable=Application.svaestatus)
        self.save_status.pack()

    def searchword(self):
        key = self.search.get()
        infos = self.translate()
        if 'translateResult' in infos:
            try:
                # yuanwen = infos['translateResult'][0][0]['src']
                # result = infos['translateResult'][0][0]['tgt']
                smartresult = infos['smartResult']['entries']
                keyvalue = ''
                for each in smartresult:
                    keyvalue += each
            except:
                keyvalue = ''
        Application.searchmessage.set(keyvalue)
        if key != '' and keyvalue != '':
            self.jsondata[key] = keyvalue
            with open(r"D:\学习资料\书籍PDF文件\word_list.json", 'w', encoding='utf-8') as json_file:
                json.dump(self.jsondata, json_file,ensure_ascii=False)
            Application.svaestatus.set('储存成功')
        else:
            Application.svaestatus.set('储存失败')

    # def searchcss(self):
    #     search_value = self.search.get()
    #     Application.searchmessage.set(self.jsondata[search_value])

    def translate(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
        }

        ###代理IP防验证

        content = self.search.get()
        salt = str(int(time.time() * 1000) + random.randint(0, 10))
        client = "fanyideskweb"
        AppKey = "ebSeFb%=XZ%T[KZ)c(sy!"
        sign = hashlib.md5((client+content+salt+AppKey).encode('utf-8')).hexdigest()

        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


        data = {}

        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = salt
        data['sign'] = sign
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTIME'
        data['typoResult'] = 'false'

        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers)
        ###利用urllib package 需要加上header
        response = urllib.request.urlopen(req)

        text = response.read().decode('utf-8')

        infos = json.loads(text)
        return infos

app = Application()
# 设置窗口标题:
app.master.title('add Json')
app.master.geometry('400x200')#窗体大小
# app.root.protocol("WM_DELETE_WINDOW", app.callback())
# 主消息循环:
app.mainloop()