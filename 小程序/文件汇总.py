import xlrd, xlwt


myWorkbook = xlrd.open_workbook(r'D:\laowu.xlsx')

mySheets = myWorkbook.sheets()

mySheet = myWorkbook.sheet_by_index(0)

f = xlwt.Workbook() 
sheet = f.add_sheet(u'137学位会')



for i in range(1,106,1):
    str1 = ''
    str2 = ''
    myRowValues = mySheet.row_values(i)
    if myRowValues[5]:
        str1 += '500/次（学位分会）\n'
        str2 += '1(学位分会)\n'
    if myRowValues[6]:
        str1 += '800/次（专家详审会）\n'
        str2 += '1（专家详审会）\n'
    if myRowValues[7]:
        str1 += '500/次（校学位会）\n'
        str2 += '1（校学位会）\n'
    if myRowValues[9]:
        str1 += '200/本（有条件论文评阅）'
        str2 = str2 + str(myRowValues[9]) + '（有条件论文评阅）'
    sheet.write(i,0,myRowValues[0])
    sheet.write(i,1,myRowValues[1])
    sheet.write(i,2,myRowValues[2])
    sheet.write(i,3,myRowValues[4])
    sheet.write(i,4,str1)
    sheet.write(i,5,str2)
    sheet.write(i,6,myRowValues[11])

f.save('xlwt_test.xls')