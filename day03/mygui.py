#!/usr/bin/env python3

import tkinter
from functools import partial

root = tkinter.Tk()    #创建顶层窗口
lb1 = tkinter.Label(root, text="hello world!", font = "Aria 16 bold")#创建标签
b1 = tkinter.Button(root, bg='blue', fg='white', text="Button 1")#创建按钮
mybutton = partial(tkinter.Button, root, bg='blue', fg='white')
#调用新的函数时，给出改变的参数即可
b2 = mybutton(text='Button 2')
b3 = tkinter.Button(root, bg='red', fg='red', text='QUIT', command=root.quit)    #创建按钮，绑定了root.quit命令
lb1.pack()    #填充到界面
b1.pack()
b2.pack()
b3.pack()
root.mainloop()    #运行这个GUI应用