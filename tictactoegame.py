# Tic-Tac-Toe: Plays // Felipe Viacava e Ricardo Bachega

# here we import the lybrary used for arrays
import numpy as np

# then we create a class for the game
class tictactoe:
    #then we setup the clicks as True and create an array that represents our checker
    def __init__(self):
        self.click = True
        self.button = np.zeros([3,3])
        
    # the following functions determine which player pressed the button and set them as 1 or 2 according to the players character                
    def getsplay(self, row, column):
        button = self.button
        if self.click == True:
            button[row][column] = 1
            #then, the click changes either to false or true again so the 1 or 2 method is valid
            self.click = False 
        else:
            button[row][column] = 2
            self.click = True
            
    # now, the tricky part. the next lines determine that if a full row, column or diagonal was completed and
    # if so, returns either 1, 2 or -1, that will be used in the Checker code to pop up a message saying who won
    # and then restart the game
    def checkswinner(self):
        button = self.button
        if (button[0][0] == 1 and button[0][1] == 1 and button[0][2] == 1 or button[1][0] == 1 and button[1][1] == 1 and button[1][2] == 1 or button[2][0] == 1 and button[2][1] == 1 and button[2][2] == 1 or button[0][0] == 1 and button[1][0] == 1 and button[2][0] == 1 or button[0][1] == 1 and button[1][1] == 1 and button[2][1] == 1 or button[0][2] == 1 and button[1][2] == 1 and button[2][2] == 1 or button[0][0] == 1 and button[1][1] == 1 and button[2][2] == 1 or button[0][2] == 1 and button[1][1] == 1 and button[2][0] == 1):
            return 1
        elif (button[0][0] == 2 and button[0][1] == 2 and button[0][2] == 2 or button[1][0] == 2 and button[1][1] == 2 and button[1][2] == 2 or button[2][0] == 2 and button[2][1] == 2 and button[2][2] == 2 or button[0][0] == 2 and button[1][0] == 2 and button[2][0] == 2 or button[0][1] == 2 and button[1][1] == 2 and button[2][1] == 2 or button[0][2] == 2 and button[1][2] == 2 and button[2][2] == 2 or button[0][0] == 2 and button[1][1] == 2 and button[2][2] == 2 or button[0][2] == 2 and button[1][1] == 2 and button[2][0] == 2):
            return 2
        elif (button[0][0] != 0 and button[0][1] != 0 and button[0][2] != 0 and button[1][0] != 0 and button[1][1] != 0 and button[1][2] != 0 and button[2][0] != 0 and button[2][1] != 0 and button[2][2] != 0):
            return -1
            
    # this function resest the array, making it possible to start the game again
    def cleansplay(self):
        self.button = np.zeros([3,3])