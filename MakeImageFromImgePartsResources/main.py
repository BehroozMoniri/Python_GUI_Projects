from tkinter import Label , Button, Frame, StringVar, PhotoImage
import tkinter as tk
import random, math, pygame, os 
from pathlib import Path
from collections import OrderedDict
mainwindow = tk.Tk()
mainwindow.title("Make Image Game")
coordinates_needed_to_win = OrderedDict()
directory = r"C:\Users\Behrooz Moniri\Documents\Programming\Python Projects\Tkinter\pythonProject2\FlyingBird\images"
cwd = Path(__file__).resolve() # os.getcwd()
#print(cwd)
print(Path(__file__).resolve().parent)
music_path = os.path.join( Path(__file__).resolve().parent,  'bensound-memories.mp3')
arranged_image_count = 0
img_obj_list = []
lbl_obj_list = []
image_index_list = [0,1,2,3,4,5,6,7,8]
pygame.mixer.init()
pygame.mixer.music.load( music_path)

coordinate_of_all_images = [(0,0), (200,0), (400,0),
                            (0,200), (200,200), (400,200),
                            (0,400), (200,400), (400,400),]
for i in range(9):
    img_obj_list.append(PhotoImage(file=os.path.join( Path(__file__).resolve().parent, 'image_part_00'+str(i+1)+'.png')))

frame = Frame(mainwindow, relief='sunken', bd=1)
frame.pack(fill='both', expand=True, padx=10, pady=10)

def pick_up_obj(event):
    wid = event.widget
    wid.startX = event.x
    wid.startY= event.y

def drag_motion(event):
    wid = event.widget
    x_position = wid.winfo_x() - wid.startX + event.x
    y_position = wid.winfo_y() - wid.startY + event.y
    wid.place(x=x_position, y = y_position)

def play_btn_handler():
    global lbl_obj_list, image_index_list
    print(random.randrange(len(image_index_list)))
    for i in range(9):
        image_index = image_index_list.pop(random.randrange(len(image_index_list)))
        lbl_obj_list[i][0].config(image=img_obj_list[image_index])
        coordinates_needed_to_win[i] = coordinate_of_all_images[image_index] # str(i)

    arranged_count_str.set('Lets arrange now!')
    # image_index_list = [i for i in range(9)]
    for i in range(9):
        lbl_obj_list[i][0].config(state='normal')
    pygame.mixer.music.play()

def check_if_game_won(coordinate_of_current_image):
    global coordinates_needed_to_win , arranged_image_count

   # if len(arranged_image_count) >= 9:
    print("coordinates_needed_to_win.values()", coordinates_needed_to_win.values())
    coordinates_win_list = list(coordinates_needed_to_win.values())

    for i in range(9):
        x_value_desired = coordinates_win_list[i][0]
        y_value_desired = coordinates_win_list[i][1]
        x_current_value = coordinate_of_current_image[i][0]
        y_current_value = coordinate_of_current_image[i][1]

        x_set = math.isclose(x_value_desired, x_current_value, abs_tol =5)
        y_set = math.isclose(y_current_value,y_value_desired, abs_tol=5)

        if x_set and y_set:
            arranged_image_count += 1
            string = 'Arranged images ' +str(arranged_image_count) + '/9' 
            arranged_count_str.set(string)

        if arranged_image_count >= 9:
            string +=  '\n You Won! '
            arranged_count_str.set( string)
            pygame.mixer.music.stop()
            for i in range(9):
                lbl_obj_list[i][0].config(state='disabled')
                
def mouse_button_release(event):
    global lbl_obj_list, coordinate_of_all_images
    coordinate_of_current_image = []
    for i in range(9):
        x = lbl_obj_list[i][0].winfo_x()
        y = lbl_obj_list[i][0].winfo_y()
        coordinate_of_current_image.append((x, y))

    check_if_game_won(coordinate_of_current_image)

img_idx = 0
for r in range(3):
    for c in range(3):
        label_obj = Label(frame, width=200, height=200)
        label_obj.config(image=img_obj_list[img_idx])
        label_obj.bind('<Button-1>', pick_up_obj)
        label_obj.bind('<B1-Motion>', drag_motion)
        label_obj.bind('<ButtonRelease-1>', mouse_button_release)
        lbl_obj_list.append((label_obj,coordinate_of_all_images[img_idx]))
        img_idx +=1
        label_obj.grid(row=r, column=c)

arranged_count_str = StringVar()
arranged_count_str.set('Arranged Images: 9/9')
arranged_image_label = Label(mainwindow, textvariable=arranged_count_str, font=('Microsoft Himalaya', 20))
arranged_image_label.place(x=625, y=20)

play_button = Button(mainwindow, text='play', padx=30, pady=2,
                     font=('Microsoft Himalaya', 20),
                     command=play_btn_handler)
play_button.place(x=625, y=100)


mainwindow.geometry("820x700")
mainwindow.mainloop()