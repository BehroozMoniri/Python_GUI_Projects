from tkinter import *

root = Tk()
w = 500
h = 500
#global x 
x = w //2
#global y 
y = h // 2
root.geometry("500x500")
my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

global  my_circle
my_circle = my_canvas.create_oval(x,y, x+10, y +10)
my_label = Label(my_canvas, text= "")
my_label.pack( pady=20)

def move(e ):
    x = e.x
    y = e.y
    my_label.config(text= f"x-coordinate: {str(x)} and y-cordinate: { str(y)}")
    # img = PhotoImage(file=".\Chess\images\oldPieces\\n.png")
    #my_canvas.move(my_circle , x, y )
    #my_canvas.create_image(x, y, image=my_circle)
     
def left(event):
    x -= 10
    y = 0
    my_canvas.move(my_circle , x, y)

def right(event):
    x += 10
    y = 0
    my_canvas.move(my_circle , x, y)

def up(event):
    
    x = 0
    y -= 10
    my_canvas.move(my_circle , x, y)

def down(event):
    
    x = 0
    y += 10
    my_canvas.move(my_circle , x, y)

root.bind("<B1-Motion>", move)
root.bind("<Left>", left )
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()