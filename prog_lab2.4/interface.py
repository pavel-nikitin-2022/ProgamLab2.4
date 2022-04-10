from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import ttk
from tkinter import *
import tkinter as tk
from data import trade_game

k = conv = cmb = cmb1 = cmb2 = date_start = date_end = None

#построение графика
def generate(data):
    global conv
    if conv:
        conv.get_tk_widget().destroy()
    sm, fn = data
    figure2 = plt.Figure(figsize=(16, 9), dpi=100)
    ax2 = figure2.add_subplot(111)
    conv = FigureCanvasTkAgg(figure2)
    conv.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax2.plot(sm)
    ax2.plot(fn)
    ax2.set_title(cmb.get())
    return conv

#события при нажатие на кнопку build
def build():
    smooth = None
    recover = None
    ticker = cmb.get()
    start = date_start.get()
    end = date_end.get()
    koef = k.get()
    if cmb1.get() == "Винзорирование":
        recover = "vinz"
    elif cmb1.get() == "Линейная аппроксимация":
        recover = "linear"
    elif cmb1.get() == "Корреляционное восстановление":
        recover = "linear"
    if cmb2.get() == "Взвешенный метод скользящего среднего":
        smooth = "static"
    elif cmb2.get() == "метод скользящего среднего со скользящим окном наблюдения":
        smooth = "dinamyc"
    data = trade_game(recover, smooth, start, end, ticker, float(koef))
    generate(data)

#верстка основного экрана
def main_screen():
    global cmb
    global cmb1
    global cmb2
    global date_start
    global date_end
    global k
    tickers = ["YNDX", "GAZP", "TATN", "SBER", "VTBR", "ALRS", "AFLT", "HYDR"]
    recovery = ["Винзорирование", "Линейная аппроксимация",
               "Корреляционное восстановление"]
    smoothing = ["Взвешенный метод скользящего среднего",
                "метод скользящего среднего со скользящим окном наблюдения"]
    window = Tk()
    window.geometry("800x600")
    window.title("Аналитика акций")

    str1 = Frame(window)
    str2 = Frame(window)
    str3 = Frame(window)
    str4 = Frame(window)
    str5 = Frame(window)
    str6 = Frame(window)
    str7 = Frame(window)

    str1.pack()
    str2.pack()
    str3.pack()
    str4.pack()
    str5.pack()
    str6.pack()
    str7.pack()

    Label(str1, text="Введите тикер ", padx=5, pady=5).pack(side=LEFT)
    Label(str2, text="Введите временной отрезок ", padx=5, pady=5).pack(side=LEFT)
    Label(str4, text="Выберите способ восстановления ", padx=5, pady=5).pack(side=LEFT)
    Label(str5, text="Выберите способ сглаживания ", padx=5, pady=5).pack(side=LEFT)
    Label(str6, text="Выберите коэф сглаживания или размер окна ", padx=5, pady=5).pack(side=LEFT)

    cmb = ttk.Combobox(str1, values=tickers , state="readonly")
    cmb1 = ttk.Combobox(str4, values=recovery, state="readonly")
    cmb2 = ttk.Combobox(str5, values=smoothing, state="readonly")

    cmb.pack(side=LEFT)
    cmb1.pack(side=LEFT)
    cmb2.pack(side=LEFT)

    Button(str7, text="Построить график", command=build, padx=5, pady=5).pack(side=LEFT)
    Button(str7, text="Очистить", command=close, padx=5, pady=5).pack(side=LEFT)

    date_start = Entry(str2, width=15)
    date_end = Entry(str2, width=15)
    k = Entry(str6, width=15)
    k.pack(side=LEFT)
    date_start.pack(side=LEFT)
    date_end.pack(side=LEFT)   

    window.mainloop()

#чистильщик
def close():
    global conv
    if conv: conv.get_tk_widget().destroy()
        
