import turtle
from isPrime import IsPrime 
from squareSpiral import SquareSpiral
import tkinter as tk
import random
from itertools import count
from collections import namedtuple
from math import ceil, floor, log10, sqrt
def DrawSpiral(n):
    sc = turtle.Screen() 
    # setup the screen size 
    sc.setup(1200,750) 
    turtle.speed(120) 
    # size  
    n = 20
    SquareSpiral(20)
    # creating instance of turtle 
    pen = turtle.Turtle() 
    sum1 = 1
    # loop to draw a side 
    for i in range(1, n ): 
        sum1 +=  i
        if IsPrime(sum1):
            pen.pencolor('red')
        else:
            pen.pencolor('black')
        pen.write(sum1)
        pen.forward(sum1 ) 
        pen.right(90) 
        sum1 +=  i
        if IsPrime(sum1):
            pen.pencolor('red')
        else:
            pen.pencolor('black')
        pen.write(sum1)
        pen.forward(sum1 ) 
        pen.right(90) 
    # closing the instance 
    turtle.done() 

#DrawSpiral(n=10)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=1400, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.oval = {}
        for column in range(50):
            for row in range(50):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                #self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="blue", tags="oval")
    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="blue")
        self.canvas.itemconfig("oval", fill="blue")
        for i in range(10):
            row = random.randint(0,19)
            col = random.randint(0,19)
            item_id = self.oval[row,col]
            self.canvas.itemconfig(item_id, fill="green")
        self.after(delay, lambda: self.redraw(delay))



    def steps_from_center(self, n):
        self.max_i = n #= int(input("What number do you want to display up to? "))
                # how many digits in the largest number?
        max_i_width = int(floor(log10(self.max_i))) + 1

        # custom output formatter - make every item the same width
        def output(  item, format_string="{{:>{}}}".format( max_i_width)):
            return format_string.format(item)

        # how big does the square have to be?
        max_n = int(ceil(sqrt(self.max_i)))
        EMPTY = output("")
        # here is our initialized data structure
        self.square = [[EMPTY] * max_n*max_n for _ in range(max_n*max_n)]
        #print("self.square: ",self.square)
        # and we start by placing a 1 in the center:
        x = y = max_n // 2
        self.square[y][x] = output(1)

        Step  = namedtuple("Step", ["dx", "dy"])
        RIGHT = Step( 1,  0)
        DOWN  = Step( 0,  1)
        LEFT  = Step(-1,  0)
        UP    = Step( 0, -1)
        for n in count(start=1):
            if n % 2:
                yield RIGHT
                for i in range(n):
                    yield DOWN
                for i in range(n):
                    yield LEFT
            else:
                yield LEFT
                for i in range(n):
                    yield UP
                for i in range(n):
                    yield RIGHT

    def draw(self, n):
        self.max_i = n #= int(input("What number do you want to display up to? "))
                # how many digits in the largest number?
        max_i_width = int(floor(log10(self.max_i))) + 1

        # custom output formatter - make every item the same width
        def output(  item, format_string="{{:>{}}}".format( max_i_width)):
            return format_string.format(item)

        # how big does the square have to be?
        max_n = int(ceil(sqrt(self.max_i)))

        # and we start by placing a 1 in the center:
        x = y = max_n // 2
        #print("x, y", x, y)
        self.text("1", 260+x*25,260+y*25, fill="blue")
        for i, step in enumerate(self.steps_from_center(n), start=2):
            if i > self.max_i:
                break
            else:
                x += step.dx
                y += step.dy
                self.square[y][x] =  output(i)
                if IsPrime(i):
                    self.text( output(i), 260+x*25,260+y*25, fill="red")
                else:
                    self.text( output(i), 260+x*25,260+y*25)

        #print("\n".join(" ".join(row) for row in self.square))

    def text(self, text_, x ,y, fill='black' ):
        self.canvas.create_text(x,y , fill=fill  ,  font=('Helvetica 10 bold'),text=text_ )
        self.canvas.update

    def make_Scrollable(self):
        #from tkinter import filedialog as fd

        self.geometry("1400x800")
        # main
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # canvas
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # scrollbar
        my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind(
            '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
        )

        second_frame = tk.Frame(my_canvas, width = 1000, height = 100)
        btn1 = tk.Button(second_frame,
                        text="Browse...",
                        compound="left",
                        fg="blue", width=22,
                        font=("bold", 10),
                        height=1,
                        )

        btn1.place(x=600, y=0)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        

#if __name__ == "__main__":
app = App()
app.draw(1000)
app.make_Scrollable()

app.mainloop()    
