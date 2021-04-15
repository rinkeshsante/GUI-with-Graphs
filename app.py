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

from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# current graph
fig = Figure(figsize=(8, 4))

plt1 = fig.add_subplot(111)
# plt2 = fig.add_subplot(212)


def animate(i):
    # add csv path
    data = pd.read_csv('sample.csv')

    # print('refresed')
    # print(data)

    # data = pd.DataFrame(data)
    data = np.array(data)
    # print(data.power.tolist())

    t = []
    i = []
    p = []
    v = []
    e = []

    for row in data:
        print(row)

        t.append(row[0])
        v.append(row[1])
        i.append(row[2])
        p.append(row[3])
        e.append(row[4])

    # time = data[(data['type'] == "timestamp")]
    # power = data[(data['type'] == "power")]

    # print('---', t, p)

    plt1.clear()
    # plt1.plot(data)
    # df[['Open','High','Low','Close','100MA']].plot()

    plt1.plot(t, p, 'g', label='power')
    plt1.plot(t, i, 'y', label='current')
    plt1.plot(t, v, 'm', label='voltage')
    plt1.plot(t, e, 'c', label='efficiency')
    # plt1.plot()
    plt1.legend()

    plt1.set_title('i vs p')

    # plt2.clear()
    # plt2.plot(data)


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # windows setting
        self.title('BelifeSat Power')
        self.geometry('1200x600')
        # self.iconphoto(False, tk.PhotoImage(file='icon.png'))

        # added container
        container = tk.Frame(self)
        container.pack(side='top', expand=True)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='save settings',
                             command=lambda: popupmsg('not supported yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='file', menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        # adding frames
        self.frames = {}

        for F in (StartPage, Dashbaord, CurrentGraph, ):
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

        # btn2 = ttk.Button(self, text='Power System',
        #                   command=lambda: controller.show_frame(PowerPage))
        # btn2.pack()

        btn3 = ttk.Button(self, text='telemetry')
        btn3.pack()

        btn4 = ttk.Button(self, text='currrent System',
                          command=lambda: controller.show_frame(CurrentGraph))
        btn4.pack()

        btn5 = ttk.Button(self, text='volatge System',
                          command=lambda: controller.show_frame(VoltageGraph))
        btn5.pack()


class Dashbaord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text='ok , graph')
        label1.pack(side='top')

        btn1 = ttk.Button(self, text='<- back',
                          command=lambda: controller.show_frame(StartPage))
        btn1.pack(side='top')


class CurrentGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text='Current vs time')
        label1.pack()

        btn1 = ttk.Button(self, text='<- back',
                          command=lambda: controller.show_frame(StartPage))
        btn1.pack()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()


window = Gui()
ani = animation.FuncAnimation(fig, animate, 5000)

window.mainloop()


# colors
# 'r' 	Red
# 'g' 	Green
# 'b' 	Blue
# 'c' 	Cyan
# 'm' 	Magenta
# 'y' 	Yellow
# 'k' 	Black
# 'w' 	White

# line
# '-' 	Solid line
# ':' 	Dotted line
# '--' 	Dashed line
# '-.' 	Dashed/dotted line
