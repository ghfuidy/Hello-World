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
            'http://thz6.com/forum.php?mod=forumdisplay&fid=197&sortid=2&sortid=2&page=' + str(i)).decode('utf-8')
        # if i == 5:
        #     with open('html/thzla1.html', 'wb') as thzla:
        #         thzla.write(html.encode('utf-8'))
        a = html.find('<div class="c cl">')
        while a != -1:
            b = html.find('onclick="atarget(this)"', a)
            if b != -1:
                # 获取番号
                BTname = html[b+32:b+39]
                # 获取完整地址
                fullhttp = 'http://thz6.com/' + html[a+29:b-3]
                # 获取图片（暂缺）
                tha_list[BTname] = fullhttp
            else:
                print('end')
                b = a + 50
            a = html.find('<div class="c cl">', b)
    return tha_list
    # 将数据保存为一个json文件
    # jsondata = json.dumps(tha_list)
    # with open('html/thzla1.json', 'a') as f:
    #     f.write(jsondata)


def getBTaddress(thz_dict):
    for each in thz_dict:
        # print(thz_dict[each])
        代理ID.dailiip()
        html = 代理ID.openurl(thz_dict[each]).decode('utf-8')
        a = html.find('<ignore_js_op>')
        b = html.find('zoomfile', a)
        # h获取第二个<ignore_js_op>,得到正反封面图
        a = a = html.find('<ignore_js_op>', b)
        b = html.find('zoomfile', a)
        c = re.search(r'\.jpg|\.gif', html[b:])
        if html[b+11] == 'd':
            if c:
                img_url = html[b+11:b+c.end()]
                img_url = 'http://thz6.com/' + img_url
            else:
                print('error')
        elif html[b+11] == 't':
            img_url = html[b+10:b+c.end()]
        # 获取下载页面链接
        d = html.find('vm', b)
        e = html.find('imc_attachad-ad', d)
        g = html.find('target', e)
        if g-e < 255:
            print(g-e)
            download_page = html[e:g-3]
            full_page = 'http://thz6.com/' + download_page
        else:
            full_page = ''
        # #BT的下载链接
        if full_page != 'http://thz6.com/':
            downloadhtml = 代理ID.openurl(full_page).decode('utf-8')
            BT_a = downloadhtml.find('<div style="padding-left:10px;">')
            BT_b = downloadhtml.find('onclick', BT_a)
            BTurl = downloadhtml[BT_a+41:BT_b-2]
        else:
            BTurl = ''
        # 链接合并为字典
        thz_full = {}
        thz_full['introduceurl'] = thz_dict[each]
        thz_full['imgurl'] = img_url
        thz_full['downloadurl'] = full_page
        thz_full['BTurl'] = BTurl
        thz_dict[each] = thz_full
        print(thz_dict[each])
    with open('html/ABP.json', 'w') as thz_full_json:
        thzdata = json.dumps(thz_dict)
        thz_full_json.write(thzdata)
    return thz_dict


def thz_docx(thz_dict):
    document = Document()
    document.add_heading('ABP系列', level=1)

    for each in thz_dict:
        p = document.add_paragraph(each)
        p.bold = True
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        代理ID.dailiip()
        imageData = 代理ID.openurl(thz_dict[each]['imgurl'])
        image_io = BytesIO()
        image_io.write(imageData)
        image_io.seek(0)
        document.add_picture(image_io, width=Inches(5))
        image_io.close()
        p = document.add_paragraph(thz_dict[each]['BTurl'])
    document.save('html/ABP.docx')


if __name__ == '__main__':
    listurl = getSNIS()
    thz_dict = getBTaddress(listurl)
    thz_docx(thz_dict)
