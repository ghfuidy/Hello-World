import 代理ID
import openpyxl
import re
import json

# def getdoubansortdata(sort,tags):
#     #sort有三个分类,T:热度,R:时间，S:评价
#     代理ID.dailiip()
#     response = 代理ID.openurl('https://movie.douban.com/tag/#/?sort='+sort+'&range=0,10&tags='+tags).decode('utf-8')
#     with open('helloworld_python/HTML/douban.html','wb') as douban:
#         douban.write(response.encode('utf-8'))
# ###豆瓣sort需要利用到app.js，暂时搁置

def getdoubanTOPdata():
    # 代理ID.dailiip()
    full_film = {}
    for i in range(0,250,25):
        response = 代理ID.openurl('https://movie.douban.com/top250?start='+ str(i) +'&filter=').decode('utf-8')
        # with open('helloworld_python/HTML/doubanTOP.html','wb') as douban:
        #     douban.write(response.encode('utf-8'))
        ol_s = response.find('grid_view')
        ol_end = response.find('</ol>')
        while ol_end - ol_s > 300:
            number = re.search(r'\d?\d?\d',response[ol_s:])
            name = re.search(r'[\u4e00-\u9fa5]+',response[ol_s:])
            realname = name.group()
            br_split = response.find('<br>',ol_s)
            p_split = response.find('</p>',br_split)
            score = re.search(r'\d\.\d',response[ol_s:])
            nation_str = response[br_split+4:p_split].rstrip().replace(' ','').replace('\n','')
            a,b,c = nation_str.split('&nbsp;/&nbsp;')
            inq = response.find('inq',ol_s)
            inq_end = response.find('</span>',inq)
            geyan = response[inq+5:inq_end]
            top250 = {}
            top250['排名'] = number.group()
            top250['上映年份'] = a
            top250['国家'] = b
            top250['类别'] = c
            top250['评分'] = score.group()
            top250['评价'] = geyan
            full_film[realname] = top250
            # print('排名是{},名字是{},上映年份是{},国家是{},类别是{},评分是{},评价是{}\n'.format(number.group(),name.group(),a,b,c,score.group(),geyan))
            ol_s = inq_end
    with open('helloworld_python/HTML/TOP250.json', 'w', encoding ='utf-8') as topfilm:
        filmdata = json.dumps(full_film,ensure_ascii=False)
        topfilm.write(filmdata)

if __name__ == '__main__':
    getdoubanTOPdata()