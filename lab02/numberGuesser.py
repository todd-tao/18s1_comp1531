'''
number guessing game

have to keep guessing until you get them all
the game will keep telling whether to go higher or lower to get the closest number you havent guessed yet, biasing towards lower

the numbers are distinct
you can quit the game any-time by typing 'q'

If a lower number is guessed, you must print:
    'The closest to [guess] is lower'
elif a higher number is guessed, you must print:
    'The closest to [guess] is higher'
elif a number in the list is guessed, you must print:
    'You found [guess]! It was in the list'

If the player wins, you must print:
    'Congratulations! You won!'

These outputs are important because of the testing
'''

import random
import math

MIN = 0
MAX = 10
NUM_VALUES = 3


def handle_guess(guess, values):
    # complete your solution here
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    if (len(values) == 1):                      #consider the len of values = 1, avoid range(0,0)
        values.remove(guess)
        return values
    for i in range(len(values)-1):
        #print("===%d====" % i)
        if (values[i] == guess):
            values.remove(guess)                #list.remove
    return values


def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value
    if (guess in values):
        return guess
    if (guess > values[len(values)-1]):             #guess > maximum
        return values[len(values)-1]
    if (guess < values[0]):                #guess< minmum
        return values[0]
    if (len(values) == 2):                 #only have too element
        if (abs(values[0] - guess) <= (values[1] - guess)):
            return values[0]
        else:
            return values[1]
            
    for i in range(len(values)-1):                  #guess in the list
        if (values[i] < guess and values[i+1] > guess):
            if (abs(values[i] - guess) <= (values[i+1] - guess)):
                return values[i]
            else:
                return values[i+1]


def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q', the game should continue to run, waiting
    # for user to input their guess.
    # This function exits when the game is over

    
    while (1):
        #print(values)
        guess = input("Please guess a number:")             #input a number
        if (guess == 'q'):                      #type 'q' to quit
            return
        else:
            guess = int(guess)              #change type of input
  
        if (guess in values):                
            print("You found %d! It was in the list" % guess)
            handle_guess(guess, values)                  
        else:
            closest_number = find_closest(guess, values)
            if (closest_number < guess):
                print("The closest to %d is lower" % guess)
            else:
                print("The closest to %d is higher" % guess)
        if (len(values) == 0):                  #once there is no element in list, break the loop
                    break
    print('Congratulations! You won!')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
