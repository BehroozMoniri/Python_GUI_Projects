import tkinter as tk
from tkinter import messagebox
import time
import random

class TowersOfHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Towers of Hanoi")
        
        self.moves = 0
        self.rods = {'A': [], 'B': [], 'C': []}
        self.selected_disk = None
        self.start_time = None
        self.best_time = None

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame, width=600, height=400)
        self.canvas.pack()

        self.label = tk.Label(self.frame, text="Enter number of disks:")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.frame)
        self.entry.pack(side=tk.LEFT)

        self.button = tk.Button(self.frame, text="Start Game", command=self.start_game)
        self.button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.frame, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.on_click)

    def start_game(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError

            self.reset_game()
            self.rods['A'] = list(range(n, 0, -1))
            self.draw_rods()
            self.moves = 0
            self.start_time = time.time()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a positive integer.")

    def on_click(self, event):
        rod = self.get_rod(event.x)
        
        if rod:
            if self.selected_disk is None:
                if self.rods[rod]:
                    self.selected_disk = (rod, self.rods[rod][-1])
            else:
                if self.move_disk(self.selected_disk[0], rod):
                    self.moves += 1
                    self.draw_rods()
                    self.selected_disk = None
                    self.check_win()

    def get_rod(self, x):
        if 50 <= x <= 150:
            return 'A'
        elif 250 <= x <= 350:
            return 'B'
        elif 450 <= x <= 550:
            return 'C'
        return None

    def move_disk(self, from_rod, to_rod):
        if not self.rods[from_rod]:
            return False
        disk = self.rods[from_rod][-1]
        if not self.rods[to_rod] or self.rods[to_rod][-1] > disk:
            self.rods[from_rod].pop()
            self.rods[to_rod].append(disk)
            return True
        return False

    def check_win(self):
        if len(self.rods['C']) == int(self.entry.get()):
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if self.best_time is None or elapsed_time < self.best_time:
                self.best_time = elapsed_time
            messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves} moves and {elapsed_time:.2f} seconds!")
            if self.best_time:
                messagebox.showinfo("Best Time", f"Your fastest time is {self.best_time:.2f} seconds!")
            self.drop_confetti()

    def draw_rods(self):
        self.canvas.delete("all")
        rod_positions = {'A': 100, 'B': 300, 'C': 500}
        rod_height = 300
        rod_width = 10

        for rod, x in rod_positions.items():
            self.canvas.create_rectangle(x - rod_width / 2, 50, x + rod_width / 2, rod_height)

            disks = self.rods[rod]
            disk_height = 20
            for i, disk in enumerate(disks):
                disk_width = 20 * disk
                self.canvas.create_rectangle(
                    x - disk_width / 2,
                    rod_height - (i + 1) * disk_height,
                    x + disk_width / 2,
                    rod_height - i * disk_height,
                    fill="blue"
                )

    def reset_game(self):
        self.moves = 0
        self.rods = {'A': [], 'B': [], 'C': []}
        self.selected_disk = None
        self.start_time = None
        self.canvas.delete("all")

    def drop_confetti(self):
        for _ in range(100):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
            self.canvas.create_oval(x, y, x+5, y+5, fill=color, outline=color)
        self.root.after(2000, self.reset_game)

if __name__ == "__main__":
    root = tk.Tk()
    app = TowersOfHanoi(root)
    root.mainloop()
