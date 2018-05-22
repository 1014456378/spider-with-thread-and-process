import tkinter as tk

import patupian


def hit_me():
    guanjianzi = shuru1.get()
    cunchulujing = shuru2.get()
    fenbianlv = shuru3.get()
    shuliang = int(shuru4.get())
    patupian.firs(guanjianzi, cunchulujing, fenbianlv,shuliang)
emmm = tk.Tk()
emmm.title("爬图片")
emmm.geometry("500x500")
vv1 = tk.StringVar()
vv2 = tk.StringVar()
vv3 = tk.StringVar()
vv4 = tk.StringVar()
Label1 = tk.Label(emmm, text='图片爬取', bg='yellow', font=('Arial', 25), width=26, heigh=2)
Label1.pack()
Label1.place(x=0, y=0)
Label2 = tk.Label(emmm, text='须用英文', bg='yellow', font=('Arial', 10), width=16, heigh=1)
Label2.pack()
Label2.place(x=360, y=100)
Label3 = tk.Label(emmm, text='我的电脑直接复制路径', bg='yellow', font=('Arial', 10), width=16, heigh=1)
Label3.pack()
Label3.place(x=360, y=150)
Label4 = tk.Label(emmm, text='例：1920x1080', bg='yellow', font=('Arial', 10), width=16, heigh=1)
Label4.pack()
Label4.place(x=360, y=200)
Label5 = tk.Label(emmm, text='*24张', bg='yellow', font=('Arial', 10), width=16, heigh=1)
Label5.pack()
Label5.place(x=360, y=250)
shuru1 = tk.Entry(emmm, width=30)
shuru1.pack()
shuru1.place(x=140, y=100)
shuru2 = tk.Entry(emmm,width=30)
shuru2.pack()
shuru2.place(x=140, y=150)
shuru3 = tk.Entry(emmm, width=30)
shuru3.pack()
shuru3.place(x=140, y=200)
shuru4 = tk.Entry(emmm, width=30)
shuru4.pack()
shuru4.place(x=140, y=250)


button1 = tk.Button(emmm, text='点我开始', font=('Arial', 15), bg='green', width=10, heigh=1,
                    command= hit_me)
button1.pack(pady=100)
button1.place(x=187, y=350)


Label11 = tk.Label(emmm, text='关键词', bg='yellow', font=('Arial', 10), width=7, heigh=1)
Label11.pack()
Label11.place(x=50, y=100)
Label12 = tk.Label(emmm, text='存储路径', bg='yellow', font=('Arial', 10), width=7, heigh=1)
Label12.pack()
Label12.place(x=50, y=150)
Label13 = tk.Label(emmm, text='分辨率', bg='yellow', font=('Arial', 10), width=7, heigh=1)
Label13.pack()
Label13.place(x=50, y=200)
Label14 = tk.Label(emmm, text='图片数', bg='yellow', font=('Arial', 10), width=7, heigh=1)
Label14.pack()
Label14.place(x=50, y=250)

emmm.mainloop()





