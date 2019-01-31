# import json
# import urllib.request
# import urllib.parse
# import 代理ID

# with open(r'D:\学习资料\书籍PDF文件\word_list.json','r',encoding='utf-8') as aimfile:
#     filedata = aimfile.read()

# jsondata = json.loads(filedata)

# url = 'https://d.apicloud.com/mcm/api/collected_word'

# for eachkey in jsondata:
#     ###word:eachkey
#     ###definition：jsondata[eachkey]
#     requestdata = {
# 	"word": eachkey,
# 	"definition": jsondata[eachkey],
# 	"repeat_times": 1
#     }

#     headers = {
#     "X-APICloud-AppId": "A6090416458893",
#     "X-APICloud-AppKey": "your appkey"
#     }
    
#     data=urllib.parse.urlencode(requestdata).encode(encoding='utf-8')
#     request = urllib.request.Request(url, data=data, headers=headers,method='POST')
    
#     # request.add_header('Content-Type', 'application/json; charset=utf-8')
#     # request.add_header('X-Requested-With','XMLHttpRequest')
#     # request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")

#     html = ''
#     response = urllib.request.urlopen(request)
#     if response is not None:
#         html = response.read()

# ####
import json
import requests
import hashlib
import time
import urllib

# def updata_all():
#     with open(r'D:\学习资料\书籍PDF文件\word_list.json','r',encoding='utf-8') as aimfile:
#         filedata = aimfile.read()

#     jsondata = json.loads(filedata)

#     url = 'https://d.apicloud.com/mcm/api/collected_word'
#     appId = "A6090416458893"
#     appKey = "5A0C5F35-7104-30D2-1AD7-B5F6864C910E"
#     timeStamp = int(time.time()*1000)
#     APPKey = hashlib.sha1((appId + "UZ" + appKey + "UZ" + str(timeStamp)).encode('utf-8')).hexdigest() + "." + str(timeStamp)



#         headers = {
#         "X-APICloud-AppId": appId,
#         "X-APICloud-AppKey": APPKey
#         }

#         headers["Content-Type"] = "application/json"

#         try:
#             response = requests.post(url,headers=headers, data=json.dumps(requestdata))
#         except Exception as e:
#             print(repr(e))
#         print(response.json())

class apicloudSource():
    """
    功能主要简述：主要是将电脑上的单词传输到apicloud云端上
    用来对特定app使用，所以APPid和APPkey输入常量
    """
    def __init__(self):
        with open(r'D:\学习资料\书籍PDF文件\word_list.json','r',encoding='utf-8') as aimfile:
            filedata = aimfile.read()
            self.worddict = json.loads(filedata)
        self.appId = "A6090416458893"
        self.appkey = "5A0C5F35-7104-30D2-1AD7-B5F6864C910E"
        timeStamp = int(time.time()*1000)
        self.APPKey = hashlib.sha1((self.appId + "UZ" + self.appkey + "UZ" + str(timeStamp)).encode('utf-8')).hexdigest() + "." + str(timeStamp)
        self.url = 'https://d.apicloud.com/mcm/api/collected_word'
        self.headers = {
			"X-APICloud-AppId":self.appId,
			"X-APICloud-AppKey":self.APPKey
		}
        self.cloudlist = set()    #云端数据的列表
        self.locallist = set()  #本地数据的集合


    def getalldata(self,id=None,obj_name=None):
        """
        获取单词总量，取得所有单词的列表，比较云端与本地的差异，并进行单词更新操作
        """
        if id or obj_name:
            print('get point data')
        else:
            counturl = self.url + "/count"
            countres = requests.get(counturl, headers = self.headers)
            wordnum = countres.json()['count']
            
            skip = 0

            while skip < wordnum:
                field = '{"where":{},"skip":'+ str(skip) +',"limit":50}'
                code_field = urllib.parse.quote(field)
                cloudurl = self.url + '?filter=' + code_field
                
                clouddata = requests.get(cloudurl, headers=self.headers)
                for each in clouddata.json():
                    self.cloudlist.add(each['word'])
                skip += 50

            for eachkey in self.worddict:
                self.locallist.add(eachkey)

            dif_word = self.locallist.difference(self.cloudlist)
            
        return dif_word

    def dellocalword(self,obj_d_l):
        for each in obj_d_l:
            del self.worddict[each]

    def addcloudword(self,obj_d_l):
        headers = self.headers
        headers["Content-Type"] = "application/json"
        
        for each in obj_d_l:
            everyword = {
                "word": each,
                "definition": self.worddict[each],
                "repeat_times": 1
            }

            try:
                response = requests.post(self.url,headers=headers, data=json.dumps(everyword))
            except Exception as e:
                print(repr(e))
            print(response.json())

resourcedata = apicloudSource()
dif_word = resourcedata.getalldata()
resourcedata.addcloudword(dif_word)
