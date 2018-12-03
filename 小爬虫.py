import urllib.request
import json

# response = urllib.request.urlopen('http://placekitten.com/g/500/400')
# cat_img = response.read()

# with open(r'C:\Users\Administrator\Desktop\cat.jpg', 'wb') as f:
#     f.write(cat_img)
# # cat_img.save(r'C:\Users\Administrator\Desktop\cat.jpg')
# #-----------------------------------------

# req = urllib.request.Request('http://placekitten.com/g/500/400')
# response = urllib.request.urlopen(req)

# print(response.geturl())
# print(response.info())
# print(response.getcode())

# cat_img = response.read()

# with open(r'C:\Users\Administrator\Desktop\cat.jpg', 'wb') as f:
#     f.write(cat_img)
# #-------------------------

import urllib.parse
import hashlib
import time
import random
import requests

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
}

###代理IP防验证

content = input('输入你想翻译的内容')
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
print(text)

infos = json.loads(text)
if 'translateResult' in infos:
    try:
        yuanwen = infos['translateResult'][0][0]['src']
        result = infos['translateResult'][0][0]['tgt']
        smartresult = infos['smartResult']['entries']
        print(yuanwen,'的翻译是',result)
        print(smartresult)
        for each in smartresult:
            print(each)
    except:
        pass
# # -------------------------------

# # #测试成功，可以使用
# # -*- coding: utf-8 -*-
# # import requests
# # import hashlib
# # import time
# # import json
# # import random


# class Youdao(object):
#     def __init__(self, msg):
#         self.msg = msg
#         self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#         self.D = "ebSeFb%=XZ%T[KZ)c(sy!"
#         self.salt = self.get_salt()
#         self.sign = self.get_sign()

#     def get_md(self, value):
#         '''md5加密'''
#         m = hashlib.md5()
#         # m.update(value)
#         m.update(value.encode('utf-8'))
#         return m.hexdigest()

#     def get_salt(self):
#         '''根据当前时间戳获取salt参数'''
#         s = int(time.time() * 1000) + random.randint(0, 10)
#         return str(s)

#     def get_sign(self):
#         '''使用md5函数和其他参数，得到sign参数'''
#         s = "fanyideskweb" + self.msg + self.salt + self.D
#         return self.get_md(s)

#     def get_result(self):
#         '''headers里面有一些参数是必须的，注释掉的可以不用带上'''
#         headers = {
#             # 'Accept': 'application/json, text/javascript, */*; q=0.01',
#             # 'Accept-Encoding': 'gzip, deflate',
#             # 'Accept-Language': 'zh-CN,zh;q=0.9,mt;q=0.8',
#             # 'Connection': 'keep-alive',
#             # 'Content-Length': '240',
#             # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#             'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
#             # 'Host': 'fanyi.youdao.com',
#             # 'Origin': 'http://fanyi.youdao.com',
#             'Referer': 'http://fanyi.youdao.com/',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
#             # 'X-Requested-With': 'XMLHttpRequest'
#         }
#         data = {
#             'i': self.msg,
#             'from': 'AUTO',
#             'to': 'AUTO',
#             'smartresult': 'dict',
#             'client': 'fanyideskweb',
#             'salt': self.salt,
#             'sign': self.sign,
#             'doctype': 'json',
#             'version': '2.1',
#             'keyfrom': 'fanyi.web',
#             'action': 'FY_BY_CL1CKBUTTON',
#             'typoResult': 'true'
#         }
#         html = requests.post(self.url, data=data, headers=headers).text
#         print(html)
#         infos = json.loads(html)
#         if 'translateResult' in infos:
#             try:
#                 result = infos['translateResult'][0][0]['tgt']
#                 print(result)
#             except:
#                 pass


# if __name__ == '__main__':
#     y = Youdao('我还就是杠上了')
#     y.get_result()

# # ------------------------------------------

# #另一种方法
# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# import requests
# import hashlib
# import time
# from pprint import pprint


# url = "http://fanyi.youdao.com/translate_o"
# params = {
#     "smartresult": "dict",
#     "smartresult": "rule"
# }


# salt = str(time.time())
# client = "fanyideskweb"
# text = input("请输入翻译内容：")
# AppKey = "ebSeFb%=XZ%T[KZ)c(sy!"
# sign = hashlib.md5((client+text+salt+AppKey).encode('utf-8')).hexdigest()


# data = {
#     "i": text,
#     "from": "AUTO",
#     "to": "AUTO",
#     "smartresult": "dict",
#     "client": client,
#     "salt": salt,
#     "sign": sign,
#     "doctype": "json",
#     "version": "2.1",
#     "keyfrom": "fanyi.web",
#     "action": "FY_BY_CLICKBUTTION",
#     "typoResult": "false"
# }

# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
#     "Referer":"http://fanyi.youdao.com/?keyfrom=dict2.index",
#     "Cookie":"OUTFOX_SEARCH_USER_ID_NCOO=1082072868.6526275; OUTFOX_SEARCH_USER_ID=2072418438@218.82.240.196; YOUDAO_EAD_UUID=800e3e66-ce9f-442d-adbf-9b3979a21a3e; _ntes_nnid=2fe3d5c70463d0c7d9cb34cd85f28f28,1526368710759; fanyi-ad-id=44881; fanyi-ad-closed=1; P_INFO=tige112@163.com|1527857737|2|mail163|11&19|shh&1527852495&youdaodict_client#shh&null#10#0#0|&0|youdaodict_client&mail163|tige112@163.com; JSESSIONID=abclAXKrY2C2GhDODT_ow; DICT_LOGIN=8||1527913051232; DICT_FORCE=true; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1527913197589"
# }


# response = requests.post(url=url,params=params,data=data,headers=headers)

# pprint(response.json())
