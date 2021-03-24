# importing matplotlib
import matplotlib.animation as animation
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib

import pandas as pd
import numpy as np
import urllib

matplotlib.use('TkAgg')

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)  # 1x1 plot no 1


def animate(i):
    pullData = open('sample.csv', 'r').read()
    dataList = pullData.split('\n')
    xl = []
    yl = []
    for line in dataList:
        if len(line) > 1:
            x, y = line.split(',')
            xl.append(float(x))
            yl.append(float(y))

    a.clear()
    a.plot(xl, yl)

# for later session


def animateWithApi(link):
    data = urllib.request.urlopen(link)
    data = data.readall().decode('utf-8')
    data = json.loads(data)
    data = data['keyname']

    data = pd.dataFrame(data)

    buys = data[(data['type'] == 'ask')]
    buys['datestamp'] = np.array(buys['timestamp'].astype('datetime64[s]'))
    buyDates = (buys['datestamp']).tolist()

    sells = data[(data['type'] == 'sell')]

    a.clear()
    a.plot_date(buyDates, buys['price'])
    a.plot_date(buyDates, sells['price'])


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # windows setting
        self.title('BelifeSat Power')
        self.geometry('700x500')
        # self.iconphoto(False, tk.PhotoImage(file='icon.png'))

        # added container
        container = tk.Frame(self)
        container.pack(side='top', expand=True)

        # adding frames
        self.frames = {}

        for F in (StartPage, Dashbaord, PowerPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text='welcome to basestation GUI Tool')
        label1.pack()

        btn1 = ttk.Button(self, text='dashbaord',
                          command=lambda: controller.show_frame(Dashbaord))
        btn1.pack()

        btn2 = ttk.Button(self, text='Power System',
                          command=lambda: controller.show_frame(PowerPage))
        btn2.pack()

        btn3 = ttk.Button(self, text='telemetry')
        btn3.pack()


class Dashbaord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text='ok , graph')
        label1.pack(side='top')

        btn1 = ttk.Button(self, text='<- back',
                          command=lambda: controller.show_frame(StartPage))
        btn1.pack(side='top')


class PowerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text='hi , Its Power Page')
        label1.pack()

        btn1 = ttk.Button(self, text='<- back',
                          command=lambda: controller.show_frame(StartPage))
        btn1.pack()

        # first calculate , then display graph

        # f = Figure(figsize=(5, 4), dpi=100)
        # a = f.add_subplot(111)  # 1x1 plot no 1
        # a.plot([1, 2, 3, 4], [82, 34, 11, 90])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()


window = Gui()
ani = animation.FuncAnimation(f, animate, 2000)
window.mainloop()
