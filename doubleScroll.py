from tkinter.constants import ALL


try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import tkinter as tk
    import tkinter.ttk as ttk

class DoubleScrolledFrame:
    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        self.outer = tk.Frame(master, **kwargs)

        self.vsb = ttk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb = ttk.Scrollbar(self.outer, orient=tk.HORIZONTAL)
        self.hsb.grid(row=1, column=0, sticky='ew')
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=height)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.outer.rowconfigure(0, weight=1)
        self.outer.columnconfigure(0, weight=1)
        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas['xscrollcommand'] = self.hsb.set
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview
        self.hsb['command'] = self.canvas.xview

        self.inner = tk.Frame(self.canvas)
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            return getattr(self.outer, item)
        else:
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        self.canvas.config(scrollregion = (0,0, max(x2, width), max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")
    
    def rep(self):
        #before repaint store vsb position caclulated in pixels from top
        bbox = self.canvas.bbox(ALL)
        self.mem_vsb_pos = self.canvas.yview()[0] * (bbox[3] - bbox[1])

        #after repaint (back calculation):
        bbox = self.canvas.bbox(ALL)
        self.canvas.yview_moveto(self.vsb.get()[0] / (bbox[3]-bbox[1]))

        #before repaint - if need repaint from top
        self.mem_vsb_pos = 0.0
        
    def _on_mousewheel(self, event):
        func = self.canvas.xview_scroll if event.state & 1 else self.canvas.yview_scroll 
        if event.num == 4 or event.delta > 0:
            func(-1, "units" )
        elif event.num == 5 or event.delta < 0:
            func(1, "units" )
    
    def __str__(self):
        return str(self.outer)