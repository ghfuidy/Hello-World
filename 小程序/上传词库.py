import urllib.request
import json
import urllib.parse
import hashlib
import requests
import time

timeStamp = int(time.time()*1000)
appId = "A6090416458893"
appkey = "5A0C5F35-7104-30D2-1AD7-B5F6864C910E"
APPKey = hashlib.sha1((appId + "UZ" + appkey + "UZ" + str(
            timeStamp)).encode('utf-8')).hexdigest() + "." + str(timeStamp)

headers = {
    "X-APICloud-AppId": "A6090416458893",
    "X-APICloud-AppKey" : APPKey,
    "Content-Type" : "application/json",
}

with open(r"D:\CODE\文献单词本\res\collected_word.json", 'rb') as json_file:
    # jsondata = json.load(json_file)
    text = json_file.read().decode('utf-8')
    wordata = json.loads(text)
    for each in range(0,len(wordata),1):
        everyword = {
            "word": wordata[each]['word'],
            "definition": wordata[each]['definition'],
            "repeat_times": 1,
            "user(uz*R*id)": "5ddbbad1ee8773a1406d7c9c",
        }
        try:
            response = requests.post("https://d.apicloud.com/mcm/api/collected_word", headers=headers, data=json.dumps(everyword))
        except Exception as e:
            print(repr(e))
        print(response.json())