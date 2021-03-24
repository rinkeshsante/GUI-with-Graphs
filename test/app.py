
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

# plot function is created for
# plotting the graph in
# tkinter window


def plot(x, y, xName='', yName='', gTitle=''):

    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(x, y)

    # fig.xlabel(xName)
    # fig.ylabel(yName)
    # fig.title(gTitle)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(
        row=2, column=2, padx=10, pady=10, columnspan=10,)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(
        row=2, column=2, padx=10, pady=10, columnspan=10)


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("800x600")


def plot1():
    plot([1, 2, 3, 4, 5], [1, 4, 9, 6, 100], 'time', 'current', 'I vs T')


def plot2():
    plot([1, 2, 3, 4, 5], [0, 4, 9, 6, 100])


def plot3():
    plot([1, 2, 3, 4, 5], [1, 4, 9, 6, 100])


def plot4():
    plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 6, 100, 90])


# button that displays the plot
plot_button = Button(master=window,
                     command=plot1,
                     height=2,
                     width=10,
                     text="I vs T")
plot_button.grid(
    row=0, column=0, padx=10, pady=10)

plot_button2 = Button(master=window,
                      command=plot2,
                      height=2,
                      width=10,
                      text="V vs T")
plot_button2.grid(
    row=0, column=1, padx=10, pady=10)

plot_button2 = Button(master=window,
                      command=plot3,
                      height=2,
                      width=10,
                      text="P vs T")
plot_button2.grid(
    row=0, column=2, padx=10, pady=10)

plot_button2 = Button(master=window,
                      command=plot4,
                      height=2,
                      width=10,
                      text="e vs T")
plot_button2.grid(
    row=0, column=3, padx=10, pady=10)

plot_button2 = Button(master=window,
                      height=2,
                      width=10,
                      text="Save to DB")
plot_button2.grid(
    row=0, column=4, padx=10, pady=10)


plot_button2 = Text(master=window,
                    height=27,
                    width=20,
                    )
plot_button2.grid(
    row=2, column=0, padx=10, pady=10, columnspan=2)

# run the gui
window.mainloop()
