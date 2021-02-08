from tkinter import *
import parser
import tkinter as tk


def m_to_km():
    m = input.get()
    try:
        m = float(m)
        print(m)
        km = m/1000
        result_lbl["text"] = (round(km,4) , "km(s)")
    except ValueError:
        #print("Error")
        result_lbl["text"] = "NUMBERS ONLY"



def m_to_cm():
    m = float(input.get())
    cm = m*100
    result_lbl["text"] = round(cm,4) , "cm(s)"

def m_to_mm():
    m = float(input.get())
    mm = m*1000
    result_lbl["text"] = round(mm,4) , "mm(s)"

def m_to_mile():
    m = float(input.get())
    mile = m*0.00062137
    result_lbl["text"] = round(mile,8) , "mile(s)"

def m_to_inch():
    m = float(input.get())
    inch = m * 39.370
    print(inch)
    result_lbl["text"] = round(inch,4) , "inch(es)"


root = tk.Tk()
root.title("Metric Unit Converter")
root.geometry("400x70")
root.resizable(False, False)

input_frame = tk.Frame(master=root)
input_frame.grid()

from_lbl = tk.Label(master=input_frame, text="FROM")
from_lbl.grid(row=0, sticky=W)
input = tk.Entry(master=input_frame)
input.grid(row=1, column=0, columnspan=2)
input_lbl = tk.Label(master=input_frame, text="meter(s)")
input_lbl.grid(row=1, column=3)

to_lbl = tk.Label(master=input_frame, text="TO")
to_lbl.grid(row=0, column=6)
result_lbl = tk.Label(master=input_frame, text="result", width=20)
result_lbl.grid(row=1, column=5, columnspan=5, sticky=E)

firstrow = tk.Frame(master=root)
firstrow.grid()


km_btn = tk.Button(master=firstrow, text="Kilometer", width=10, command=m_to_km)
km_btn.grid()
cm_btn = tk.Button(master=firstrow, text="Centimeter", width=10, command=m_to_cm)
cm_btn.grid(row=0,column=1)
mm_btn = tk.Button(master=firstrow, text="Millimeter", width=10, command=m_to_mm)
mm_btn.grid(row=0,column=2)
mile_btn = tk.Button(master=firstrow, text="Mile", width=10, command=m_to_mile)
mile_btn.grid(row=0,column=3)
inch_btn = tk.Button(master=firstrow, text="Inch", width=10, command=m_to_inch)
inch_btn.grid(row=0,column=4)

root.mainloop()
