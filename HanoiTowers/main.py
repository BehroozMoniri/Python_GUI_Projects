# def towers_of_hanoi(n, source, target, auxiliary):
#     """
#     Solve the Towers of Hanoi puzzle.

#     :param n: Number of disks
#     :param source: The source rod
#     :param target: The target rod
#     :param auxiliary: The auxiliary rod
#     """
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return

#     towers_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     towers_of_hanoi(n - 1, auxiliary, target, source)

# def play_towers_of_hanoi():
#     """
#     Play the Towers of Hanoi game.
#     """
#     print("Welcome to the Towers of Hanoi game!")
#     try:
#         n = int(input("Enter the number of disks: "))
#         if n <= 0:
#             print("Number of disks must be a positive integer.")
#             return
        
#         print(f"Solving the Towers of Hanoi puzzle for {n} disks:")
#         towers_of_hanoi(n, 'A', 'C', 'B')
#     except ValueError:
#         print("Invalid input! Please enter a positive integer.")

# # Run the game
# if __name__ == "__main__":
#     play_towers_of_hanoi()
import tkinter as tk
from tkinter import messagebox

class TowersOfHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Towers of Hanoi")

        self.moves = []
        self.rods = {'A': [], 'B': [], 'C': []}

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

    def start_game(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError

            self.reset_game()
            self.rods['A'] = list(range(n, 0, -1))
            self.draw_rods()
            self.moves = []
            self.solve_hanoi(n, 'A', 'C', 'B')
            self.animate_moves()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a positive integer.")

    def solve_hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.moves.append((source, target))
            return

        self.solve_hanoi(n - 1, source, auxiliary, target)
        self.moves.append((source, target))
        self.solve_hanoi(n - 1, auxiliary, target, source)

    def animate_moves(self):
        if not self.moves:
            return

        move = self.moves.pop(0)
        disk = self.rods[move[0]].pop()
        self.rods[move[1]].append(disk)
        self.draw_rods()
        self.root.after(500, self.animate_moves)

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
        self.moves = []
        self.rods = {'A': [], 'B': [], 'C': []}
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = TowersOfHanoi(root)
    root.mainloop()