import tkinter as tk
import pyautogui as pg
import pyperclip#用于复制操作
from pynput.mouse import Listener#导入监听
x=tk.Tk()
x.geometry('400x200+800+300')
x.title('鼠标坐标获取')
x.resizable(False,False)
x.attributes('-topmost',1)
x1=tk.IntVar()
x2=tk.IntVar()
tk.Label(x,font=('黑体',30),text='X:').place(x=0,y=100)
tk.Label(x,font=('黑体',30),text='Y:').place(x=210,y=100)
tk.Label(x,font=('黑体',20),text='单击鼠标左键以复制坐标').place(x=10,y=30)
def update():
    a,b=pg.position()
    x1.set(a)
    x2.set(b)
    x.after(50,update)#内循环自动更新操作,可以实时间隔n毫秒重复执行
tk.Entry(x,font=('黑体',30),textvariable=x1,width=5).place(x=50,y=100)
tk.Entry(x,font=('黑体',30),textvariable=x2,width=5).place(x=260,y=100)
update()#外循环启动一次以不断执行
def d(k, l,button,pressed):
        if pressed:
            o= f'({k},{l})'
            pyperclip.copy(o)
            x1.set(k)
            x2.set(l)
listener = Listener(on_click=d)#用全局监听事件代替一直监视的thread,提高了运行效率
listener.start()
x.mainloop()