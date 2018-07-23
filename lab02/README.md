# Lab 02 (Due in the lab)

# Aim

1.  Understand the importance of requirements engineering and create requirements specifications based on UML use-cases
    
2.  Progress on simple Python exercises based on topics covered in week 2 (Functions, Data Structures, Control Flow)
    

# Lab instructions

 
This lab must be completed during your lab session and for this lab, you are expected to work in groups of two. For the odd-numbered classes, one group of three may be permitted.

## Task 1: Requirements Analysis (6 marks)

AffordableRentals is a company specialising in car rentals to customers. The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy who have completed the requirements gathering and developed the following high-level problem statement. For the purposes of this lab, the scope of the system is limited to the following functionality.

  

1.  A car rental is a vehicle that can be used temporarily for a fee during a specified period.
    
2.  The cars that can be rented from AffordableRentals are grouped into small, medium, large and premium cars.
    
3.  A customer should be able to specify a search criteria and view available cars that match the search criteria. The search criteria should include age, preferred pick-up and drop-off locations
    
4.  The search result should include details of the car type and price for each day of car rental.
    
5.  From the displayed search results, the customer can select a car and proceed with booking the car.
    
6.  During the booking process, the customer is required to specify additional details such as:
    

-   name of the customer and age
    
-   licence number
    
-   the rental period in number of days
    
-   option to purchase an insurance cover
    
-   email-address
    

7.  Insurance is provided by an external company, QBEI Insurances.
    
8.  Once the booking details have been provided by the customer, a net price is computed and displayed to the customer.
    
9.  The customer proceeds with the booking by providing credit card details for payment. The company uses an external Credit Card system to handle payments.
    
10.  Once the payment has been confirmed, an email is sent to the customer confirming the booking.
    
11.  The online system must permit staff of affordable rentals to login to the system with a user-name and password
    
12.  Admin staff once logged in will be able to enter new car information to the system.
    
13.  For each car, the system will hold the following pieces of information: vehicle-type (small, medium, large, premium), make, model, year and registration
    
14.  Managers once logged in will be able to generate weekly reports that show a log of cars rented during the week
    

  

**Your task is to:**

  

1.  Identify the system Actors and goals **(1 mark)**
    

  

2.  Draw a use-case diagram to model the behaviour of the online rental system. The model should include the actors, the use cases, the relation between the use cases and the actors and the relation between the use cases. **(3 marks)**
    

_(Refer to lecture slide, use-case diagram for Device control to help you with this task)_

  

3.  Define a detailed use-case specification for the main use-case of customer renting a car. **(2 marks)**
    

  

Use the template provided in the lecture to define this specification. It must include:

-   _Use-Case name_
    
-   _Brief description_
    
-   _Initiating Actor,_
    
-   _Actor’s goal,_
    
-   _Participating actors_
    
-   _Flow of events for the Main Success usage scenario._
    

  

For the purposes of this lab, you don’t need to define the pre-condition, post-condition and the alternate usage scenarios. _(Refer to lecture slide, usage scenario for Use-Case1: Unlock to help you with this task._)

  

To obtain marks for the above task, you can draw the use-case diagram on paper or you choose to use an online tool such as draw.io to draw your use-case diagram, but it is not necessary. Use-case specification can be typed up or hand-written. All hand-written work must be clear enough to be marked by your tutor.

  

## Task 2: Python Exercises (4 marks)

Complete the following exercises and demo them to your tutor to get marked. The process to import the starter code is the same as last week. Go to https://cgi.cse.unsw.edu.au/~cs1531/18s1/github/run.cgi/labs, select **lab02** and click **Import**. 

  

**Exercise 1:** Fibonacci extension - Print the nth number in the fibonacci series given the index n **(2 Marks)**

Last week, you were asked to complete a Python exercise that produced a list of Fibonacci numbers of size _n_, where n is provided. In this exercise, you are required to write a program that reads a number n and prints the nth number in the Fibonacci series. The program must make use of a **recursive function** to implement this task

  
  

The Fibonacci series in this program should start from one. The first 10 numbers are shown below:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55….

The number at index 1 is 1 and the number at index 3 is 2. So, the number at index 10 would be 55.

_Input:_  5  
_Output:_  5

The starter code for this exercise is in the `fibonacci.py` file. Please complete your solution within this file.  Do not change the function name because it is required during the tests.

**Exercise 2: Extended numberGuesser** **(2 Marks)**

This exercise involves you creating a little command line guessing game. It is fairly simple but will give you some practice in splitting up code into logical sections as well as some of the python `builtin` functions, like `len` and `range`. The rules are as follows:

 - A list of random numbers is created
 - The program then asks for the user to make a guess by entering a number on the command line
 - If the user guesses one of the numbers in the list, that number is removed
 - If the user does not guess a number in the list, the program prints a message saying whether the closest element that **IS** in the list is either higher or lower than their guess.
 - The game ends when the user quits early (types 'q') or the user has guessed all of the numbers in the list.

Please note, the outputs are given for you at the top of the starter code and must be copied exactly as stdout is used for the testing of this exercise.

Please also implement all of the function skeletons as they are tested individually as well.

## Testing
This lab uses the `pytest` package (which you will learn about later on) and some plugins to test the programming exercises.

You will need to install these packages in order to run the tests. To do this, you will use a *virtual environment* which is essentially a nice way to separate python modules you only need for specific projects.

Please read http://www.cse.unsw.edu.au/~cs1531/18s1/labs/lab02/virtual_env.html to get help set up and give some more information about virtual environments.

The below commands will set up your *virtual environment.* Please refer to 
```bash
virtualenv --python=/usr/bin/python3 venv
. venv/bin/activate
pip3 install -r requirements.txt 
```

You can now run the tests by simply running 
```bash
pytest
```
