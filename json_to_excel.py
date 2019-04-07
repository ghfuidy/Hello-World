###将jso文件转化为excel文件。未完成。。
import xlwt
import json
def readFromJson(file):
    with open(file, 'r', encoding='utf8') as fr:
        jsonData = json.load(fr)
    return jsonData

def writeToExcel(file):
    json = readFromJson(file)
    excel = xlwt.Workbook()
    sheet1 = excel.add_sheet(u'sheet1')
    sheet1.write(0,0,'title')
    sheet1.write(0,1,'pdflink')
    sheet1.write(0,2,'publish')
    sheet1.write(0,3,'authors')
    sheet1.write(0,4,'journalname')
    sheet1.write(0,5,'impactfactor')
    sheet1.write(0,6,'JCR')
    length = len(json)
    j = 0
    for i in json:
        title=i
        for each in json[i]:  
            sheet1.write(j+1,0,json[i][each]['title'])
            sheet1.write(j+1,1,json[i][each]['pdflink'])
            sheet1.write(j+1,2,json[i][each]['publish'])
            sheet1.write(j+1,3,json[i][each]['authors'])
            sheet1.write(j+1,4,json[i][each]['journalname'])
            sheet1.write(j+1,5,json[i][each]['impactfactor'])
            sheet1.write(j+1,6,json[i][each]['JCR'])
            j=j+1 
             

    excel.save('D://python_example//helloworld_python//HTML//'+title+'.xls')

if __name__ == '__main__':
    url = input('请输入链接')
    writeToExcel(url)