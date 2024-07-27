from tkinter import *
#from PIL import ImageTk, Image
#import sqlite3
from tkinter import ttk
root = Tk()
root.title("Panels")
#root.iconbitmap()
root.geometry("400x500")
panel_1 = PanedWindow(bd=4, relief="raised" , bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)

panel_2 = PanedWindow(panel_1, orient=VERTICAL , bd=4, relief="raised" , bg="blue")
panel_1.add(panel_2)

top_label = Label(panel_2, text="Top Panel")
panel_2.add(top_label)

bottom_label = Label(panel_2, text="Bottom Panel")
panel_2.add(bottom_label)

panel_3 = PanedWindow(panel_2, orient=HORIZONTAL , bd=4, relief="raised" , bg="pink")
third_label = Label(panel_3, text="third Panel")
panel_3.add(third_label)
panel_2.add(panel_3)


root.mainloop()