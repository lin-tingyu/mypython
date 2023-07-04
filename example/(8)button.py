import tkinter as tk
#import pyinstaller#(pip install pyinstaller)

#https://johnsonnnn.medium.com/python-tkinter-gui-%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95-4e1be246ea2f

def _hit1():
    tk.messagebox.showinfo('提示','1')
def _hit2():
    tk.messagebox.showwarning('警告','2')
def _hit3():
    tk.messagebox.showerror('錯誤','3')
def _hit4():
    qQ =tk.messagebox.askokcancel('關閉','4')
    if qQ:
        window.destroy()

def check():
    #提取目前 var 內容
    print(var.get())

def hello():
    print('hello')
    
window = tk.Tk()
window.title('GUI')
window.geometry('380x400')
window.resizable(False, False)

test = tk.Button(text="測試", command=_hit1)
test.pack(side="top")
test2 = tk.Button(text="測試2", command=_hit2)
test2.pack(side="top")
test3 = tk.Button(text="測試3", command=_hit3)
test3.pack(side="left")
test4 = tk.Button(text="測試4", command=_hit4)
test4.pack(side="left")

#設定變數 Int 型別儲存目前內容
var = tk.IntVar()
#儲存的資料位置為 var
#勾選時值設為1 未勾選則設為0 每次按下皆顯示目前狀態
tk.Checkbutton(window, variable=var, text='Check', onvalue=1, offvalue=0, command=check).pack()



#創建菜單框架
menu = tk.Menu(window)
#tearoff=False 關閉菜單裡的虛線欄
filemenu = tk.Menu(menu, tearoff=False)
#將 filemenu 放入 menu 菜單
menu.add_cascade(menu=filemenu, label='File')
#增加菜單選項
filemenu.add_command(label='Hello', command=hello)
#增加分隔線
filemenu.add_separator()
#增加菜單選項
filemenu.add_command(label='Exit', command=window.quit)
#將 menu 菜單放入 root
window.config(menu=menu)


window.mainloop()