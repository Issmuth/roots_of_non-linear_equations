# import this library to use mathematical expressions, use "pip install sympy" if library not on you device
from sympy import *

#defining the symbol x for function variables
x = symbols('x')

# define the error tolerance as global variabl so the functions terminates when they reach this point
errTolerance = 0.00001

def bisection(func):
    """Bisection method implementation.
    
    Args:
        func: function to find root for
    Return: root of the function.
    """

    try:
        # accept the upper and lower continous intervals from the user
        lower = float(input("Enter the lower interval: "))
        upper = float(input("Enter the upper interval: "))

        # check if the entered value is a numeral either float or integer
        if (type(upper) is not float)\
            or (type(lower) is not float):
            raise TypeError
    except ValueError:
        print("upper and lower intervals must either be an integer or float")
        bisection(func)

    # check if the function is actually continous on the given intervals
    a = (func.subs(x, upper).evalf())
    b = (func.subs(x, lower).evalf())  
    isCont = a * b

    # if isCont is less than 0 it continues
    if isCont < 0:
        pass
    #if it is equal to zero one of the intervals is the root
    elif isCont == 0:
        if (func.subs(x, upper).evalf()) == 0:
            print("root at iteration 0 is already the interval: {}".format(upper))
            menu()
        else:
            print("root at iteration 0 is already the interval: {}".format(lower))
            menu()
    # otherwise user must choose another interval since there is no root in that interval
    else:
        print ("The intervals provided are not continous for the function. Please try again")
        bisection(func)

    #setting initial err value for the loop
    err = abs(upper - lower)

    # now bisect the intervals and check accordingly until the error tolerance is reached
    while err > errTolerance:
        root = (upper + lower) / 2
        print("root = {}".format(root), end="\t\t")
        print("a={}\t\tb={}".format(lower, upper))

        if (func.subs(x, lower).evalf()) == 0:
            print ("root found hence, ")
            root = lower
            break

        if (func.subs(x, upper).evalf()) == 0:
            print ("root found hence, ")
            root = upper
            break
        
        if ((func.subs(x, root).evalf()) * (func.subs(x, upper).evalf())) < 0:
            lower = root
            err = abs(upper - lower)

        if ((func.subs(x, root).evalf()) * (func.subs(x, lower).evalf())) < 0:
            upper = root
            err = abs(upper - lower)
    print("Error Tolerance reached, loop terminated...")
    print("The closest approximate root is : {}".format(root))


def newtonRaphson(func):
    """Newton Raphson method function."""
    # set iteration to 0
    iteration = 0

    # accept initial guess and number of iterations from the user
    try:
        x0 = int(input('insert your initial guess please?\n'))
        maxiteration = int(input('Give a maximum number of iterations'))
    except ValueError:
         print("initial guess and max iteration must either be an integer or float")
         newtonRaphson(func)
         
    # differentiate the function the user passed using diff function
    der = diff(func, x)
  
    while iteration < maxiteration:
        # evaluate the function at the initial guess for both the f and f'
        d = der.subs(x, x0).evalf()
        f = func.subs(x, x0).evalf()

        # set the next enhanced guess to the difference between the initial guess and the division of the evaluations for before
        xnext = x0 - f/d
        root = round(xnext, 5)
        print("root at iteration {}: {}".format(iteration, root), end="\t\t")
        print("next guess is: {}".format(xnext))

        # Check if the difference between current guess and next guess is below a certain tolerance
        if abs(xnext - x0) < errTolerance:
            print("Root found within tolerance hence ")
            break
        x0 = xnext
        iteration += 1

    print("maximum iteration reached......")
    print("The closest approximate root is: {}".format(root))

def menu():
    """Menu function for basic user interaction."""

    # define a menu option dictionary
    option = {
        1: bisection,
        2: newtonRaphson
    }

    print("------------ Welcome ------------")

    try:
        # request action from the user.
        choice = int(input("Which method do you want to use?\n1. Bisection Method\n2. Newton-Raphson Method\n3. Exit\n"))

        if choice in option:
        # Accept a function from the user
            func_str = input("Enter a function you want to finds the roots for (check manual for function input format): ")
            func = sympify(func_str)
            option[choice](func)
            menu()
        elif choice == 3:
            quit
        else:
            print("Invalid option. please try again")
            menu()
    except ValueError:
        print("\n\n-------------------------------\nEnter the option 1, 2 or 3 only\n-------------------------------\n\n")
        menu()

# starts the program from the menu when this script is executed directly
if __name__ == '__main__':
    menu()
