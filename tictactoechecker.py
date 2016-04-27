# Tic-Tac-Toe: Checker // Felipe Viacava e Ricardo Bachega

# importing lybrarys to be used in this code
import tkinter as tk
from tkinter import messagebox
import tictactoegame
from tictactoegame import tictactoe

# creating the class that contains the checker's data
class checker:
    
    def __init__(self):
        self.window = tk.Tk() # creates the window
        self.game = tictactoe() # uses the class created in the other file
        self.window.title('Tic-Tac-Toe') # creating the title
        # now, we've come to the part of the code where we setup the window's and buttons's dimensions
        # first, lines and columns
        self.window.geometry("600x700+200+200")
        self.window.rowconfigure(0, weight = 3,minsize = 200)
        self.window.rowconfigure(1, weight = 3,minsize = 200)
        self.window.rowconfigure(2, weight = 3,minsize = 200)
        self.window.rowconfigure(3, weight = 1,minsize = 100)
        self.window.columnconfigure(0, weight = 3,minsize = 200)
        self.window.columnconfigure(1, weight = 3,minsize = 200)
        self.window.columnconfigure(2, weight = 3,minsize = 200)
        # now the buttons
        self.button1 = tk.Button(self.window)
        self.button2 = tk.Button(self.window)
        self.button3 = tk.Button(self.window)
        self.button4 = tk.Button(self.window)
        self.button5 = tk.Button(self.window)
        self.button6 = tk.Button(self.window)
        self.button7 = tk.Button(self.window)
        self.button8 = tk.Button(self.window)
        self.button9 = tk.Button(self.window)
        self.button1.grid(row = 0, column = 0, sticky="nsew")
        self.button2.grid(row = 0, column = 1, sticky="nsew")
        self.button3.grid(row = 0, column = 2, sticky="nsew")
        self.button4.grid(row = 1, column = 0, sticky="nsew")
        self.button5.grid(row = 1, column = 1, sticky="nsew")
        self.button6.grid(row = 1, column = 2, sticky="nsew")
        self.button7.grid(row = 2, column = 0, sticky="nsew")
        self.button8.grid(row = 2, column = 1, sticky="nsew")
        self.button9.grid(row = 2, column = 2, sticky="nsew")
        self.button1.configure(command = self.pressedbutton1)
        self.button2.configure(command = self.pressedbutton2)
        self.button3.configure(command = self.pressedbutton3)
        self.button4.configure(command = self.pressedbutton4)
        self.button5.configure(command = self.pressedbutton5)
        self.button6.configure(command = self.pressedbutton6)
        self.button7.configure(command = self.pressedbutton7)
        self.button8.configure(command = self.pressedbutton8)
        self.button9.configure(command = self.pressedbutton9)
        
        # and now the title and font        
        self.label = tk.Label(self.window)
        self.label.configure(text = "X's turn")
        self.label.configure(font="Impact 24")
        self.label.grid(row=3, column=0, columnspan=3, sticky="nsew")
    
    # function that runs the game
    def runsgame(self):
        self.window.mainloop()
        
    # function that cleans the checker so the players can play again
    def cleanschecker(self):
        self.game.cleansplay() # here we use the function that cleans the array created in the other file so the plays can restart
        self.button1.configure(state= "normal")
        self.button2.configure(state= "normal")
        self.button3.configure(state= "normal")
        self.button4.configure(state= "normal")
        self.button5.configure(state= "normal")
        self.button6.configure(state= "normal")
        self.button7.configure(state= "normal")
        self.button8.configure(state= "normal")
        self.button9.configure(state= "normal")
        self.button1.configure(text = "")
        self.button2.configure(text = "")
        self.button3.configure(text = "")
        self.button4.configure(text = "")
        self.button5.configure(text = "")
        self.button6.configure(text = "")
        self.button7.configure(text = "")
        self.button8.configure(text = "")
        self.button9.configure(text = "")
        
    # now that we have everything done with the checker's layout, it's time to program how it will respond as the game goes on
    def pressedbutton1(self):
        # the following lines setup what font the button will show and will disable it after it's been clicked on
        self.button1.configure(font = "Impact 16")
        self.button1.configure(state = "disabled")
        # and these ones get if the button has been clicked on and which player did it.
        # they also disable the button for future clicks and show which player did it by printing the correspondent character
        # after that, they change the play indicator so the next player knows it's his turn
        if self.game.click == True:
            self.button1.configure(text = "X")
            self.game.getsplay(0,0)
            self.label.configure(text = "O's turn")
        else:
            self.button1.configure(text = "O")
            self.game.getsplay(0,0)
            self.label.configure(text = "X's turn")
            
        # after we've got the play and printed the character on the button, it's time to check if
        # someone has won. if that's what happened, the code uses the other file's functions to find
        # the winning play and then pops up a text message saying who has won.
        # after that's done, the checker gets cleared up so it is possible to play again, starting
        # with the player who LOST
            
        winner = self.game.checkswinner()
        
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()
    
    # SO the rest of the code is the same thing as the past few lines, but applied to the other buttons
        
    def pressedbutton2(self):
        
        self.button2.configure(font = "Impact 16")
        self.button2.configure(state = "disabled")
        
        if self.game.click == True:
            self.button2.configure(text = "X")
            self.game.getsplay(0,1)
            self.label.configure(text = "O's turn")
        else:
            self.button2.configure(text = "O")
            self.game.getsplay(0,1)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()

    def pressedbutton3(self):
        
        self.button3.configure(font = "Impact 16")
        self.button3.configure(state = "disabled")
        
        if self.game.click == True:
            self.button3.configure(text = "X")
            self.game.getsplay(0,2)
            self.label.configure(text = "O's turn")
        else:
            self.button3.configure(text = "O")
            self.game.getsplay(0,2)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()
        
    def pressedbutton4(self):
        
        self.button4.configure(font = "Impact 16")
        self.button4.configure(state = "disabled")
        
        if self.game.click == True:
            self.button4.configure(text = "X")
            self.game.getsplay(1,0)
            self.label.configure(text = "O's turn")
        else:
            self.button4.configure(text = "O")
            self.game.getsplay(1,0)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()

    def pressedbutton5(self):
        
        self.button5.configure(font = "Impact 16")
        self.button5.configure(state = "disabled")
        
        if self.game.click == True:
            self.button5.configure(text = "X")
            self.game.getsplay(1,1)
            self.label.configure(text = "O's turn")
        else:
            self.button5.configure(text = "O")
            self.game.getsplay(1,1)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()
            
    def pressedbutton6(self):
        
        self.button6.configure(font = "Impact 16")
        self.button6.configure(state = "disabled")
        
        if self.game.click == True:
            self.button6.configure(text = "X")
            self.game.getsplay(1,2)
            self.label.configure(text = "O's turn")
        else:
            self.button6.configure(text = "O")
            self.game.getsplay(1,2)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()


    def pressedbutton7(self):
        
        self.button7.configure(font = "Impact 16")
        self.button7.configure(state = "disabled")
        
        if self.game.click == True:
            self.button7.configure(text = "X")
            self.game.getsplay(2,0)
            self.label.configure(text = "O's turn")
        else:
            self.button7.configure(text = "O")
            self.game.getsplay(2,0)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()

    def pressedbutton8(self):
        
        self.button8.configure(font = "Impact 16")
        self.button8.configure(state = "disabled")
        
        if self.game.click == True:
            self.button8.configure(text = "X")
            self.game.getsplay(2,1)
            self.label.configure(text = "O's turn")
        else:
            self.button8.configure(text = "O")
            self.game.getsplay(2,1)
            self.label.configure(text = "X's turn")
        
        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()
            
    def pressedbutton9(self):
        
        self.button9.configure(font = "Impact 16")
        self.button9.configure(state = "disabled")
        
        if self.game.click == True:
            self.button9.configure(text = "X")
            self.game.getsplay(2,2)
            self.label.configure(text = "O's turn")
        else:
            self.button9.configure(text = "O")
            self.game.getsplay(2,2)
            self.label.configure(text = "X's turn")

        winner = self.game.checkswinner()
        if winner == 1:
            tk.messagebox.showinfo('Winner', 'X wins!')
            self.cleanschecker()
        elif winner == 2:
            tk.messagebox.showinfo ('Winner', 'O wins!')
            self.cleanschecker()
        elif winner == -1:
            tk.messagebox.showinfo ('Winner', "It's a draw!")
            self.cleanschecker()
            
# and now we can successfuly run the game :)
        
checker = checker()
checker.runsgame()

# THAT'S IT BABY