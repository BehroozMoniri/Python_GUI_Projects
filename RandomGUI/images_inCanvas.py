from tkinter import *

canvas_width = 500
canvas_height =500

root = Tk()

canvas = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()
#global x
x = 20
#global y
y =  20
img = PhotoImage(file=".\Chess\images\oldPieces\\n.png")
canvas.create_image(x, y, anchor=NW, image=img)
circle = canvas.create_oval(10, 10, 20, 20)

def move(e ):
    x = e.x
    y = e.y
    global img
    my_label.config(text= f"x-coordinate: {str(x)} and y-cordinate: { str(y)}")
    img = PhotoImage(file=".\Chess\images\oldPieces\\n.png")
    canvas.create_image(x, y, image=img)
     
canvas.bind("<B1-Motion>", move)

my_label = Label(root, text= "")

my_label.pack( pady=20)

# def left(event  ):
#     x -= 10
#     y = 0
#     canvas.move(img , x, y)

# def right(event):
#     x += 10
#     y = 0
#     canvas.move(img , x, y)

# def up(event):
#     x = 0
#     y -= 10
#     canvas.move(img , x, y)

# def down(event):
#     x = 0
#     y += 10
#     canvas.move(img , x, y)

# root.bind("<Left>", left   )
# root.bind("<Right>", right)
# root.bind("<Up>", up)
# root.bind("<Down>", down)


mainloop()