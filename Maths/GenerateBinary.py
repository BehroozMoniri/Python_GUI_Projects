import tkinter as tk
from random import choice

root = tk.Tk()

bits = 8
rows = 8

numbers = [0, 1]

matrix_locations = [(x, y + 1) for x in range(bits) for y in range(rows)]
matrix_texts     = []
matrix_labels    = []

result_locations = [(x, y + 1) for x in range(bits, bits + 1) for y in range(rows)]
result_texts     = []
result_labels    = []

def generate_labels():

    for index, location in enumerate(matrix_locations):

        matrix_texts.append(tk.StringVar())
        matrix_texts[index].set(choice(numbers))

        matrix_labels.append(tk.Label(root, textvariable = matrix_texts[index]))
        matrix_labels[index].grid(row = location[1], column = location[0], padx = 2, pady = 2)

    for index, location in enumerate(result_locations):

        result_texts.append(tk.StringVar())
        result_texts[index].set("")

        result_labels.append(tk.Label(root, textvariable = result_texts[index]))
        result_labels[index].grid(row = location[1], column = location[0], padx = 2, pady = 2, sticky = "W")

    read_matrix()

def update_matrix():

    for text in matrix_texts:

        text.set(choice(numbers))

    read_matrix()

def read_matrix():

    string_binaries = ["" for row in range(rows)]

    for index, location in enumerate(matrix_locations):

        string_binaries[location[1] - 1] += str(matrix_texts[index].get())

    denaries = [int(string, base = 2) for string in string_binaries]

    for row in range(rows):

        result_texts[row].set(" = {}".format(denaries[row]))

binary_label = tk.Label(root, text = "Binaries")
binary_label.grid(row = 0, column = 0, columnspan = bits)

denary_label = tk.Label(root, text = "Denaries")
denary_label.grid(row = 0, column = bits)

generate_labels()

update_matrix_button = tk.Button(root, text = "Update matrix", command = update_matrix)
update_matrix_button.grid(row = rows + 1, column = 0, columnspan = bits + 1, sticky = "EW")

root.mainloop()

