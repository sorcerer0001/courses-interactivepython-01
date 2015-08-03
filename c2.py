
import simplegui
import random
import math

num_range = 100

remaining_guesses = 0

secret_number = 0


def new_game():

    global num_range, remaining_guesses, secret_number

    secret_number = random.randrange(0, num_range)
    remaining_guesses = int(math.ceil(math.log(num_range, 2)))

    print
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining_guesses


def range100():

    global num_range

    num_range = 100
    new_game()

def range1000():

    global num_range

    num_range = 1000
    new_game()
    
def input_guess(guess):

    global remaining_guesses, secret_number

    guess = int(guess)
    remaining_guesses -= 1

    print
    print "Guess was", guess

    if guess == secret_number:
        print "Correct"
        new_game()
    elif remaining_guesses == 0:
        print "You lose"
        new_game()
    else:
        print "Number of remaining guesses is", remaining_guesses
        if guess < secret_number:
            print "Higher"
        else:
            print "Lower"



frame = simplegui.create_frame("Guess the number", 200, 200)



frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)



new_game()
