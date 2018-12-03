from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import StringVar, IntVar
import json

class Application(Frame):
    root = Tk()
    searchmessage = StringVar()
    searchmessage.set('搜索结果是：')

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        with open(r"D:\学习资料\书籍PDF文件\word_list.json", 'rb') as json_file:
            self.json_file = json_file
            self.jsondata = json.load(json_file)

    def createWidgets(self):
        self.keyInput = Entry(self)
        self.keyInput.pack()
        self.valueInput = Entry(self)
        self.valueInput.pack()
        self.alertButton = Button(self, text='add', command=self.hello)
        self.alertButton.pack()
        self.search = Entry(self)
        self.search.pack()
        self.seaechButton = Button(self, text='search', command=self.searchcss)
        self.seaechButton.pack()
        self.show_searchmessage = Label(self, textvariable=Application.searchmessage)
        self.show_searchmessage.pack()

    def hello(self):
        key = self.keyInput.get()
        keyvalue = self.valueInput.get()
        

        if key != '' and keyvalue != '':
            self.jsondata[key] = keyvalue
            with open(r"D:\学习资料\书籍PDF文件\word_list.json", 'w', encoding='utf-8') as json_file:
                json.dump(self.jsondata, json_file)
            messagebox.showinfo('提示', '输入成功\n' + key + '的值是:' + keyvalue)
        else:
            messagebox.showerror('错误', '请输入正确的值')

    def searchcss(self):
        search_value = self.search.get()
        Application.searchmessage.set(self.jsondata[search_value])


app = Application()
# 设置窗口标题:
app.master.title('add Json')
app.master.geometry('400x200')#窗体大小
# app.root.protocol("WM_DELETE_WINDOW", app.callback())
# 主消息循环:
app.mainloop()