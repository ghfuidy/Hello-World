import PyPDF2

# #多个PDf文件合并成一个
# filenames = ['one.pdf','two.pdf']

# merger = PyPDF2.PdfFileMerger()
# for filename in filenames:
#     merger.append(PyPDF2.PdfFileReader(filename))
# merger.write('Python这门课.pdf')

# #增加文件水印
# with open('Python这门课.pdf', 'rb') as pdfFile:
#     pdfReader =PyPDF2.PdfFileReader(pdfFile)
#     minutesFirstPage = pdfReader.getPage(0)

#     with open('watermark.pdf','rb') as markFile:
#         pdfWatermarkReader = PyPDF2.PdfFileReader(markFile)
#         minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

#         pdfWirter =PyPDF2.PdfFileWriter()
#         pdfWirter.addPage(minutesFirstPage)
        
#         for pageNum in range(1,pdfReader.numPages):
#             pageobj = pdfReader.getPage(pageNum)
#             pdfWirter.addPage(pageobj)

#         with open('watermarkMinutes.pdf', 'wb') as resultPdfFile:
#             pdfWirter.write(resultPdfFile)

# #the second ways to merge two files
# #可省略前面的   PyPDF2.
# from PyPDF2 import PdfFileReader, PdfFileWriter
# # 文件的打开方法变为open
# pdfFile = open('Python这门课.pdf', 'rb')

#读取加密文件
with open('17material.pdf', 'rb') as pdfFileobj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileobj)

if pdfReader.isEncrypted:
    if pdfReader.decrypt('jiaoyanshi151'):
        pageobj = pdfReader.getPage(1)
        print(pageobj.extractText())
    else:
        print('Wrong password')
else:
    pageobj = pdfReader.getPage(0)
    print(pageobj.extractText())

# #加密文件
# with open('test_car.pdf', 'rb') as pdfFile:
#     pdfReader = PyPDF2.PdfFileReader(pdfFile)
#     pdfWriter = PyPDF2.PdfFileWriter()

#     for pageNum in range(pdfReader.numPages):
#         pdfWriter.addPage(pdfReader.getPage(pageNum))
    
#     pdfWriter.encrypt('python')
    
#     with open('encryptedDream.pdf', 'wb') as resultPdf:
#         pdfWriter.write(resultPdf)