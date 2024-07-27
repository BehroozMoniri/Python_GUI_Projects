
import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image
import os
import random
import numpy as np
import tkinter as tk
# Function
def image_to_tiles(im, tile_size = 9):
    """
    Function that splits an image into tiles
    :param im: image: image path
    :param tile_size: width in pixels of a tile
    :return tiles:
    """
    image = Image.open(im)
        
    w = image.width
    h = image.height
    
    row_count = np.int64((h-h%tile_size)/tile_size)
    col_count = np.int64((w-w%tile_size)/tile_size)
    
    n_slices = np.int64(row_count*col_count)
    
    # Image info
    print(f'Image: {im}')
    print(f'Dimensions: w:{w} h:{h}')
    print(f'Tile count: {n_slices}')


    r = np.linspace(0, w, row_count+1)
    r_tuples = [(np.int64(r[i]), np.int64(r[i])+tile_size) for i in range(0, len(r)-1)]
    q = np.linspace(0, h, col_count+1)
    q_tuples = [(np.int64(q[i]), np.int64(q[i])+tile_size) for i in range(0, len(q)-1)]
    
    #print(f'r_tuples:{r_tuples}\n\nq_tuples:{q_tuples}\n')
    
    tiles = []
    for row in range(row_count):
        for column in range(col_count):
            [y1, y2, x1, x2] = *r_tuples[row], *q_tuples[column]
            x2 = x1+tile_size
            y2 = y1+tile_size
            tile_image = image.crop((x1,y1,x2,y2))
            tile_coords = {'x1':x1,'y1':y1,'x2':x2,'y2':y2}
            tiles.append({'image':tile_image,'coords':tile_coords})

    return tiles

# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
 
    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((300, 300))
        pic = ImageTk.PhotoImage(img)
 
       # tiles = image_to_tiles(path)
       # corners = [(0,0) , (200,0), (400,0), (0,200), (200, 200), (400, 200), (400, 400)]
        # for i in range(20):
        #     tile = random.choice(tiles)
        #     tile['image'].show()

        # re-sizing the app window in order to fit picture
        # and buttom
        app.geometry("760x600")
        label.config(image=pic)
        label.image = pic
 
    # if no file is selected, then we are displaying below message
    else:
        print("No file is chosen !! Please choose a file.")

# Main method
if __name__ == "__main__":
 
    # defining tkinter object
    app = tk.Tk()
 
    # setting title and basic size to our App
    app.title("My Image Viewer")
    app.geometry("560x270")
 
    # adding background image
    # img = ImageTk.PhotoImage(file='bird.jpeg')
    # imgLabel = Label(app, image=img)
    # imgLabel.place(x=0, y=0)
 
    # adding background color to our upload button
    app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "lightgreen")
 
    label = tk.Label(app)
    label.pack(pady=10)
 
    # defining our upload buttom
    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)
 
    app.mainloop()    

