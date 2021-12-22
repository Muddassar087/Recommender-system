import time
import tkinter as tk
from tkinter.constants import *
from PIL import Image, ImageTk
from Frames import panels
from recommendation import recommendKNN

class SearchResult(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.__mem = []

        self.searchRes = []
        self.searchItem = str
        self.__config()

    def setSearchResult(self, res):
        self.searchRes = res
    
    def setSearchItem(self, item):
        self.searchItem = item
    
    def __config(self): pass
    
    def hide(self):
        self.pack_forget()
    
    def show(self):
        self.pack(side=tk.TOP, expand=0,anchor=N, fill=Y)
    
    def clear(self):
        for _m in self.__mem:
            _m.destroy()

    def __renderRating(self, master=None, rating=5):
        from data import starfilled
        self.ratingstarF = Image.open(starfilled).resize(size=(25,25))
        self.re = ImageTk.PhotoImage(self.ratingstarF),
        self.ratingPanel = tk.Frame(master, bg="#F6F6F6")
        self.ratingPanel.pack(side=TOP,pady=3)

        for _ in range(rating):
            self.s = tk.Label(master=self.ratingPanel ,image=self.re)
            self.s.pack(side=LEFT, padx=3)

        self.rl = tk.Label(master=self.ratingPanel, font=("Roboto 12 bold"), text=f"{rating} / 5", fg="grey")
        self.rl.pack(side=LEFT)


    def render(self):
        self.f = tk.Frame(self)
        self.f.pack(side=LEFT, padx=200, anchor=NW, fill=Y, expand=0)
        
        def back(event=None):
            self.hide()
            catalogue = panels["catalogue"]
            catalogue.showmain()

        self.backbtn = tk.Label(self.f, text="Back", cursor="hand2",font=("Roboto 12 underline"), fg="blue")
        self.backbtn.pack(side=TOP, anchor=NW)
        self.backbtn.bind("<Button-1>", back)

        self.p = tk.Frame(self, relief=GROOVE, borderwidth=2)
        self.p.pack(padx=200)

        self.resfor = tk.Label(self.p, text=f'''Search result for "{self.searchItem}"''', font=("Roboto 16 bold"))
        self.resfor.pack(side=TOP, anchor=NW)

        if not self.searchRes.__len__() < 1:
            for prod in self.searchRes:
                self.__mem.append(Sproduct(master=self.p,name=prod['name'], rating=prod['average_rating'], image=prod['img'], _id=prod["product_id"]))
        else:
            self.nf = tk.Label(self.p, text='''No result found!"''', font=("Roboto 16 bold"), fg="green")
            self.nf.pack(side=TOP, anchor=NW)
            self.__mem.append(self.nf)

        self.__mem.append(self.f)
        self.__mem.append(self.backbtn)
        self.__mem.append(self.p)
        self.__mem.append(self.resfor)
        
class Sproduct(tk.Frame):
    def __init__(self, master=None, name=str, rating=int, image=str, _id=int):
        super().__init__(master)
        self.name = name
        self.img = image
        self.rating = rating
        self.id = _id
        self.render()
        self.__config()
        self.pack(side=tk.TOP, padx=50, pady=20, fill=X)

    def __renderRating(self, master=None, r=5):
        from data import starfilled
        self.ratingstarF = Image.open(starfilled).resize(size=(25,25))
        self.re = ImageTk.PhotoImage(self.ratingstarF),
        self.ratingPanel = tk.Frame(master, bg="#F6F6F6")
        self.ratingPanel.pack(side=LEFT,pady=3)

        for _ in range(self.rating):
            self.s = tk.Label(master=self.ratingPanel ,image=self.re)
            self.s.pack(side=LEFT, padx=3)

        self.rl = tk.Label(master=self.ratingPanel, font=("Roboto 12 bold"), text=f"{r} / 5", fg="grey")
        self.rl.pack(side=LEFT)

    def __config(self):
        self['borderwidth'] = 2
        self['relief'] = GROOVE
        self["cursor"] = "hand2"

        def selectedProduct(event=None, _id=int):
            rRes, gdata = recommendKNN(_id=_id)
            print("---------------------")
            print(gdata)
            logg = panels["loggs"]
            s = time.time()
            local_time = time.ctime(s)

            logg.addLogg(name=f"product id {_id} at '{local_time}'")
            c = panels["catalogue"]
            c.hidemain()
            pp = panels["productpage"]
            sr = panels["searchresult"]
            sr.hide()
            rp = panels["recommendation"]
            pp.clear()
            rp.clear()
            rp.setProps(rRes, gdata)
            pp.setProps(self.name, self.img, self.rating, gdata)
            pp.render()
            rp.render()
            pp.show()
            rp.show()

        self.bind("<Enter>", lambda event: self.pname.config(font=("Roboto 18 bold underline"), fg="grey"))
        self.bind("<Leave>", lambda event: self.pname.config(font=("Roboto 18 bold"), fg="black"))

        self.image.bind("<Button-1>", lambda event: selectedProduct(_id=self.id))
        self.pname.bind("<Button-1>", lambda event: selectedProduct(_id=self.id))

    def render(self):
            self._img = Image.open(self.img).resize(size=(200,200))
            self.r = ImageTk.PhotoImage(self._img),
            self.image = tk.Label(self, image=self.r)
            self.image.pack(side=LEFT)
            
            self.f = tk.Frame(self)
            self.f.pack(side=LEFT, ipadx=5)

            self.pname = tk.Label(self.f, text=self.name, font=("Roboto 18 bold"))
            self.pname.pack(side=tk.TOP)
            self.__renderRating(master=self.f, r=self.rating)        
