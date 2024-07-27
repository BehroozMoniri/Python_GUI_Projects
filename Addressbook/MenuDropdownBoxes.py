from tkinter import *
#from PIL import ImageTk, Image
#import sqlite3
from tkinter import ttk
root = Tk()
root.title("Address Book")
#root.iconbitmap()
root.geometry("400x500")

def selected(event):
    myLabel = Label(root, text=clicked.get()).pack()
     
# binding drop down boxes and menu boxes
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20) #grid(root, bd=column, columnspan=1 ,row=0, column=1, padx=20, pady=10)#

def comboClicked(event):
    global myLabel
    myLabel = Label(root, text=myCombo.get()).pack()


def clear():
    hide_all_frames()
    myLabel.pack_forget()
    root.children.clear()
    root.pack_forget()

myCombo = ttk.Combobox(root, values=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboClicked)
myCombo.pack() #grid(root, row=2, column=1, padx=20, pady=10)

# Creating menu bar on top of the page
def our_command():
    global myLabel
    myLabel = Label(root, text="Wow you clicked a drop down menue").pack()

# creating frames
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)

def edit_cut_new():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    global myLabel
    myLabel = Label(edit_cut_frame, text=myCombo.get()).pack()


def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()    

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    global myLabel
    myLabel = Label(file_new_frame, text=myCombo.get()).pack()



myMenu = Menu(root)
root.config(menu=myMenu)
fileMenu=Menu(myMenu)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New...", command=file_new)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut_new)
edit_menu.add_command(label="Copy", command=edit_cut_new)
edit_menu.add_command(label="Clear All", command=clear)

button_clear = Button(root, text="Clear All", command=clear)
button_clear.pack()

file_new_frame = Frame(root, width=400, height=400, bg="green")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")



root.mainloop()