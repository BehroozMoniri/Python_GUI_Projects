import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import time

class SlidingPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sliding Puzzle Game")

        self.canvas_width = 900
        self.canvas_height = 600
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.best_time = float('inf')

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.show_image(self.original_image)

    def show_image(self, image):
        image = image.resize((self.canvas_height, self.canvas_height), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image((self.canvas_width - self.canvas_height) // 2, 0, anchor=tk.NW, image=self.tk_image)

    def start_game(self):
        self.tile_count = 9
        self.reset_game()
        self.tiles = self.create_tiles()
        self.shuffle_tiles()
        self.start_time = time.time()
        self.update_canvas()

    def reset_game(self):
        self.canvas.delete("all")
        self.tiles = []
        self.tile_positions = {}
        self.correct_positions = {}

    def create_tiles(self):
        image_width, image_height = self.original_image.size
        tile_width = image_width // 3
        tile_height = image_height // 3

        tiles = []
        for row in range(3):
            for col in range(3):
                box = (col * tile_width, row * tile_height, (col + 1) * tile_width, (row + 1) * tile_height)
                tile_image = self.original_image.crop(box)
                tile_image = tile_image.resize((tile_width, tile_height), Image.LANCZOS)
                tk_tile_image = ImageTk.PhotoImage(tile_image)
                tile_id = self.canvas.create_image(col * tile_width + (self.canvas_width - image_width) // 2, row * tile_height, anchor=tk.NW, image=tk_tile_image, tags="tile")
                self.tile_positions[tile_id] = (row, col)
                self.correct_positions[(row, col)] = tile_id
                tiles.append((tile_id, tk_tile_image))

        self.tile_width, self.tile_height = tile_width, tile_height
        return tiles

    def shuffle_tiles(self):
        positions = list(self.tile_positions.values())
        random.shuffle(positions)
        for tile_id, pos in zip(self.tile_positions.keys(), positions):
            self.tile_positions[tile_id] = pos

    def update_canvas(self):
        for tile_id, (row, col) in self.tile_positions.items():
            self.canvas.coords(tile_id, col * self.tile_width + (self.canvas_width - self.tile_width * 3) // 2, row * self.tile_height)

        self.canvas.tag_bind("tile", "<Button-1>", self.on_tile_click)
        self.canvas.tag_bind("tile", "<B1-Motion>", self.on_tile_drag)
        self.canvas.tag_bind("tile", "<ButtonRelease-1>", self.on_tile_release)

    def on_tile_click(self, event):
        self.selected_tile = self.canvas.find_closest(event.x, event.y)[0]
        self.start_x, self.start_y = event.x, event.y

    def on_tile_drag(self, event):
        dx, dy = event.x - self.start_x, event.y - self.start_y
        self.canvas.move(self.selected_tile, dx, dy)
        self.start_x, self.start_y = event.x, event.y

    def on_tile_release(self, event):
        new_x, new_y = self.canvas.coords(self.selected_tile)
        col = int((new_x - (self.canvas_width - self.tile_width * 3) // 2) // self.tile_width)
        row = int(new_y // self.tile_height)

        if 0 <= col < 3 and 0 <= row < 3:
            self.tile_positions[self.selected_tile] = (row, col)
            self.update_canvas()

        if self.check_win():
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if elapsed_time < self.best_time:
                self.best_time = elapsed_time
                messagebox.showinfo("Congratulations!", f"You completed the puzzle in {elapsed_time:.2f} seconds! New best time!")
            else:
                messagebox.showinfo("Congratulations!", f"You completed the puzzle in {elapsed_time:.2f} seconds!")
            self.reset_game()

    def check_win(self):
        for (row, col), tile_id in self.correct_positions.items():
            pos = self.tile_positions[tile_id]
            if abs(row - pos[0]) > 0.1 or abs(col - pos[1]) > 0.1:
                return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = SlidingPuzzleGame(root)
    root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk
# import random
# import time

# class SlidingPuzzleGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sliding Puzzle Game")
        
#         self.canvas = tk.Canvas(root, width=600, height=600)
#         self.canvas.pack()

#         self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
#         self.upload_button.pack()

#         self.tile_count_entry = tk.Entry(root)
#         self.tile_count_entry.pack()
#         self.tile_count_entry.insert(0, "Enter number of tiles")

#         self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
#         self.start_button.pack()

#         self.best_time = float('inf')

#     def upload_image(self):
#         self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
#         if self.image_path:
#             self.original_image = Image.open(self.image_path)
#             self.show_image(self.original_image)

#     def show_image(self, image):
#         image = image.thumbnail((600, 600), Image.Resampling.LANCZOS)
#         #image = image.resize((600, 600), Image.ANTIALIAS)
#         self.tk_image = ImageTk.PhotoImage(image)
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

#     def start_game(self):
#         try:
#             self.tile_count = int(self.tile_count_entry.get())
#             if not (self.tile_count ** 0.5).is_integer() and self.tile_count % 2 != 0:
#                 raise ValueError("Number of tiles must be an even number or a perfect square")
#         except ValueError as e:
#             messagebox.showerror("Invalid Input", str(e))
#             return
        
#         self.reset_game()
#         self.tiles = self.create_tiles()
#         self.shuffle_tiles()
#         self.start_time = time.time()
#         self.update_canvas()

#     def reset_game(self):
#         self.canvas.delete("all")
#         self.tiles = []
#         self.tile_positions = {}

#     def create_tiles(self):
#         image_width, image_height = self.original_image.size
#         tile_width = image_width // int(self.tile_count ** 0.5)
#         tile_height = image_height // int(self.tile_count ** 0.5)
        
#         tiles = []
#         for row in range(int(self.tile_count ** 0.5)):
#             for col in range(int(self.tile_count ** 0.5)):
#                 box = (col * tile_width, row * tile_height, (col + 1) * tile_width, (row + 1) * tile_height)
#                 tile_image = self.original_image.crop(box)
#                 tile_image = tile_image.thumbnail((tile_width, tile_height), Image.Resampling.LANCZOS)
#                 #tile_image = tile_image.resize((tile_width, tile_height), Image.ANTIALIAS)
#                 tk_tile_image = ImageTk.PhotoImage(tile_image)
#                 tile_id = self.canvas.create_image(col * tile_width, row * tile_height, anchor=tk.NW, image=tk_tile_image)
#                 self.tile_positions[tile_id] = (row, col)
#                 tiles.append((tile_id, tk_tile_image))
        
#         self.tile_width, self.tile_height = tile_width, tile_height
#         return tiles

#     def shuffle_tiles(self):
#         positions = list(self.tile_positions.values())
#         random.shuffle(positions)
#         for tile_id, pos in zip(self.tile_positions.keys(), positions):
#             self.tile_positions[tile_id] = pos

#     def update_canvas(self):
#         for tile_id, (row, col) in self.tile_positions.items():
#             self.canvas.coords(tile_id, col * self.tile_width, row * self.tile_height)
        
#         self.canvas.tag_bind("tile", "<Button-1>", self.on_tile_click)
#         self.canvas.tag_bind("tile", "<B1-Motion>", self.on_tile_drag)
#         self.canvas.tag_bind("tile", "<ButtonRelease-1>", self.on_tile_release)

#     def on_tile_click(self, event):
#         self.selected_tile = self.canvas.find_closest(event.x, event.y)[0]
#         self.start_x, self.start_y = event.x, event.y

#     def on_tile_drag(self, event):
#         dx, dy = event.x - self.start_x, event.y - self.start_y
#         self.canvas.move(self.selected_tile, dx, dy)
#         self.start_x, self.start_y = event.x, event.y

#     def on_tile_release(self, event):
#         new_x, new_y = self.canvas.coords(self.selected_tile)
#         col = int(new_x // self.tile_width)
#         row = int(new_y // self.tile_height)
#         self.tile_positions[self.selected_tile] = (row, col)
#         self.update_canvas()

#         if self.check_win():
#             end_time = time.time()
#             elapsed_time = end_time - self.start_time
#             if elapsed_time < self.best_time:
#                 self.best_time = elapsed_time
#                 messagebox.showinfo("Congratulations!", f"You completed the puzzle in {elapsed_time:.2f} seconds! New best time!")
#             else:
#                 messagebox.showinfo("Congratulations!", f"You completed the puzzle in {elapsed_time:.2f} seconds!")
#             self.reset_game()

#     def check_win(self):
#         for tile_id, (row, col) in self.tile_positions.items():
#             correct_row, correct_col = divmod(self.tiles.index((tile_id, self.canvas.itemcget(tile_id, "image"))), int(self.tile_count ** 0.5))
#             if row != correct_row or col != correct_col:
#                 return False
#         return True

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SlidingPuzzleGame(root)
#     root.mainloop()
