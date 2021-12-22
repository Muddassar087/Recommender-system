import time
import tkinter as tk
from Frames import panels
from tkinter.constants import *
from PIL import Image, ImageTk
from data import prodDisplay, starfilled
from doubleScroll import DoubleScrolledFrame
from productpage import ProductPage, RecommendationPanel
from recommendation import recommendKNN
from searchresult import SearchResult

class Catalogue(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.__config()
        self.render()
        self.pack(side=LEFT, pady=10, fill=BOTH, expand=1, padx=10)
    
    def __config(self):
        self["bg"] = "#DADADA"

    def hidemain(self):
        self.frame.pack_forget()
    
    def showmain(self):
        self.frame.pack(side=TOP, fill=BOTH, expand=1)

    def render(self):
        self.mainFrame = tk.Frame(master=self)
        self.mainFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.sf = DoubleScrolledFrame(self.mainFrame)
        panels['scrollbar'] = self.sf
        self.frame = tk.Frame(self.sf)
        self.frame.pack(side=TOP, fill=BOTH, expand=1)

        panels["productsframe"] = self.frame

        for i in range(len(prodDisplay)):
            for j in range(len(prodDisplay[i])):
                pr = prodDisplay[i][j]
                Product(self.frame, img=pr["img"], name=pr["name"], rating=pr["average_rating"],_id=pr["product_id"], row=i, col=j)

        panels["productpage"] = ProductPage(master=self.sf)
        panels["recommendation"] = RecommendationPanel(master=self.sf)
        panels["searchresult"] = SearchResult(master=self.sf)

        self.sf.pack(side=TOP, fill=BOTH, expand=1)

class Product(tk.Frame):
    def __init__(self, master=None, img=str, name=str, rating=int, _id=int, row=int, col=int):
        super().__init__(master=master)
        self.image = img
        self.rating = rating
        self.name = name
        self.id = _id

        self._r = row
        self._c = col
        self.img = Image.open(self.image).resize(size=(300,300))
        self.r = ImageTk.PhotoImage(self.img),

        self.ratingstarF = Image.open(starfilled).resize(size=(25,25))
        self.re = ImageTk.PhotoImage(self.ratingstarF),

        self.render()
        self.__config()

        self.grid(padx=5, pady=10, row=self._r, column=self._c)
    
    def __config(self):

        def onenter(event=None):
            self.pImage["fg"] = "grey"
            self.pImage["font"] = "Roboto 12 underline"
        def onleave(event=None):
            self.pImage["font"] = "Roboto 12"
            self.pImage["fg"] = "black"

        self.bind('<Enter>', onenter)
        self.bind('<Leave>', onleave)

        self.pImage.bind("<Button-1>",lambda e: self.selectedProduct(_id=self.id))
        
    def selectedProduct(self, event=None, _id=int):
        
        rRes, gData = recommendKNN(_id=_id)
        s = time.time()
        local_time = time.ctime(s)
        print("-----------------------")
        print(gData)
        logg = panels["loggs"]
        logg.addLogg(name=f"product id {self.name} at '{local_time}'")
        c = panels["catalogue"]
        sb = panels['scrollbar']
        sb.rep()
        c.hidemain()
        pp = panels["productpage"]
        rp = panels["recommendation"]
        pp.clear()
        rp.clear()
        rp.setProps(rRes, gData)
        pp.setProps(self.name, self.image, self.rating, gData)
        pp.render()
        rp.render()
        pp.show()
        rp.show()

    def renderRating(self):
        self.ratingPanel = tk.Frame(self, bg="#F6F6F6")
        self.ratingPanel.pack(pady=3)
        for _ in range(self.rating):
            self.s = tk.Label(master=self.ratingPanel ,image=self.re)
            self.s.pack(side=LEFT, padx=3)

        self.rl = tk.Label(master=self.ratingPanel, font=("Roboto 12 bold"), text=f"{self.rating} / 5", fg="grey")
        self.rl.pack(side=LEFT)
    
    def render(self):
        self.pImage = tk.Label(master=self,text=self.name, font=("Roboto 12") ,image=self.r, compound="top", cursor="hand2")
        self.pImage.pack()
        self.renderRating()