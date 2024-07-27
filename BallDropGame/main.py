from tkinter import *
from tkinter import colorchooser, messagebox
import tkinter as tk
import random, math  , time
from collections import deque 
 
# max_list_size=8
# colours = ["green","pink", "blue", "yellow", "orange"]
# deque1 = deque()
# deques = { "deque"+str(i+1): deque() for i in range(5)}

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=400, height=400, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.title("Ball Drop Game")
        #self.iconbitmap("./redketchup/favicon.svg")
        #self.iconbitmap('./ionos/favicon')  # \\
        self.moves = 0
        self.start_time = None
        self.best_time = None
        self.geometry("225x320")
        self.rows = 100
        self.columns = 100
        self.col_deq = deque()
        self.column =1
        self.cellwidth = 35
        self.cellheight = 35
        self.move_successful = False
        self.won = False
        self.color_button = tk.Button(self.canvas, text="Pick Background Color", command=self.pick_color)
        self.color_button.pack(side=tk.BOTTOM)
        #self.keepchecking = True     
        self.colours = ["lime","red", "blue", "yellow", "orange"]*7
        self.deques = { "deque"+str(i+1): deque() for i in range(6)}
        random.shuffle(self.colours) 
        self.winner_deques =  {'deque1': deque(['yellow']*6), 
                               'deque2': deque(['blue']*6), 
                               'deque3': deque(['lime']*6), 
                               'deque4': deque([ 'orange']*6), 
                               'deque5': deque(['red']*6),
                            'deque6': deque([]*6)}
        #print("self.winner_deques: ",self.winner_deques)
        #print("random.sample(self.colours,2 ) ", random.sample(self.colours,1 ) )
        self.colours += random.sample(self.colours,1 )
        self.i = 0
        for j in range(6):
            for i in range(6):
                self.deques[f"deque{j+1}"].appendleft( self.colours [self.i])
                self.i += 1
        #print(self.deques)
        self.rect = {}
        self.oval = {}
        myMenu = Menu(self)
        self.config(menu=myMenu)
        fileMenu=Menu(myMenu)
        myMenu.add_cascade(label="Options", menu=fileMenu)
        fileMenu.add_command(label="New Game", command=self.reset)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.close)
        self.start_time = time.time()
        self.root = tk.Tk()

    def drawboard(self ):
        for column in range(6):
            for row in range(8):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                #self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill=self.deques["deque"+str(column+1)][row], tags="oval")
    def placeballs(self ):
        for column in range(6):
            for row in range(-1*len(self.deques["deque"+str(column+1)] ),0,1):

                x1 = column*self.cellwidth
                y1 = (row+8)* self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.oval[row,column] = self.canvas.create_oval(x2-2,y2-2,x1+2,y1+2, fill=self.deques["deque"+str(column+1)][row], tags="oval")


    def make_a_move(self, from_deq, to_deq):
        try:
            if (len(self.deques["deque"+str(to_deq )]) <8) and (len(self.deques["deque"+str(from_deq )])>0):
                color = self.deques["deque"+str(from_deq )].popleft()
                self.deques["deque"+str(to_deq )].appendleft(color)
                self.move_successful = True
                self.col_deq = deque()
                self.moves += 1
                return self.move_successful  

        except KeyError:
            print("You clicked outside the allowed area!")
            pass #return self.move_successful  
        finally:

            self.move_successful = False
            self.drawboard()
            self.placeballs( )
            return self.move_successful  

    def check_win(self):
        long_list = []
        for column in range(6):
            short_list = []
            for row in range( len(self.deques["deque"+str(column+1)] )-1 ):
                first = self.deques["deque"+str(column+1)][0]
                if (first == self.deques["deque"+str(column+1)][row+1]):    
                    short_list.append(True)
                else:
                    short_list.append(False)
                if all(short_list):
                    long_list.append(True)
                else:
                    long_list.append(False)

        if all(long_list):
            self.won = True
            self.root.title("You have finished it!")
            self.root.geometry("315x100")
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if self.best_time is None or elapsed_time < self.best_time:
                self.best_time = elapsed_time
            message = f"\nYou solved the puzzle in {self.moves} moves and {elapsed_time:.2f} seconds!"
            #messagebox.showinfo("Congratulations!", message=message )
            if self.best_time:
                message += f"\nYour fastest time is {self.best_time:.2f} seconds!"
                messagebox.showinfo("Best Time", message)
            #self.drop_confetti()
            print("Congrats!")
            final_frame = Frame(self.root, width=800, height=800, bg="white", bd=5)
            again_button = Button(self.root, text="Play again" ,command=self.reset)
            again_button.pack(side = TOP)
            close_button = Button(self.root, text="Close" ,command=self.root.quit)
            close_button.pack( side = TOP)
            myLabel = Label(final_frame, text= message ).pack()   
            if self.best_time:
                messagebox.showinfo("Best Time", f"Your fastest time is {self.best_time:.2f} seconds!")
            final_frame.pack(fill="both", expand=1) 
           # self.keepchecking = False
        # while (not self.won):
        #     time.sleep(2.5)
        #     print("2.5 seconds has passed, still check_won?", (not self.won))
        #     #self.deques = self.winner_deques
        #     self.check_win()
        #    
                #break
    def select_a_col(self, event):
        #print(f"x corrodinate {event.x} and y-coord {event.y}")
        self.column = math.ceil(event.x/35)
        row = 9 - math.ceil(event.y/35)
        #print(f"row {row} and col {self.column}")
        self.col_deq.appendleft(self.column)
        if len(self.col_deq)==2:
            #print(self.col_deq)
            #print("going to Check for Win")
            self.check_win()
            #print("Finished Checking for Win")
            success = self.make_a_move( from_deq=self.col_deq[1],to_deq= self.col_deq[0])
            if success:
                self.col_deq = deque()
            else:
                self.col_deq.rotate()
                if (len(self.col_deq)>0):
                    self.col_deq.popleft()

    def reset(self):
        self.destroy()
        self.root.destroy()
        app = App()
        app.drawboard()
        app.placeballs()
        app.bind("<Button-1>" ,  app.select_a_col)
        app.check_win() 
        app.mainloop() 

    def close(self   ):
        if self.root:
            self.root.quit()
            #self.root.destroy()
        self.quit()
    
    def pick_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.canvas.config(bg=color)

        
if __name__=="__main__":
    #main()
    app = App()
    app.drawboard()
    app.placeballs()
    app.bind("<Button-1>" ,  app.select_a_col)
    app.check_win() 
    app.mainloop() 
 




