import calenday
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Listbox
calendar.setfirstweekday(6)
def 一():
    leap=leapy.get()
    if not jc(leap):
        if calendar.isleap(leap):
            lb1.insert(str(leap) + "是闰年！")
        else:
            lb1.insert(str(leap) + "不是闰年！")
    else:
        messagebox.showerror("ERROR","请输入整数！")
def 二():
    leap1=leapy1.get()
    leap2=leapy2.get()
    if not jc(leap1) or jc(leap2):
        d_a=calendar.leapdays(int(leap1),int(leap2))
        lb2.insert(str(leap1) + "至" + str(leap2) + "年间共有" + d_a + "个闰年！")
    else:
        messagebox.showerror("ERROR","请输入整数！")
def 三():
    month1=monthy1.get()
    month2=monthy2.get()
    if not jc(month1) or jc(month2):
        ls=list(calendar.monthrange(int(month1),int(month2)))
        dy=["周一","周二","周三","周四","周五","周六","周日"]
        ls[1]=dy[int(ls[1])]
        lb3.insert(str(month1) + "年" + str(month2) + "月起于" + ls[1] + "，共" + ls[2] + "天")
    else:
        messagebox.showerror("ERROR","请输入整数！")
def 四():
    month1=monthy3.get()
    month2=monthy4.get()
    if not jc(month1) or jc(month2):
        if month2 != "-":
            print(calendar.month(int(month1),int(month2))
        else:
            print(calendar.calendar(int(month1))
    else:
        messagebox.showerror("ERROR","请输入整数！")
def jc(a):
    try:
        int(a)
    except ValueError:
        return True
    else:
        return False
root=tk.Tk()
root.title("年份测试器")
tkk.Label(root,text="请在使用本程序的同时搭配Python IDLE共同食用（使用）").grid(column=0,row=1)
ttk.Label(root,text="年份").grid(column=1,row=0)
ttk.Label(root,text="判断结果").grid(column=1,row=2)

