from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from numpy import arange, sin, pi
from tkinter import *


import matplotlib
matplotlib.use('TkAgg')

# implement the default mpl key bindings


class gui(Tk):
    def __init__(self):
        super().__init__()
        # self.geometry('300x150')
        self.title('Repo Manager')

        # buttons
        Button(text='I vs T', command=self.currentGraph).grid(
            row=2, column=0, padx=10, pady=10)
        Button(text='V vs T', command=self.updateVal).grid(
            row=2, column=1, padx=10, pady=10)
        Button(text='P vs T', command=self.deleteVal).grid(
            row=2, column=2, padx=10, pady=10)
        Button(text='eficiency Vs T', command=self.save).grid(
            row=2, column=3, padx=10, pady=10)
        Button(text='refresh', command=self.save).grid(
            row=2, column=3, padx=10, pady=10)

        self.commonGraph()

    # self.addItem()

    def commonGraph(self):

        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)

        a.plot(t, s)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, root)
        toolbar.update()
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def currentGraph(self):
        self.graph = None


gui().mainloop()
