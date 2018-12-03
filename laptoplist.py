import requests
import re
import json
import time
from bs4 import BeautifulSoup
import 代理ID
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
 
#获取一页编号
def get_bianhao(url):
    res=requests.get(url,headers=headers,timeout=20)
    res.encoding=res.apparent_encoding
    soup=BeautifulSoup(res.text,'html.parser')
    bianhao=soup.select('#J_goodsList > ul > li > div > div.p-img > a')
    bianhao1=list(map(lambda x:x['href'],bianhao))
    bianhaos=[]
    for bh in bianhao1:
        bianhao2=re.findall(r'//item.jd.com/(\d+).html',bh)
        if bianhao2 != []:
            bianhaos.append(bianhao2[0])
        else:
            pass
    return bianhaos
#获取笔记本标题和品牌
total={}
def get_shangpin(id):
    url='https://item.jd.com/'+id+'.html'
    代理ID.dailiip()
    laptop_param={}
    try:
        res=requests.get(url,headers=headers,timeout=20)
        res.encoding=res.apparent_encoding
        soup=BeautifulSoup(res.text,'html.parser')
        try:
            # URLJ='https://p.3.cn/prices/mgets?callback=jQuery2224728&type=1&area=1_72_2799_0&pdtk=&pduid=401650232&pdpin=&pin=null&pdbp=0&skuIds=J_'+id+'%2C'
            URLJ = 'http://p.3.cn/prices/mgets?skuIds=J_' + id
            price = get_jiage(URLJ)
            #获取品牌
            pinpai=soup.select('#parameter-brand > li > a')
            pinpai1=pinpai[0].text.strip()
            #各项详细参数
            Ptable_part = str(soup.find('div',class_='Ptable'))
            parameter2_part = str(soup.find('ul',class_='parameter2'))
            lapclass = get_infos('系列',Ptable_part,parameter2_part)
            laptype = get_infos('型号',Ptable_part,parameter2_part)
            Memory_capacity = get_infos('(内存容量|系统内存)',Ptable_part,parameter2_part)
            Memory_type = get_infos('内存类型',Ptable_part,parameter2_part)
            CPU_type = get_infos('(CPU型号|CPU类型|处理器)',Ptable_part,parameter2_part)
            CPU_Num = get_infos('核心',Ptable_part,parameter2_part)
            Harddisk = get_infos('硬盘容量',Ptable_part,parameter2_part)
            Harddisk_solid = get_infos('固态硬盘',Ptable_part,parameter2_part)
            Harddisk_type = get_infos('(类型|存储容量|硬盘容量)',Ptable_part,parameter2_part)
            DP = get_infos('(显示芯片|显卡型号)',Ptable_part,parameter2_part)
            DPchip_capacity = get_infos('显存容量',Ptable_part,parameter2_part)
            Lap_size = get_infos('尺寸',Ptable_part,parameter2_part)
            lap_weight = get_infos('(净重|裸机重量)',Ptable_part,parameter2_part)
            screen_size = get_infos('屏幕规格',Ptable_part,parameter2_part)
            screen_type = get_infos('屏幕类型',Ptable_part,parameter2_part)

            laptop_param = {'品牌':pinpai1,
            '系列':lapclass,
            '型号':laptype,
            '内存容量':Memory_capacity,
            '内存类型':Memory_type,
            'CPU型号':CPU_type,
            '核心':CPU_Num,
            '硬盘容量':Harddisk,
            '固态硬盘':Harddisk_solid,
            '类型':Harddisk_type,
            '显示芯片':DP,
            '显存容量':DPchip_capacity,
            '尺寸':Lap_size,
            '净重':lap_weight,
            '屏幕规格':screen_size,
            '屏幕类型':screen_type,
            '价格':price,
            '商品编号':id}
            name = pinpai1 + lapclass + laptype
            total[name] = laptop_param
        except Exception as errorept:
            print(repr(errorept),url)
            with open('helloworld_python//HTML//'+id+'.html','wb') as jindong:
                jindong.write(res.text.encode('utf-8'))
            print('ok')
    except Exception as e:
        print(repr(e))
        print(url,'erroe http')
#获取笔记本价格
def get_jiage(url):
    rj=requests.get(url,headers=headers,timeout=20)
    jdj=json.loads(rj.text.lstrip('jQuery2224728([').rstrip(']);\n'))
    return jdj['p']

def get_infos(Obj,page_content,sub_page):
    pattern = '<dt>'+ Obj +'</dt>.*?<dd>(.*?)</dd>'
    result = re.findall(pattern, page_content)
    if len(result) == 0:
        pattern = '<li title=".*?">'+ Obj +'.*?</li>'
        result = re.search(pattern,sub_page)
        if result != None:
            result = result.group().split('：')[1].strip('</li>')
        else:
            result = '空'
    elif isinstance(result[0],list):
        result = result[0][1]
    else:
        result = result[0]
    return result

if __name__ == '__main__':
    for i in range(1,20):
        URL='https://search.jd.com/search?keyword=笔记本电脑&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V01&wq=笔记本&page=5'+str(2 * i - 1)  
        for id in get_bianhao(URL):
            print(id)
            get_shangpin(id)
            time.sleep(0.5)
 
print(total)
with open(r"D:\学习资料\书籍PDF文件\laptoplist.json", 'w', encoding='utf-8') as json_file:
    json.dump(total, json_file,ensure_ascii=False)