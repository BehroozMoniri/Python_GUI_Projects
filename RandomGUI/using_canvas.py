from tkinter import *

# root = Tk()
# root.geometry("500x500")

# my_canvas = Canvas(root, width=500, height=500, bg="white")
# my_canvas.grid(row=0, column=0)

# my_canvas.create_arc(100, 100, 300, 350 ) # , fill="blue"
# my_canvas.create_bitmap(1,2)
# my_canvas.create_image( )
# my_canvas.create_line()
# my_canvas.create_polygon()
# my_canvas.create_oval()


# my_canvas.create_rectangle(100, 100, 300, 350, fill="blue")

# my_canvas.create_oval(100, 100, 300, 350 , fill="cyan")
# my_canvas.create_arc(100, 100, 300, 350 , fill="pink")
# my_canvas.create_line(100, 100, 300, 350, fill="red", width=5)
# root.mainloop()


from tkinter import *

canvas_width = 300
canvas_height =80

master = Tk()
canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
nsteps = len(bitmaps)
step_x = int(canvas_width / nsteps)

for i in range(0, nsteps):
   canvas.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])

mainloop()
 

