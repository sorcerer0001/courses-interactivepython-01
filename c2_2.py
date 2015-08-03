# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

intNumberRange=100
intGuessTimeEx=7
intGuessTime=0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global intGuessTime
    intGuessTime=0
    secret_number=random.randint(0,intNumberRange-1)
    print ""
    print "NEW game start, Enter a number."
    # remove this when you add your code    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global intNumberRange
    global intGuessTimeEx
    intNumberRange=100
    intGuessTimeEx=7
    print ""
    print "range change to [0,100),guess time limit:7"
    new_game()
    # remove this when you add your code    


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global intNumberRange
    global intGuessTimeEx
    intNumberRange=1000
    intGuessTimeEx=10
    print ""
    print "range change to [0,1000),guess time limit:10"
    new_game()
    
def input_guess(guess):
    # main game logic goes here 
    print "Guess was "+guess
    guess=int(guess)
    if secret_number==guess:
        print "Correct!!!"
        new_game()
    elif secret_number<guess:
        print "Higher"
    elif secret_number>guess:
        print "Lower"
    global intGuessTime
    intGuessTime=intGuessTime+1
    if intGuessTimeEx==intGuessTime:
        print "you lose,the Correct number is"+str(secret_number)
        new_game()
    # remove this when you add your code


    
# create frame
entFrame=simplegui.create_frame("guess the number",200,200)

# register event handlers for control elements and start frame
entFrame.add_button("Range is [0,100)",range100,200)
entFrame.add_button("Range is [0,1000)",range1000,200)
entFrame.add_input("Enter the guess",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
