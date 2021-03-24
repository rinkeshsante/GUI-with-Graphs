from tkinter import ttk
import tkinter as tk

from ..app import gui
from .PowerPage import PowerPage
from .Dashboard import dashbaord


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
