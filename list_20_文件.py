
# # # # heine = open(r'C:\python_example\helloworld_python\heine.txt')
# # # # # heine = open('C:\\python_example\\helloworld_python\\heine.txt')
# # # # poem = heine.read()
# # # # print(poem)
# # # # # print(heine.closed)
# # # # heine.close()
# # # # # print(heine.closed)

# # # # # with open(r'C:\python_example\helloworld_python\heine.txt', mode = 'a') as heine:
# # # # #     heine.write('\nFrom Heine\n')

# # # # # with open(r'C:\python_example\helloworld_python\heine.txt', mode = 'r') as heine:
# # # # #     print(heine.read())

# # # # with open(r'C:\python_example\helloworld_python\heine.txt', mode = 'r+') as heine:
# # # #     print(heine.tell())
# # # #     heine.write('\nterrible\n')
# # # #     print(heine.tell())
# # # #     print(heine.read())
# # # #     heine.seek(0)
# # # #     print(heine.read())

# # # with open(r'C:\python_example\helloworld_python\heine.txt', mode = 'w') as heine:
# # #     heine.write('''123456789
# # #         182kudhakh
# # #         sadhalksjdllla
# # #     ''')

# # # with open(r'C:\python_example\helloworld_python\heine.txt') as h:
# # #     # print(h.read(100))
# # #     # print(h.readline(),end = '')
# # #     # for line in h:
# # #     #     print(line, end = '')
# # #     size_to_read = 10
# # #     f_content = h.read(size_to_read)
# # #     while len(f_content) > 0:
# # #         print(f_content, end = '')
# # #         f_content = h.read(size_to_read)
# # # #读过的会自动排除，然后递进？

# # with open(r'C:\python_example\helloworld_python\test.txt','w',encoding = 'utf-8') as f:
# #     f.write('''滚滚长江东逝水
# #     浪花淘尽英雄
# #     是非成败转头空
# #     青山依旧在
# #     几度夕阳红
# #     ''')

# # with open(r'C:\python_example\helloworld_python\test.txt','r',encoding = 'utf-8') as f:
# #     s = f.read()
# #     print(s)


# with open(r'C:\python_example\helloworld_python\meili.jpg','rb') as rf:
#     with open (r'C:\python_example\helloworld_python\meili_copy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
# #音频操作同样

# import shelve
# shelfFile = shelve.open('myCat')
# cats = ['garfiled', 'Tom', 'Kitty']
# shelfFile['cats'] = cats

# shelfFile.close()

# sh = shelve.open('myCat')
# print(sh['cats'])
# print(sh.keys())
# print(list(sh.keys()))
# print(sh.values)
# print(list(sh.values()))

# import pprint
# cats = [{'name':'garfiled','desc':'chubby'},{'name':'Tom','desc':'naughty'}]

# s = pprint.pformat(cats)
# print(type(s))

# with open('myCats.py','w') as fileobj:
#     fileobj.write('cats = ' + s + '\n')

# #使用保存的文件,需要将myCats文件加到解释器
# import myCats
# print(myCats.cats)

# print(myCats.cats[0])

with open('123.txt','w') as m:
    m.write('my favourite girls are...')

f = open('123.txt')
print(f.read())
# 直接使用open的路径如上所示，文件位于C:\python_example中