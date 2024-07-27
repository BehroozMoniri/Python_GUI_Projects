###!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import *


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.punches_list = []
        self.ent = tk.StringVar()

        self.init_ui()

    def init_ui(self):


        f = ttk.Frame()
        ttk.Label(f, text = "Entry").pack()
        self.txTest = ttk.Entry(f, textvariable=self.ent).pack()
        self.lstItems = self.get_listbox(f, 40,80)
        w = ttk.Frame()

        ttk.Button(w, text="Punch In",command=self.punch_In).pack()
        ttk.Button(w, text="Punch Out", command=self.punch_Out).pack()
        ttk.Button(w, text="Close", command=self.on_close).pack()

        f.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        w.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)


    def punch_In(self,):
        s = "IN {0:>30} {1}".format(str(datetime.now()), self.ent.get())
        self.set_list(s)

    def punch_Out(self):
        s = "OUT {0:>29} {1}".format(str(datetime.now()), self.ent.get())
        self.set_list(s)

    def set_list(self,s):

        self.punches_list.append(s)

        self.lstItems.delete(0, tk.END)
        for i in self.punches_list:
            self.lstItems.insert(tk.END, i)

    def on_set(self):

        self.check.set(1)

    def on_close(self):
        self.parent.on_exit()

    def get_listbox(self, container, height=None, width=None):


        sb = tk.Scrollbar(container,orient=tk.VERTICAL)

        w = tk.Listbox(container,
                    relief=tk.GROOVE,
                    selectmode=tk.BROWSE,
                    height=height,
                    width=width,
                    background = 'white',
                    font='TkFixedFont',
                    yscrollcommand=sb.set,)

        sb.config(command=w.yview)

        w.pack(side=tk.LEFT,fill=tk.BOTH, expand =1) 
        sb.pack(fill=tk.Y, expand=1)

        return w        

class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.set_style()
        self.set_title() 
        Main(self,)     

    def set_style(self):
        self.style = ttk.Style()
        #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.theme_use("clam")

    def set_title(self):
        s = "{0}".format('Employee Time-Clock')
        self.title(s)

    def on_exit(self):
        """Close all"""
        if messagebox.askokcancel( self.title(), "Do you want to quit?", parent=self):
            self.destroy()               

if __name__ == '__main__':
    app = App()
    app.mainloop()