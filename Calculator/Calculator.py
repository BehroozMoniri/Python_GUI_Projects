# This is a sample Python script.
import tkinter as tk
from tkinter import StringVar, Button, Entry
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
mainwindow = tk.Tk()
mainwindow.title("Calculator")
# import math

ans_entry = Entry(mainwindow, relief="raised", bd=5, width=20, font=("Helvetica",15), bg="green", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)
btn_1 = Button(mainwindow, text="1", padx=20, pady=10)
btn_1.grid(row=1, column=0)

btn_2 = Button(mainwindow, text="2", padx=20, pady=10)
btn_2.grid(row=1, column=1)

btn_3 = Button(mainwindow, text="3", padx=20, pady=10)
btn_3.grid(row=1, column=2)

btn_div = Button(mainwindow, text="/", padx=20, pady=10)
btn_div.grid(row=1, column=3)

btn_4 = Button(mainwindow, text="4", padx=20, pady=10)
btn_4.grid(row=2, column=0)

btn_5 = Button(mainwindow, text="5", padx=20, pady=10)
btn_5.grid(row=2, column=1)

btn_6 = Button(mainwindow, text="6", padx=20, pady=10)
btn_6.grid(row=2, column=2)

btn_mul = Button(mainwindow, text="*", padx=20, pady=10)
btn_mul.grid(row=2, column=3)

btn_7 = Button(mainwindow, text="7", padx=20, pady=10)
btn_7.grid(row=3, column=0)

btn_8 = Button(mainwindow, text="8", padx=20, pady=10)
btn_8.grid(row=3, column=1)

btn_9 = Button(mainwindow, text="9", padx=20, pady=10)
btn_9.grid(row=3, column=2)

btn_sub = Button(mainwindow, text="-", padx=20, pady=10)
btn_sub.grid(row=3, column=3)

btn_clr = Button(mainwindow, text="C", padx=20, pady=10)
btn_clr.grid(row=4, column=0)

btn_0 = Button(mainwindow, text="0", padx=20, pady=10)
btn_0.grid(row=4, column=1)

btn_ans = Button(mainwindow, text="=", padx=20, pady=10)
btn_ans.grid(row=4, column=2)

btn_plus = Button(mainwindow, text="+", padx=20, pady=10)
btn_plus.grid(row=4, column=3)

btn_oct = Button(mainwindow, text="Oct", padx=14, pady=10)
btn_oct.grid(row=5, column=0)

btn_hex = Button(mainwindow, text="Hex", padx=14, pady=10)
btn_hex.grid(row=5, column=1)

btn_dec = Button(mainwindow, text=".", padx=20, pady=10)
btn_dec.grid(row=5, column=2)

btn_power= Button(mainwindow, text="^", padx=20, pady=10)
btn_power.grid(row=5, column=3)
equation = {}
def mouse_button_release(event):
    #print(event.x, event.y)
    wid = event.widget
    #print("Widget : ", wid)
    text = wid.cget("text")
    #print("text", text)

    if text in "0123456789.":
        ans_entry.insert(len(ans_entry.get()), text)
    if text == "Oct" and len(ans_entry.get()):
        oct_num = oct(int(ans_entry.get()))
        oct_num = oct_num[2:]
        ans_entry.delete(0, 'end')
        ans_entry.insert(0, str(oct_num))

    if text == "Hex" and len(ans_entry.get()):
        hex_num = hex(int(ans_entry.get()))
        hex_num = hex_num[2:]
        ans_entry.delete(0, 'end')
        ans_entry.insert(0, str(hex_num))

    if text == 'C':
        ans_entry.delete(0, 'end')
        equation.clear()

    if text in "+-*/^":
        if ans_entry.get():
            equation['num_1'] = float(ans_entry.get())
            ans_entry.delete(0, 'end')
            equation['operation'] = text
    if text == "=":
        if 'operation' in equation.keys() and len(ans_entry.get()):
            equation['num_2'] = float(ans_entry.get())
            ans_entry.delete(0, 'end')
            #print(equation)
            num_1 = equation['num_1']
            op = equation['operation']
            num_2 = equation['num_2']

            if op == '+':
                ans = num_1 + num_2
            elif op == "-":
                ans = num_1 - num_2
            elif op == "*":
                ans = num_1 * num_2
            elif op == "/":
                ans = num_1 / num_2
            elif op == "^":
                ans = pow(num_1 ,num_2)


            ans_entry.insert(0, ans)
            ans_entry.clear()

mainwindow.bind('<ButtonRelease-1>', mouse_button_release)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
mainwindow.mainloop()