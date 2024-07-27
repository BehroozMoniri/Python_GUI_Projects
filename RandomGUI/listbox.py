from tkinter import *

root = Tk()
root.geometry("500x500")
# s
my_listbox = Listbox(root, width=50,   selectmode=MULTIPLE) #yscrollcommand=my_scrol
my_listbox.grid(row= 0, column=0, columnspan=5 , pady=15)

my_listbox.insert(END, "This is the first item")

my_list = ["one", "two" , "three"]*6

for item in my_list:
    my_listbox.insert(END, item)

def delete():
    my_listbox.delete(ANCHOR)
    my_lable.config(text='')

def select():
    my_lable.config(text=my_listbox.get(ANCHOR))
def delete_all():
    my_listbox.delete(0, END)
entry = Entry( root, textvariable=StringVar, width=30)
entry.grid(row= 2, column=1, pady=5)

global new_label
new_label = Label(root, text= "")
new_label.grid(row= 5, column=0)
def add():
    my_listbox.insert(END, entry.get())
    entry.delete(0, END)
def select_all():
    result = ""
    for item in my_listbox.curselection():
        result += str(my_listbox.get(item) ) + "\n"
    print(result)
    new_label.config(text=result)
def delete_multiple():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


my_lable = Label(root, text="Enter your text:")
my_lable.grid(row= 2, column=0, pady=5)

add_button = Button(root, text="Add" , command= add)
add_button.grid(row= 3, column=1, pady=5) 

my_button = Button(root, text="Delete" , command= delete)
my_button.grid(row= 4, column=0, pady=5)

my_button2 = Button(root, text="Select" , command= select)
my_button2.grid(row= 3, column=2, pady=5)

my_button3 = Button(root, text="Delete All" , command= delete_all)
my_button3.grid(row= 3, column=3, pady=5)

my_button4 = Button(root, text="Select All" , command= select_all)
my_button4.grid(row= 3, column=4, pady=5)

my_button4 = Button(root, text="Delete multiple" , command= delete_multiple )
my_button4.grid(row= 4, column=1, pady=5)
#my_frame = Frame(root)
my_scroll = Scrollbar(root, orient=VERTICAL, )

my_scroll.config(command=my_listbox.yview)
my_scroll.grid(row= 0, column=4, sticky="e" ,ipady=50) #fill=Y
#my_frame.grid(row= 0, column=0)





root.mainloop()