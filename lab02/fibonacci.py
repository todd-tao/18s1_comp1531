'''
Define a recursive function that, takes in an index n will calculate the n-th number in the fibonacci sequence.
The fibonacci sequence is defined as 
f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)
The index is to be read from the standard input and 
the fibonacci number at that index is to be printed
to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

#Initialising a dictionary with a fibonacci series of 4 elements
fib_dict = {
	0: 0,
	1: 1,
	2: 1,
	3: 2
}

# Define this recursive function to return the expected output
# Do not print it from this function
def fib_sequence(num):
    # to be completed
    if (num in fib_dict):
        return fib_dict[num]
    else:
        fib_dict[num] = fib_sequence(num-1) + fib_sequence(num-2)

    return fib_dict[num]

if __name__ == '__main__':
	#write code to accept user input, call the function and print the result
    num = int(input("Enter the n-th number you want:"))
    print(fib_sequence(num))
