import 代理ID
import json
import re
from docx import Document
from io import BytesIO
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def getSNIS():
    代理ID.dailiip()
    tha_list = {}
    for i in range(1, 16):
        html = 代理ID.openurl(
            'http://thz6.com/forum.php?mod=forumdisplay&fid=204&sortid=2&sortid=2&page=' + str(i)).decode('utf-8')
        # if i == 5:
        #     with open('html/thzla1.html', 'wb') as thzla:
        #         thzla.write(html.encode('utf-8'))
        a = html.find('<div class="c cl">')
        while a != -1:
            b = html.find('onclick="atarget(this)"', a)
            if b != -1:
                # 获取番号
                BTname = html[b+32:b+40]
                # 获取完整地址
                fullhttp = 'http://thz6.com/' + html[a+29:b-3]
                # 获取图片（暂缺）
                tha_list[BTname] = fullhttp
            else:
                print('end')
                b = a + 50
            a = html.find('<div class="c cl">', b)

    # 将数据保存为一个json文件
    jsondata = json.dumps(tha_list)
    with open('html/thzla1.json', 'a') as f:
        f.write(jsondata)


def getBTaddress():
    with open('html/thzla1.json', 'r') as thzjson:
        jsondata = thzjson.read().encode('utf-8')
        thz_dict = json.loads(jsondata)
        for each in thz_dict:
            # print(thz_dict[each])
            代理ID.dailiip()
            html = 代理ID.openurl(thz_dict[each]).decode('utf-8')
            a = html.find('<ignore_js_op>')
            b = html.find('zoomfile', a)
            #h获取第二个<ignore_js_op>,得到正反封面图
            a = a = html.find('<ignore_js_op>', b)
            b = html.find('zoomfile', a)
            c = re.search(r'(.jpg)|(.gif)', html[b:])
            if html[b+11] == 'd':
                if c:
                    img_url = html[b+11:b+c.end()]
                    img_url = 'http://thz6.com/' + img_url
                else:
                    print('error')
            elif html[b+11] == 't':
                img_url = html[b+10:b+c.end()]
            #获取下载页面链接
            d = html.find('vm', b)
            e = html.find('imc_attachad-ad', d)
            g = html.find('target',e)
            if g-e < 255:
                download_page = html[e:g-3]
                full_page = 'http://thz6.com/'+ download_page
            else:
                full_page = ''
            # #BT的下载链接
            if full_page != '':
                downloadhtml = 代理ID.openurl(full_page).decode('utf-8')
                BT_a = downloadhtml.find('<div style="padding-left:10px;">')
                BT_b = downloadhtml.find('onclick',BT_a)
                BTurl = downloadhtml[BT_a+41:BT_b-2]
            else:
                BTurl = ''
            #链接合并为字典
            thz_full = {}
            thz_full['introduceurl'] = thz_dict[each]
            thz_full['imgurl'] = img_url
            thz_full['downloadurl'] = full_page
            thz_full['BTurl'] = BTurl
            thz_dict[each] = thz_full
            print(thz_dict[each])
    with open('html/thzla.json', 'w') as thz_full_json:
        thzdata = json.dumps(thz_dict)
        thz_full_json.write(thzdata)


# downloadhtml = 代理ID.openurl(full_page).decode('utf-8')
# BT_a = downloadhtml.find('"http://thz6.com/forum.php?mod=attachment&aid=')
# BT_b = downloadhtml.find('onclick',BT_a)
# print(BT_a,BT_b,downloadhtml[BT_a:BT_b-2])

# def getdownload_url():
#     with open('html/thzla.json', 'r') as thzfulljson:
#         jsondata = thzfulljson.read().encode('utf-8')
#         thz_fulldict = json.loads(jsondata)
#         for each in  thz_fulldict:
#             down_url = thz_fulldict[each]['downloadurl']
#             代理ID.dailiip()
#             downloadhtml = 代理ID.openurl(down_url).decode('utf-8')
#             # with open('html/thzla1.html', 'wb') as thzla:
#             #     thzla.write(downloadhtml.encode('utf-8'))
#             BT_a = downloadhtml.find('<div style="padding-left:10px;">')
#             BT_b = downloadhtml.find('onclick',BT_a)
#             print(downloadhtml[BT_a+41:BT_b-2])
#             thz_fulldict[each]['BTurl'] = downloadhtml[BT_a+41:BT_b-2]

print('start')
getBTaddress()