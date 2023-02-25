from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('Record Work hours') #นี่คือชื่อโปรแกรม
GUI.geometry('600x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='Record Work hours',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

##########WorkIN##########
LF1 = ttk.LabelFrame(GUI,text='เวลาเข้างาน')
LF1.place(x=50,y=100)

v_data1 = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data1,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

def SaveData1():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data1.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data1.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    

B4 = ttk.Button(LF1,text='IN',command=SaveData1)
B4.pack(ipadx=20,ipady=20)

##########WorkOUT##############
LF2 = ttk.LabelFrame(GUI,text='เวลาออกงาน')
LF2.place(x=300,y=100)

v_data2 = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E2 = ttk.Entry(LF2,textvariable=v_data2,font=('Angsana New',25))
E2.pack(pady=10,padx=10)

from datetime import datetime

def SaveData2():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data2.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,' ',data] # [เวลา, ,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data2.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B5 = ttk.Button(LF2,text='OUT',command=SaveData2)
B5.pack(ipadx=20,ipady=20)


GUI.mainloop()
