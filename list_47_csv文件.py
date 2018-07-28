import csv, pprint

###csv文件读操作
def csvREADER(number_):
    exampleFile = open(r'D:\Download\comments.csv',encoding='utf-8', newline='')
    exampleReader = csv.reader(exampleFile)
    if number_ == 1:
        exampleData = list(exampleReader)
        pprint.pprint(exampleData)

        print(exampleData[1][3])
    elif number_ == 2:
        exampleFile.seek(0) ###将csv指针重新移动到首位
        for row in exampleReader:
            print('Row #'+ str(exampleReader.line_num) + str(row))

    exampleFile.close()

###csv文件写操作
def csvWRITE():
    outputFile = open('output.csv', 'w', newline='')

    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
    outputWriter.writerow(['hello world', 'eggs'])
    outputWriter.writerow([1, 2, 3.1415, 4])
    outputFile.close()

###更改csv文件的间隔符逗号和间距
def tsvFile():
    csvFile = open('example.tsv', 'w', newline='')
    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
    csvWriter.writerow(['apples','origins','grapes'])
    csvWriter.writerow(['eggs', 'bacon', 'ham'])
    csvFile.close()

p = input('输入执行标记')
if p == 'all':
    csvREADER(1)
    csvREADER(2)
    csvWRITE()
    tsvFile()
elif p == 'read':
    csvREADER(1)
    csvREADER(2)
elif p == 'write':
    csvWRITE()
elif p == 'tsv':
    tsvFile()
else:
    print('没有此选项，继续执行')

###removes the header from all CSV files in the current
import shutil
import pathlib

###拷贝对象文件夹到目标文件夹
srcPath = 'D:\\CODE\\数据存储'
destPATH = 'D:\\CODE\\removeHead'

withHeaderPath = pathlib.Path(srcPath)
withoutHeaderPath = pathlib.Path(destPATH)

if not withoutHeaderPath.exists():
    shutil.copytree(srcPath, destPATH)
else:
    for f in [x for x in withHeaderPath.iterdir() if x.is_file]:
        shutil.copy(str(f), destPATH)

for csvFilename in withoutHeaderPath.iterdir():
    if not csvFilename.name.endswith('.csv'):
        continue
    
    print('Removing header from ' + str(csvFilename) + '...')
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(csvFilename, 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()