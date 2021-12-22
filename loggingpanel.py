import tkinter as tk
from tkinter.constants import *
from pandas.core.frame import DataFrame
from Frames import panels
from doubleScroll import DoubleScrolledFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LoggingPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.render()
        self.__config()
    
    def setGdata(self, gdata):
        self.gdata = gdata
    
    def lhide(self):
        self.pack_forget()
    
    def lshow(self):
        self.pack(side=RIGHT, fill=Y, padx=10 ,anchor=NE, expand=0)

    def gshow(self):
        self.g.render()

    def ghide(self):
        self.g.destroy()

    def __config(self):
        self["bg"] = "#EFEEEE"
        self["borderwidth"] = 3
        self["relief"] = "groove"
    
    def addLogg(self, name=""):
        self.loggs = tk.Frame(self.sf)
        self.loggs.pack(side=TOP, anchor=NW)
        tk.Label(self.loggs, text=name,justify=LEFT ,anchor="e",font=("Roboto 18")).pack(side=TOP, anchor=NW, padx=10)

    class Graphp(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self.config( width=600, height=399, relief=RIDGE, borderwidth=2)
        
        def show(self):
            self.pack(side=BOTTOM, fill=BOTH, padx=10)
        def hide(self):
            self.pack_forget()

        def render(self, data=DataFrame):
            figure1 = plt.Figure(figsize=(6,5), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, self)
            bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            data.plot(kind='bar', legend=True, ax=ax1)
            ax1.set_title('Prodcts vs distance')
    
    def render(self):

        self.sf = DoubleScrolledFrame(self)

        self.sf.pack(side=TOP, fill=BOTH, expand=1)
        
        panels["loggs"] = self
