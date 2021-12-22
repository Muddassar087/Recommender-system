import tkinter as tk
from tkinter.constants import *
from Frames import panels
from services import search

class SearchBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.__mem = []

        self.__config()
        self.render()
        self.pack(side=TOP, expand=0, fill=X, padx=10,ipady=30)

    def __config(self):
        self["bg"] = "#DADADA"

    def frame(self, x, y):
        self.p = tk.Frame

    def render(self):
        self.searchFieldvar = tk.StringVar()
        self.panel = tk.Frame(self, bg='#DADADA')
        self.panel.pack(ipadx=10, side=BOTTOM)
        
        self.resfor = tk.Label(self.panel, text="Product Recommender System", font=("roboto 19 italic"), bg="#DADADA")
        self.resfor.pack(side=TOP, anchor=N, ipady=10)

        self.searchField = tk.Entry(master=self.panel, highlightthickness=2,width=60, font=("Calibri", 15), relief=GROOVE, borderwidth=1,textvariable=self.searchFieldvar )
        self.searchField.pack(side=LEFT, pady=10, ipadx=20, ipady=6, expand=0, fill=X)
        
        def btnf(event=None):
            searchItem = self.searchFieldvar.get()
            if searchItem.__len__() > 1:
                catalogue = panels['catalogue']
                catalogue.hidemain()
                searchResult = panels["searchresult"]
                pp = panels["productpage"]
                rec = panels["recommendation"]
                rec.hide()
                pp.hide()
                searchResult.clear()

                searchResult.setSearchResult(res=search(searchItem))
                searchResult.setSearchItem(item=searchItem)
                searchResult.show()
                searchResult.render()

                logg = panels["loggs"]
                logg.addLogg(name=f"Search result for {searchItem}")
            self.btn.focus_set()

        self.btn = tk.Button(master=self.panel, text="Search", font=("Calibri", 15),  width=12, fg="white", bg="#A74D4D")
        self.btn.pack(side=LEFT, padx=6, fill=X)
        self.btn.bind("<Button-1>", btnf)
        self.btn.bind("<Return>", btnf)
        
