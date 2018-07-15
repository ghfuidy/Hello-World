import PyPDF2

# #多个PDf文件合并成一个
# filenames = ['one.pdf','two.pdf']

# merger = PyPDF2.PdfFileMerger()
# for filename in filenames:
#     merger.append(PyPDF2.PdfFileReader(filename))
# merger.write('Python这门课.pdf')

#增加文件水印
with open('Python这门课.pdf', 'rb') as pdfFile:
    pdfReader =PyPDF2.PdfFileReader(pdfFile)
    minutesFirstPage = pdfReader.getPage(0)

    with open('watermark.pdf','rb') as markFile:
        pdfWatermarkReader = PyPDF2.PdfFileReader(markFile)
        minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

        pdfWirter =PyPDF2.PdfFileWriter()
        pdfWirter.addPage(minutesFirstPage)
        
        for pageNum in range(1,pdfReader.numPages):
            pageobj = pdfReader.getPage(pageNum)
            pdfWirter.addPage(pageobj)

        with open('watermarkMinutes.pdf', 'wb') as resultPdfFile:
            pdfWirter.write(resultPdfFile)