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
fI = Figure()
aI = fI.add_subplot(111)  # 1x1 plot no 1

# voltage graph
# fV = Figure(figsize=(5, 4), dpi=100)
# aV = fV.add_subplot(111)  # 1x1 plot no 1

# # power graph
# fP = Figure(figsize=(5, 4), dpi=100)
# aP = fP.add_subplot(111)  # 1x1 plot no 1

# # effeicinecy graph
# fE = Figure(figsize=(5, 4), dpi=100)
# aE = fE.add_subplot(111)  # 1x1 plot no 1


def animate(i):
    pullData = open('sample.csv', 'r').read()
    dataList = pullData.split('\n')

    tl = []
    il = []
    vl = []
    pl = []
    el = []

    for line in dataList:
        if len(line) > 1:
            # print(line)
            t, i, v, p, e = line.split(',')
            tl.append(float(t))
            il.append(float(i))
            vl.append(float(v))
            pl.append(float(p))
            el.append(float(e))

    # print(tl, il, vl, pl, el)
    print('refresded')

    aI.clear()
    aI.plot(tl, il)

    # aV.clear()
    # aV.plot(tl, vl)

    # ap.clear()
    # ap.plot(tl, pl)

    # aE.clear()
    # aE.plot(tl, el)

# for later session


# def animateWithApi(link):
#     data = urllib.request.urlopen(link)
#     data = data.readall().decode('utf-8')
#     data = json.loads(data)
#     data = data['keyname']

#     data = pd.dataFrame(data)

#     buys = data[(data['type'] == 'ask')]
#     buys['datestamp'] = np.array(buys['timestamp'].astype('datetime64[s]'))
#     buyDates = (buys['datestamp']).tolist()

#     sells = data[(data['type'] == 'sell')]

#     a.clear()
#     a.plot_date(buyDates, buys['price'])
#     a.plot_date(buyDates, sells['price'])


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # windows setting
        self.title('BelifeSat Power')
        self.geometry('700x600')
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


# class PowerPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         label1 = ttk.Label(self, text='hi , Its Power Page')
#         label1.pack()

#         btn1 = ttk.Button(self, text='<- back',
#                           command=lambda: controller.show_frame(StartPage))
#         btn1.pack()

#         # first calculate , then display graph

#         # f = Figure(figsize=(5, 4), dpi=100)
#         # a = f.add_subplot(111)  # 1x1 plot no 1
#         # a.plot([1, 2, 3, 4], [82, 34, 11, 90])

#         canvas = FigureCanvasTkAgg(fI, self)
#         canvas.draw()
#         canvas.get_tk_widget().pack()

#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack()


class CurrentGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text='Current vs time')
        label1.pack()

        btn1 = ttk.Button(self, text='<- back',
                          command=lambda: controller.show_frame(StartPage))
        btn1.pack()

        canvas = FigureCanvasTkAgg(fI, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()


# class VoltageGraph(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         label1 = ttk.Label(self, text='Voltage')
#         label1.pack()

#         btn1 = ttk.Button(self, text='<- back',
#                           command=lambda: controller.show_frame(StartPage))
#         btn1.pack()

#         canvas = FigureCanvasTkAgg(fV, self)
#         canvas.draw()
#         canvas.get_tk_widget().pack()

#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack()


window = Gui()
ani = animation.FuncAnimation(fI, animate, 2000)
# ani1 = animation.FuncAnimation(fV, animate, 2000)
# ani = animation.FuncAnimation(fI, animate, 2000)
# ani = animation.FuncAnimation(fI, animate, 2000)
window.mainloop()
