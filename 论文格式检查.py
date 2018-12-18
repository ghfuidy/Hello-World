from docx import Document
from docx.shared import RGBColor


word = Document(r'D:\学习资料\毕业设计\毕设资料\镁合金表面的仿生沉积1.docx')
for paragraph in word.paragraphs:
    i = 0
    for run in paragraph.runs:
        print(run.style.name)
#         if run.font.name == u'宋体':
#             run.font.color.rgb = RGBColor(0, 255, 0) #绿色
#         elif run.font.name == u'Times New Roman':
#             run.font.color.rgb = RGBColor(0,0,255) #蓝色

# word.save(r"D:\学习资料\书籍PDF文件\镁合金表面的仿生沉积_核.docx")