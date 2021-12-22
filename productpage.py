import tkinter as tk
from tkinter.constants import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import time
from plot import plotG
from Frames import panels

from PIL import Image, ImageTk

class ProductPage(tk.Frame):
    def __init__(self, master=None, name=str, price=0, desc="", ratiing=int):
        super().__init__(master=master)
        self.__mem = []
        self.name = name
        self.price = price
        self.rating = ratiing
        self.desc = desc

        self.__config()
    
    def setProps(self, name, img, rating, gdata):
        self.name = name
        self.img = img
        self.rating = rating
        self.gdata = gdata
    
    def show(self):
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=0)

    def hide(self):
        self.pack_forget()

    def clear(self):
        for _m in self.__mem:
            _m.destroy()

    def __config(self):
        pass
    
    def __renderRating(self, master=None):
        from data import starfilled
        self.ratingstarF = Image.open(starfilled).resize(size=(25,25))
        self.re = ImageTk.PhotoImage(self.ratingstarF),
        self.ratingPanel = tk.Frame(master, bg="#F6F6F6")
        self.ratingPanel.pack(side=LEFT,pady=3)

        for _ in range(self.rating):
            self.s = tk.Label(master=self.ratingPanel ,image=self.re)
            self.s.pack(side=LEFT, padx=3)

        self.rl = tk.Label(master=self.ratingPanel, font=("Roboto 12 bold"), text=f"{self.rating} / 5", fg="grey")
        self.rl.pack(side=LEFT)

    def render(self):
        self.space = tk.Frame(self, width=200, height=500,)
        self.space.pack(side=LEFT, anchor=NW, padx=60)

        def back(event=None):
            s = time.time()
            local_time = time.ctime(s)
            logg = panels["loggs"]
            logg.addLogg(name=f"product {self.name} leave at '{local_time}'")
            self.hide()
            catalogue = panels["catalogue"]
            rp = panels["recommendation"]
            rp.hide()
            catalogue.showmain()

        self.backbtn = tk.Label(self.space, text="Back",cursor="hand2", font=("Roboto 12 underline"), fg="blue")
        self.backbtn.pack(side=TOP, anchor=NW)
        self.backbtn.bind("<Button-1>", back)

        self.fff = tk.Frame(self)
        self.fff.pack(side=LEFT)

        self.pPanel = tk.Frame(self.fff, width=500, height=500)
        self.pPanel.pack(side=LEFT, padx=20, pady=10)

        self.img = Image.open(self.img).resize(size=(500,500))
        self.r = ImageTk.PhotoImage(self.img),

        self.l = tk.Label(self.pPanel, image=self.r)
        self.l.pack()

        self.pPanel1 = tk.Frame(self.fff, width=500, height=500)
        self.pPanel1.pack(side=TOP, pady=10, fill=BOTH, ipady=30)

        self.l1 = tk.Label(self.pPanel1, text=self.name, font=("Roboto 18 bold"), fg="grey")
        self.l1.pack(side=TOP, anchor=NW)

        self.l1 = tk.Label(self.pPanel1, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n"+
        " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown \nprinter took a galley"+
        " of type and scrambled it to make a type specimen book. It has survived not only five centuries,\n but also the leap into "+
        "electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with\n the release of Letraset"+
        " sheets containing Lorem Ipsum passages, and more \nrecently with desktop publishing software like Aldus PageMaker"+
        " including versions of Lorem Ipsum.", anchor="e" , justify=LEFT ,font=("Roboto 14"), fg="black",)
        self.l1.pack(side=TOP, anchor=NW)

        self.__renderRating(master=self.pPanel1)

        self.buybtn = tk.Button(self.pPanel1, text="Buy",font=("Calibri", 15), state=DISABLED,disabledforeground="white", command=None, relief=GROOVE ,fg="white", bg="#A74D4D")
        self.buybtn.pack(side=LEFT, ipadx=30, ipady=10, padx=30)
        self.__mem.append(self.buybtn)
        self.__mem.append(self.pPanel1)
        self.__mem.append(self.pPanel)
        self.__mem.append(self.fff)
        self.__mem.append(self.backbtn)
        self.__mem.append(self.space)


        

class RecommendationPanel(tk.Frame):

    class Rproduct(tk.Frame):
        def __init__(self, master=None, outer=None, img=None, name=None, rating=None):
            super().__init__(master)
            self.outer = outer
            self.__config()
            
            self.img = img
            self.name = name
            self.rating = rating

            self.render()
            self.pack(side=LEFT)

        def __renderRating(self, rating):
            from data import starfilled
            self.ratingstarF = Image.open(starfilled).resize(size=(25,25))
            self.re = ImageTk.PhotoImage(self.ratingstarF),
            self.ratingPanel = tk.Frame(self, bg="#F6F6F6")
            self.ratingPanel.pack(pady=3)
            for _ in range(rating):
                self.s = tk.Label(master=self.ratingPanel ,image=self.re)
                self.s.pack(side=LEFT, padx=3)

            self.rl = tk.Label(master=self.ratingPanel, font=("Roboto 12 bold"), text=f"{rating} / 5", fg="grey")
            self.rl.pack(side=LEFT)

        def __config(self): pass
        def render(self):
            self.img = Image.open(self.img).resize(size=(300,300))
            self.r = ImageTk.PhotoImage(self.img)
            self.pPanel = tk.Label(self, image=self.r, text=self.name, compound=TOP,font=("Roboto 12"),)
            self.pPanel.pack(side=TOP, anchor=N, padx=20, pady=10)
            self.__renderRating(self.rating)

        
    def __init__(self, master=None, recProd=[]):
        super().__init__(master=master)
        self.recProd = recProd
        self.__mem = []
        self.__config()

    def setProps(self, recp, gdata):
        self.recProd = recp
        self.gdata = gdata

    def show(self):
        self.pack(side=tk.TOP, fill=tk.X, expand=0, padx=10, pady=5)

    def hide(self):
        self.pack_forget()
    
    def clear(self):
        for p in self.__mem: p.destroy()

    def __config(self):
        self["relief"] = GROOVE
        self["borderwidth"] = 2
        self["height"] = 300

    def __plot(self, data):
        root = tk.Tk()
        figure1 = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        data.plot(kind='bar', legend=True, ax=ax1, xlabel="product Name")
        ax1.set_title('Product vs distance')
        root.mainloop()

    def render(self):
        

        self.ff = tk.Frame(self)
        self.ff.pack(side=TOP, anchor=NW, padx=10, pady=5)
        self.l = tk.Label(self.ff, text="Recommendations for you", 
        font=("Roboto 19"), fg="black")
        self.l.pack(side=LEFT)
        
        self.b = tk.Label(self.ff, text="plot graph", 
        font=("Roboto 18"), fg="grey", relief=GROOVE)
        self.b.pack(side=LEFT, padx=10, pady=10)
        self.b.bind("<Button-1>", lambda e: self.__plot(self.gdata))

        for prod in self.recProd:
            self.__mem.append(self.Rproduct(master=self, img=prod["img"], name=prod["name"], rating=prod["average_rating"]))
        
        self.__mem.append(self.ff)