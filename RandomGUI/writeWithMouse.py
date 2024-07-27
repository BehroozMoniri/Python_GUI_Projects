from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

canvas_width = 500
canvas_height = 500

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   C.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
C = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
C.pack(expand = YES, fill = BOTH)
C.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
# eps = C.postscript(colormode='color')

# # Save canvas as "in-memory" EPS and pass to PIL without writing to disk
# im = Image.open(BytesIO(bytes(eps,'ascii')))
# im.save('result.png')

mainloop()
 
 

# root = Tk()
# cv = Canvas(root)
# cv.create_rectangle(10,10,50,50, fill='green')
# cv.pack()

# cv.update()
# Get the EPS corresponding to the canvas


 

# from tkinter import *
# from PIL import Image
# import webcolors

# drawing = False

# def findobjat(x,y,C):
#     obj = C.find_overlapping(x,y,x,y)
    
#     if len(obj) == 0:
#         return (255,255,255)
    
#     color = C.itemcget(obj[-1],"fill")

#     if type(color) == str:
#         color = webcolors.name_to_rgb(color)

#     return color

# def save(C,w,h):
#     im = Image.new("RGB",(w,h))
#     for x in range(w):
#         for y in range(h):
#             color = findobjat(x,y,C)
#             im.putpixel((x,y),color)
#     return im

# def postsave():
#     save(C,canvas_width,canvas_height).save("image.png")
    
# def drawstart(event):
#     global drawing
#     drawing = True

# def drawstop(event):
#     global drawing
#     drawing = False

# def draw(event):
#     if drawing:
#         C.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill = "black")

 
 
# C.bind("<Button-1>",drawstart)
# C.bind("<ButtonRelease-1>",drawstop)
# C.bind("<B1-Motion>",draw)

# button = Button(master,text = "Save image",command = postsave)
# button.pack()

# C.pack()
# master.mainloop()

