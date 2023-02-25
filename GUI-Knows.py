from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import info
import study
from money import *
from study import subject
GUI = Tk ()
GUI.title('ทำไรก็ทำไป')
GUI.geometry ('500x400')

def Button1():
    
    text = 'วิชาที่กำลังเรียน' ,(subject) 
    messagebox.showinfo('วิชาที่กำลังเรียน',subject)
    
FB1 = LabelFrame(GUI,text='studys')
FB1.place(x=40,y=150)
B1 = ttk.Button (FB1,text='วิชาที่เรียนอยู่',command=Button1)
B1.pack(ipadx=20,ipady=20,padx=30,pady=30)

#######################
def Button2():
    text = 'สถานะการเงินในขณะนี้มี' , (my_account) ,'บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    
FB2 = LabelFrame(GUI,text='Money')
FB2.place(x=250,y=150)
B2 = ttk.Button (FB2,text='เงินที่เหลือ',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)

GUI.mainloop()
