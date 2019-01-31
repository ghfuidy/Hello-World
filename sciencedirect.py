###这个脚本是用来用class来重构elsevier脚本的
###有空再说吧，先把谷歌的chrome驱动版写完
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

class getScienceDirect():
    def __init__(self,keywords,geturl):
        self.keywords = keywords
        self.geturl = geturl
        
    def search_c(self):
        pass
    
    def achievearticle(self):
            browser = webdriver.Chrome()
            browser.get(self.geturl)
            cookies = browser.get_cookies()