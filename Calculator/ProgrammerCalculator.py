import tkinter as tk
from tkinter import ttk, Menu
from math import sin, cos, tan, exp, log, pi, radians

class ProgrammerCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Powerful Programmer's Calculator")
        self.mode = tk.StringVar(value="Programmer")
        self.result = tk.StringVar(value="0")
        self.create_widgets()
        self.last_operation = None

    def create_widgets(self):
        # Menu for Bitwise Operations
        menubar = Menu(self.root)
        bitwise_menu = Menu(menubar, tearoff=0)
        bitwise_menu.add_command(label="AND", command=lambda: self.bitwise_operation("AND"))
        bitwise_menu.add_command(label="NAND", command=lambda: self.bitwise_operation("NAND"))
        bitwise_menu.add_command(label="OR", command=lambda: self.bitwise_operation("OR"))
        bitwise_menu.add_command(label="XOR", command=lambda: self.bitwise_operation("XOR"))
        bitwise_menu.add_command(label="NOT", command=lambda: self.bitwise_operation("NOT"))
        bitwise_menu.add_command(label="NOR", command=lambda: self.bitwise_operation("NOR"))
        menubar.add_cascade(label="Bitwise Operations", menu=bitwise_menu)
        self.root.config(menu=menubar)

        # Mode Switch
        mode_frame = tk.Frame(self.root)
        mode_frame.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(mode_frame, text="Programmer", command=lambda: self.switch_mode("Programmer")).pack(side=tk.LEFT)
        ttk.Button(mode_frame, text="Scientific", command=lambda: self.switch_mode("Scientific")).pack(side=tk.LEFT)

        # Display
        display = ttk.Entry(self.root, textvariable=self.result, font=("Arial", 24), justify="right")
        display.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Paned Window for Buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True)

        self.switch_mode("Programmer")

    def switch_mode(self, mode):
        self.mode.set(mode)
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        if mode == "Programmer":
            self.create_prog_buttons()
        else:
            self.create_sci_buttons()

    def create_prog_buttons(self):
        buttons = [
            ("Hex", self.hex_convert), ("Dec", self.dec_convert), ("Oct", self.oct_convert), ("Bin", self.bin_convert),
            ("<<", self.left_shift), (">>", self.right_shift),
            ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
            ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
            ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
            ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
            ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
            ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
            ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
            ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
            ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
            ("=", self.evaluate_expression)
        ]
        self.arrange_buttons(buttons)

    def create_sci_buttons(self):
        buttons = [
            ("sin", lambda: self.scientific_operation("sin")), ("cos", lambda: self.scientific_operation("cos")),
            ("tan", lambda: self.scientific_operation("tan")), ("exp", lambda: self.scientific_operation("exp")),
            ("log", lambda: self.scientific_operation("log")), ("pi", lambda: self.append_to_display(str(pi))),
            ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
            ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
            ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
            ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
            ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
            ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
            ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
            ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
            ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
            ("=", self.evaluate_expression)
        ]
        self.arrange_buttons(buttons)

    def arrange_buttons(self, buttons):
        rows = 5
        cols = 4
        for r in range(rows):
            self.buttons_frame.rowconfigure(r, weight=1)
        for c in range(cols):
            self.buttons_frame.columnconfigure(c, weight=1)

        for index, (text, command) in enumerate(buttons):
            row = index // cols
            col = index % cols
            button = ttk.Button(self.buttons_frame, text=text, command=command)
            button.grid(row=row, column=col, sticky=tk.NSEW)

    def hex_convert(self):
        self.result.set(hex(int(self.result.get(), 0)))

    def dec_convert(self):
        self.result.set(int(self.result.get(), 0))

    def oct_convert(self):
        self.result.set(oct(int(self.result.get(), 0)))

    def bin_convert(self):
        self.result.set(bin(int(self.result.get(), 0)))

    def left_shift(self):
        self.result.set(int(self.result.get(), 0) << 1)

    def right_shift(self):
        self.result.set(int(self.result.get(), 0) >> 1)

    def bitwise_operation(self, op):
        try:
            value = int(self.result.get(), 0)
            if op == "NOT":
                self.result.set(~value)
            else:
                second_value = int(self.get_second_value(), 0)
                if op == "AND":
                    self.result.set(value & second_value)
                elif op == "OR":
                    self.result.set(value | second_value)
                elif op == "XOR":
                    self.result.set(value ^ second_value)
                elif op == "NAND":
                    self.result.set(~(value & second_value))
                elif op == "NOR":
                    self.result.set(~(value | second_value))
        except ValueError:
            self.result.set("Error")

    def get_second_value(self):
        return tk.simpledialog.askstring("Input", "Enter second value:")

    def append_to_display(self, value):
        if self.result.get() == "0" or self.last_operation == "=":
            self.result.set(value)
        else:
            self.result.set(self.result.get() + value)
        self.last_operation = value

    def arithmetic_operation(self, operator):
        self.result.set(self.result.get() + operator)
        self.last_operation = operator

    def clear_display(self):
        self.result.set("0")

    def scientific_operation(self, op):
        try:
            value = float(self.result.get())
            if op == "sin":
                self.result.set(sin(radians(value)))
            elif op == "cos":
                self.result.set(cos(radians(value)))
            elif op == "tan":
                self.result.set(tan(radians(value)))
            elif op == "exp":
                self.result.set(exp(value))
            elif op == "log":
                self.result.set(log(value))
        except ValueError:
            self.result.set("Error")

    def evaluate_expression(self):
        try:
            self.result.set(eval(self.result.get()))
        except Exception as e:
            self.result.set("Error")
        self.last_operation = "="

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ProgrammerCalculator(root)
    root.mainloop()

# import tkinter as tk
# from tkinter import ttk, Menu
# from math import sin, cos, tan, exp, log, pi, radians

# class ProgrammerCalculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Powerful Programmer's Calculator")
#         self.mode = tk.StringVar(value="Programmer")
#         self.result = tk.StringVar(value="0")
#         self.create_widgets()
#         self.last_operation = None

#     def create_widgets(self):
#         # Menu for Bitwise Operations
#         menubar = Menu(self.root)
#         bitwise_menu = Menu(menubar, tearoff=0)
#         bitwise_menu.add_command(label="AND", command=lambda: self.bitwise_operation("AND"))
#         bitwise_menu.add_command(label="NAND", command=lambda: self.bitwise_operation("NAND"))
#         bitwise_menu.add_command(label="OR", command=lambda: self.bitwise_operation("OR"))
#         bitwise_menu.add_command(label="XOR", command=lambda: self.bitwise_operation("XOR"))
#         bitwise_menu.add_command(label="NOT", command=lambda: self.bitwise_operation("NOT"))
#         bitwise_menu.add_command(label="NOR", command=lambda: self.bitwise_operation("NOR"))
#         menubar.add_cascade(label="Bitwise Operations", menu=bitwise_menu)
#         self.root.config(menu=menubar)

#         # Mode Switch
#         mode_frame = tk.Frame(self.root)
#         mode_frame.pack(side=tk.TOP, fill=tk.X)
#         ttk.Button(mode_frame, text="Programmer", command=lambda: self.switch_mode("Programmer")).pack(side=tk.LEFT)
#         ttk.Button(mode_frame, text="Scientific", command=lambda: self.switch_mode("Scientific")).pack(side=tk.LEFT)

#         # Display
#         display = ttk.Entry(self.root, textvariable=self.result, font=("Arial", 24), justify="right")
#         display.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

#         # Paned Window for Buttons
#         self.paned_window = tk.PanedWindow(self.root, orient=tk.VERTICAL)
#         self.paned_window.pack(fill=tk.BOTH, expand=True)

#         self.buttons_frame = tk.Frame(self.paned_window)
#         self.paned_window.add(self.buttons_frame)
#         self.create_prog_buttons()

#     def switch_mode(self, mode):
#         self.mode.set(mode)
#         for widget in self.buttons_frame.winfo_children():
#             widget.destroy()
#         if mode == "Programmer":
#             self.create_prog_buttons()
#         else:
#             self.create_sci_buttons()

#     def create_prog_buttons(self):
#         buttons = [
#             ("Hex", self.hex_convert), ("Dec", self.dec_convert), ("Oct", self.oct_convert), ("Bin", self.bin_convert),
#             ("<<", self.left_shift), (">>", self.right_shift),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]
#         for text, command in buttons:
#             button = ttk.Button(self.buttons_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def create_sci_buttons(self):
#         buttons = [
#             ("sin", lambda: self.scientific_operation("sin")), ("cos", lambda: self.scientific_operation("cos")),
#             ("tan", lambda: self.scientific_operation("tan")), ("exp", lambda: self.scientific_operation("exp")),
#             ("log", lambda: self.scientific_operation("log")), ("pi", lambda: self.append_to_display(str(pi))),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]
#         for text, command in buttons:
#             button = ttk.Button(self.buttons_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def hex_convert(self):
#         self.result.set(hex(int(self.result.get(), 0)))

#     def dec_convert(self):
#         self.result.set(int(self.result.get(), 0))

#     def oct_convert(self):
#         self.result.set(oct(int(self.result.get(), 0)))

#     def bin_convert(self):
#         self.result.set(bin(int(self.result.get(), 0)))

#     def left_shift(self):
#         self.result.set(int(self.result.get(), 0) << 1)

#     def right_shift(self):
#         self.result.set(int(self.result.get(), 0) >> 1)

#     def bitwise_operation(self, op):
#         try:
#             value = int(self.result.get(), 0)
#             if op == "NOT":
#                 self.result.set(~value)
#             else:
#                 second_value = int(self.get_second_value(), 0)
#                 if op == "AND":
#                     self.result.set(value & second_value)
#                 elif op == "OR":
#                     self.result.set(value | second_value)
#                 elif op == "XOR":
#                     self.result.set(value ^ second_value)
#                 elif op == "NAND":
#                     self.result.set(~(value & second_value))
#                 elif op == "NOR":
#                     self.result.set(~(value | second_value))
#         except ValueError:
#             self.result.set("Error")

#     def get_second_value(self):
#         return tk.simpledialog.askstring("Input", "Enter second value:")

#     def append_to_display(self, value):
#         if self.result.get() == "0" or self.last_operation == "=":
#             self.result.set(value)
#         else:
#             self.result.set(self.result.get() + value)
#         self.last_operation = value

#     def arithmetic_operation(self, operator):
#         self.result.set(self.result.get() + operator)
#         self.last_operation = operator

#     def clear_display(self):
#         self.result.set("0")

#     def scientific_operation(self, op):
#         try:
#             value = float(self.result.get())
#             if op == "sin":
#                 self.result.set(sin(radians(value)))
#             elif op == "cos":
#                 self.result.set(cos(radians(value)))
#             elif op == "tan":
#                 self.result.set(tan(radians(value)))
#             elif op == "exp":
#                 self.result.set(exp(value))
#             elif op == "log":
#                 self.result.set(log(value))
#         except ValueError:
#             self.result.set("Error")

#     def evaluate_expression(self):
#         try:
#             self.result.set(eval(self.result.get()))
#         except Exception as e:
#             self.result.set("Error")
#         self.last_operation = "="

# if __name__ == "__main__":
#     root = tk.Tk()
#     calculator = ProgrammerCalculator(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk, Menu
# from math import sin, cos, tan, exp, log, pi, radians

# class ProgrammerCalculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Programmer's Calculator")
#         self.mode = tk.StringVar(value="Programmer")
#         self.result = tk.StringVar(value="0")
#         self.create_widgets()
#         self.last_operation = None

#     def create_widgets(self):
#         # Menu for Bitwise Operations
#         menubar = Menu(self.root)
#         bitwise_menu = Menu(menubar, tearoff=0)
#         bitwise_menu.add_command(label="AND", command=lambda: self.bitwise_operation("AND"))
#         bitwise_menu.add_command(label="NAND", command=lambda: self.bitwise_operation("NAND"))
#         bitwise_menu.add_command(label="OR", command=lambda: self.bitwise_operation("OR"))
#         bitwise_menu.add_command(label="XOR", command=lambda: self.bitwise_operation("XOR"))
#         bitwise_menu.add_command(label="NOT", command=lambda: self.bitwise_operation("NOT"))
#         bitwise_menu.add_command(label="NOR", command=lambda: self.bitwise_operation("NOR"))
#         menubar.add_cascade(label="Bitwise Operations", menu=bitwise_menu)
#         self.root.config(menu=menubar)

#         # Mode Switch
#         mode_frame = tk.Frame(self.root)
#         mode_frame.pack(side=tk.TOP, fill=tk.X)
#         ttk.Button(mode_frame, text="Programmer", command=lambda: self.switch_mode("Programmer")).pack(side=tk.LEFT)
#         ttk.Button(mode_frame, text="Scientific", command=lambda: self.switch_mode("Scientific")).pack(side=tk.LEFT)

#         # Display
#         display = ttk.Entry(self.root, textvariable=self.result, font=("Arial", 24), justify="right")
#         display.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

#         # Buttons Frame
#         self.buttons_frame = tk.Frame(self.root)
#         self.buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         self.create_prog_buttons()

#     def switch_mode(self, mode):
#         self.mode.set(mode)
#         for widget in self.buttons_frame.winfo_children():
#             widget.destroy()
#         if mode == "Programmer":
#             self.create_prog_buttons()
#         else:
#             self.create_sci_buttons()

#     def create_prog_buttons(self):
#         buttons = [
#             ("Hex", self.hex_convert), ("Dec", self.dec_convert), ("Oct", self.oct_convert), ("Bin", self.bin_convert),
#             ("<<", self.left_shift), (">>", self.right_shift),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]
#         for text, command in buttons:
#             button = ttk.Button(self.buttons_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def create_sci_buttons(self):
#         buttons = [
#             ("sin", lambda: self.scientific_operation("sin")), ("cos", lambda: self.scientific_operation("cos")),
#             ("tan", lambda: self.scientific_operation("tan")), ("exp", lambda: self.scientific_operation("exp")),
#             ("log", lambda: self.scientific_operation("log")), ("pi", lambda: self.append_to_display(str(pi))),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]
#         for text, command in buttons:
#             button = ttk.Button(self.buttons_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def hex_convert(self):
#         self.result.set(hex(int(self.result.get(), 0)))

#     def dec_convert(self):
#         self.result.set(int(self.result.get(), 0))

#     def oct_convert(self):
#         self.result.set(oct(int(self.result.get(), 0)))

#     def bin_convert(self):
#         self.result.set(bin(int(self.result.get(), 0)))

#     def left_shift(self):
#         self.result.set(int(self.result.get(), 0) << 1)

#     def right_shift(self):
#         self.result.set(int(self.result.get(), 0) >> 1)

#     def bitwise_operation(self, op):
#         try:
#             value = int(self.result.get(), 0)
#             if op == "NOT":
#                 self.result.set(~value)
#             else:
#                 second_value = int(self.get_second_value(), 0)
#                 if op == "AND":
#                     self.result.set(value & second_value)
#                 elif op == "OR":
#                     self.result.set(value | second_value)
#                 elif op == "XOR":
#                     self.result.set(value ^ second_value)
#                 elif op == "NAND":
#                     self.result.set(~(value & second_value))
#                 elif op == "NOR":
#                     self.result.set(~(value | second_value))
#         except ValueError:
#             self.result.set("Error")

#     def get_second_value(self):
#         return simpledialog.askstring("Input", "Enter second value:")

#     def append_to_display(self, value):
#         if self.result.get() == "0" or self.last_operation == "=":
#             self.result.set(value)
#         else:
#             self.result.set(self.result.get() + value)
#         self.last_operation = value

#     def arithmetic_operation(self, operator):
#         self.result.set(self.result.get() + operator)
#         self.last_operation = operator

#     def clear_display(self):
#         self.result.set("0")

#     def scientific_operation(self, op):
#         try:
#             value = float(self.result.get())
#             if op == "sin":
#                 self.result.set(sin(radians(value)))
#             elif op == "cos":
#                 self.result.set(cos(radians(value)))
#             elif op == "tan":
#                 self.result.set(tan(radians(value)))
#             elif op == "exp":
#                 self.result.set(exp(value))
#             elif op == "log":
#                 self.result.set(log(value))
#         except ValueError:
#             self.result.set("Error")

#     def evaluate_expression(self):
#         try:
#             self.result.set(eval(self.result.get()))
#         except Exception as e:
#             self.result.set("Error")
#         self.last_operation = "="

# if __name__ == "__main__":
#     root = tk.Tk()
#     calculator = ProgrammerCalculator(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import simpledialog
# from math import sin, cos, tan, exp, log, pi, radians

# class Calculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Powerful Programmer's Calculator")

#         self.mode = tk.StringVar(value="Programmer")
#         self.result = tk.StringVar(value="0")

#         self.create_widgets()
#         self.last_operation = None

#     def create_widgets(self):
#         # Mode Switch
#         mode_frame = tk.Frame(self.root)
#         mode_frame.pack(side=tk.TOP, fill=tk.X)
#         ttk.Button(mode_frame, text="Programmer", command=lambda: self.switch_mode("Programmer")).pack(side=tk.LEFT)
#         ttk.Button(mode_frame, text="Scientific", command=lambda: self.switch_mode("Scientific")).pack(side=tk.LEFT)

#         # Display
#         display = ttk.Entry(self.root, textvariable=self.result, font=("Arial", 24), justify="right")
#         display.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

#         # Programmer mode widgets
#         self.prog_frame = tk.Frame(self.root)
#         self.prog_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         self.create_prog_buttons()

#         # Scientific mode widgets
#         self.sci_frame = tk.Frame(self.root)

#         self.create_sci_buttons()

#     def switch_mode(self, mode):
#         self.mode.set(mode)
#         if mode == "Programmer":
#             self.sci_frame.pack_forget()
#             self.prog_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         else:
#             self.prog_frame.pack_forget()
#             self.sci_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#     def create_prog_buttons(self):
#         # Programmer Buttons
#         buttons = [
#             ("Hex", self.hex_convert), ("Dec", self.dec_convert), ("Oct", self.oct_convert), ("Bin", self.bin_convert),
#             ("<<", self.left_shift), (">>", self.right_shift),
#             ("AND", lambda: self.bitwise_operation("AND")), ("OR", lambda: self.bitwise_operation("OR")),
#             ("XOR", lambda: self.bitwise_operation("XOR")), ("NOT", lambda: self.bitwise_operation("NOT")),
#             ("NAND", lambda: self.bitwise_operation("NAND")), ("NOR", lambda: self.bitwise_operation("NOR")),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]

#         for text, command in buttons:
#             button = ttk.Button(self.prog_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def create_sci_buttons(self):
#         # Scientific Buttons
#         buttons = [
#             ("sin", lambda: self.scientific_operation("sin")), ("cos", lambda: self.scientific_operation("cos")),
#             ("tan", lambda: self.scientific_operation("tan")), ("exp", lambda: self.scientific_operation("exp")),
#             ("log", lambda: self.scientific_operation("log")), ("pi", lambda: self.append_to_display(str(pi))),
#             ("C", self.clear_display), ("(", lambda: self.append_to_display("(")), (")", lambda: self.append_to_display(")")),
#             ("+", lambda: self.arithmetic_operation("+")), ("-", lambda: self.arithmetic_operation("-")),
#             ("*", lambda: self.arithmetic_operation("*")), ("/", lambda: self.arithmetic_operation("/")),
#             ("%", lambda: self.arithmetic_operation("%")), (".", lambda: self.append_to_display(".")),
#             ("0", lambda: self.append_to_display("0")), ("1", lambda: self.append_to_display("1")),
#             ("2", lambda: self.append_to_display("2")), ("3", lambda: self.append_to_display("3")),
#             ("4", lambda: self.append_to_display("4")), ("5", lambda: self.append_to_display("5")),
#             ("6", lambda: self.append_to_display("6")), ("7", lambda: self.append_to_display("7")),
#             ("8", lambda: self.append_to_display("8")), ("9", lambda: self.append_to_display("9")),
#             ("=", self.evaluate_expression)
#         ]

#         for text, command in buttons:
#             button = ttk.Button(self.sci_frame, text=text, command=command)
#             button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

#     def hex_convert(self):
#         self.result.set(hex(int(self.result.get(), 0)))

#     def dec_convert(self):
#         self.result.set(int(self.result.get(), 0))

#     def oct_convert(self):
#         self.result.set(oct(int(self.result.get(), 0)))

#     def bin_convert(self):
#         self.result.set(bin(int(self.result.get(), 0)))

#     def left_shift(self):
#         self.result.set(int(self.result.get(), 0) << 1)

#     def right_shift(self):
#         self.result.set(int(self.result.get(), 0) >> 1)

#     def bitwise_operation(self, op):
#         try:
#             value = int(self.result.get(), 0)
#             if op == "NOT":
#                 self.result.set(~value)
#             else:
#                 second_value = int(self.get_second_value(), 0)
#                 if op == "AND":
#                     self.result.set(value & second_value)
#                 elif op == "OR":
#                     self.result.set(value | second_value)
#                 elif op == "XOR":
#                     self.result.set(value ^ second_value)
#                 elif op == "NAND":
#                     self.result.set(~(value & second_value))
#                 elif op == "NOR":
#                     self.result.set(~(value | second_value))
#         except ValueError:
#             self.result.set("Error")

#     def get_second_value(self):
#         return simpledialog.askstring("Input", "Enter second value:")

#     def append_to_display(self, value):
#         if self.result.get() == "0" or self.last_operation == "=":
#             self.result.set(value)
#         else:
#             self.result.set(self.result.get() + value)
#         self.last_operation = value

#     def arithmetic_operation(self, operator):
#         self.result.set(self.result.get() + operator)
#         self.last_operation = operator

#     def clear_display(self):
#         self.result.set("0")

#     def scientific_operation(self, op):
#         try:
#             value = float(self.result.get())
#             if op == "sin":
#                 self.result.set(sin(radians(value)))
#             elif op == "cos":
#                 self.result.set(cos(radians(value)))
#             elif op == "tan":
#                 self.result.set(tan(radians(value)))
#             elif op == "exp":
#                 self.result.set(exp(value))
#             elif op == "log":
#                 self.result.set(log(value))
#         except ValueError:
#             self.result.set("Error")

#     def evaluate_expression(self):
#         try:
#             self.result.set(eval(self.result.get()))
#         except Exception as e:
#             self.result.set("Error")
#         self.last_operation = "="

# if __name__ == "__main__":
#     root = tk.Tk()
#     calculator = Calculator(root)
#     root.mainloop()
