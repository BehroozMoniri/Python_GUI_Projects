from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Address Book")
#root.iconbitmap()
root.geometry("400x500")

conn = sqlite3.connect("address_book.db")
cursor = conn.cursor()
#create a table need to be done only once
# cursor.execute(""" CREATE TABLE addresses(
#                first_name text,
#                last_name text,
#                address text,
#                city text,
#                state text,
#                zipcode int
#                )""")





# delete function
def delete():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM addresses WHERE oid={delete_box.get()}"      )
    delete_box.delete(0, END)
    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
                   {
                       "f_name":f_name.get(),
                       "l_name": l_name.get(),
                       "address": address.get(),
                       "city": city.get(),
                       "state":state.get(),
                       "zipcode": zipcode.get()
                   })

    conn.commit()
    conn.close()

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    query()
# Query will grab data from the database
def query():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    #print(records)+
    print_records = "ID, FirstName, LastName, City, State, zipcode \n"
    for record in records:
        print_records +=   str(record[6]) + " " +str(record[0]) + " " + str(record[1]) +  " " + str(record[2]) + " " +str(record[3]) + " " +str(record[4])+ " " +str(record[5])+ "\n"  

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0 , columnspan=2)
    conn.commit()
    conn.close()

def save():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    record_id = delete_box.get()
    cursor.execute("""UPDATE addresses SET   
                    first_name = :first,
                    last_name = :last,
                    address= :address,
                    city= :city,
                    state= :state,
                    zipcode= :zipcode
                   WHERE oid = :oid""",  {
                        "first":f_name_editor.get(),
                       "last": l_name_editor.get(),
                       "address": address_editor.get(),
                       "city": city_editor.get(),
                       "state":state_editor.get(),
                       "zipcode": zipcode_editor.get(), 
                       "oid" : record_id 
                   })
    conn.commit()
    conn.close()
    editor.destroy()
    query()

def update():
    global editor, f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor
    editor = Tk()
    editor.title("Update record")
    editor.geometry("320x200")
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(20, 0))# to push it down from the top pady
    f_name_label = Label(editor, text="First Name",justify="left")
    f_name_label.grid(row=0, column=0, pady=(20, 0) )
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    l_name_label = Label(editor, text="Last Name",justify="right")
    l_name_label.grid(row=1, column=0 )
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    address_label = Label(editor, text="Address",justify="right")
    address_label.grid(row=2, column=0)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    city_label = Label(editor, text="City",justify="right")
    city_label.grid(row=3, column=0)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    state_label = Label(editor, text="State",justify="right")
    state_label.grid(row=4, column=0)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    zipcode_label = Label(editor, text="Zipcode",justify="right")
    zipcode_label.grid(row=5, column=0)

    # submit button
    submit_btn = Button(editor, text="Save Record", command=save)
    submit_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=20)
    cancel_btn = Button(editor, text="Cancle", command=cancel)
    cancel_btn.grid(row=6, column=1, columnspan=1,  pady=10, padx=10, ipadx=25)
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
     
    cursor.execute(f"SELECT * FROM addresses WHERE oid={delete_box.get()}")
    records = cursor.fetchall()
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    conn.commit()
    conn.close()
    query()
def cancel():
    conn.close()
    editor.destroy()
    query()

def close():
    root.destroy()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(20, 0))# to push it down from the top pady
f_name_label = Label(root, text="First Name",justify="right")
f_name_label.grid(row=0, column=0, pady=(20, 0) )
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
l_name_label = Label(root, text="Last Name",justify="right")
l_name_label.grid(row=1, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
address_label = Label(root, text="Address",justify="right")
address_label.grid(row=2, column=0)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
city_label = Label(root, text="City",justify="right")
city_label.grid(row=3, column=0)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
state_label = Label(root, text="State",justify="right")
state_label.grid(row=4, column=0)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
zipcode_label = Label(root, text="Zipcode",justify="right")
zipcode_label.grid(row=5, column=0)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)
delete_box_label = Label(root, text="Select ID Number:",justify="right")
delete_box_label.grid(row=8, column=0)

# submit button
submit_btn = Button(root, text="Add records to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=1, pady=10, padx=10, ipadx=10) #, ipadx=100

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6, column=1, columnspan=1,  pady=10, padx=10, ipadx=25) #, ipadx=127

delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=1,  pady=10, padx=10, ipadx=35) #, ipadx=136

update_btn = Button(root, text="Edit record", command=update)
update_btn.grid(row=10, column=1, columnspan=1,  pady=10, padx=10, ipadx=35) #, ipadx=143

close_btn = Button(root, text="Close", command=close )
close_btn.grid(row=13, column=0, columnspan=2,  pady=10, padx=10, ipadx=153)


#commit changes and close
# conn.commit()
# conn.close()

root.mainloop()