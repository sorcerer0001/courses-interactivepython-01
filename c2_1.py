# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

# initialize global variables used in your code here
guess = 0
secret_number = 0
num_range = 100
attempts = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0, num_range)
    a = str(num_range)
    print ""
    print "New game. The range is from 0 to " + a

def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(inp):
    global guess
    guess = int(inp)
    print ""
    print "Guess was " + inp
    
    global attempts
    attempts = attempts + 1
    n = math.ceil(math.log((num_range-0+1), 10)/math.log(2, 10))
    remaining_guesses = str(int(n) - attempts)
    print "Number of remaining guesses: " + remaining_guesses
    
    if guess < secret_number:
        print "Higher"
    elif guess > secret_number:
        print "Lower"
    else:
        print "Correct"
        attempts = 0
        new_game()
    
    if attempts >= math.ceil(n):
        attempts = 0
        print "OH, SORRY...CONSUMED ATTEMPTS. LET`S PLAY AGAIN"
        new_game()
    else:
        ""
# create frame
frame=simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
button1=frame.add_button('Range is [0,100)', range100, 200)
button2=frame.add_button('Range is [0,1000)', range1000, 200)
inp=frame.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
