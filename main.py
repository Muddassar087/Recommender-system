import tkinter as tk
from searchbar import SearchBar as search
from productcatalogue import Catalogue
from loggingpanel import LoggingPanel
from Frames import panels

class root(tk.Tk):
    minWidth = 1480
    minHeight = 950
    offsetx = 200
    offsety = 50

    def __init__(self):
        super().__init__()
        self.checkvar = tk.BooleanVar()
        self.checkvar2 = tk.BooleanVar()

        self.__config()
        self.render()

    def __config(self):

        def showloggs():
            loggs = panels['loggs']
            statusloggs = self.checkvar.get()
            if statusloggs:
                loggs.lshow()
            else:
                loggs.lhide()
                self.checkvar2.set(False)

        def _rendermenu():
            menu = tk.Menu(self, tearoff=0)
            actionmenu = tk.Menu(menu, tearoff=0)
            actionmenu.add_checkbutton(label="Show loggs", command=showloggs, onvalue=1, offvalue=0, variable=self.checkvar)
            menu.add_cascade(label="Actions", menu=actionmenu)

            return menu
        def rootfocus():
            self.focus_set()

        self.bind("<Button-1>", rootfocus())
        self.config(menu=_rendermenu())
        self.geometry(f"{self.minWidth}x{self.minHeight}+{self.offsetx}+{self.offsety}")

    def render(self):
        panels["search"] = search(master=self)
        panels["catalogue"] = Catalogue(self)
        panels["loggs"] = LoggingPanel(self)

if __name__ == "__main__":
    window = root()
    window.mainloop()