# Date: 1/1/2020 Description: First attempt at creating a code that solves non linear equations. I used the Numerical
# methods book as a reference.

# The first numerical method found in the book (Chapter 3 and on) is the regula falsi method, so I am going to try
# and write a code that solves nonlinear equations using this method.

# Inputs need to be a nonlinear equation and points a and b where f(a)*f(b)<0

def regula_falsi(def f(x),a,b):
# Gonna break up the code into parts to make it easier to visualize

    # Step 1: Define a tolerance and a maximum number of iterations within the function
    tol = 0.0001
    iterations = 100

    # Step 2: Determine if the input a or b is a solution
    msg1 = '{} is a solution'
    if f(a) = 0
        return print(msg1.format(a))
    elif f(b) = 0
        return print(msg1.format(b))

    #Step 3: Determine if [a,b] contains a solution
    if f(a)*f(b) > 0
        return print('There exists not solution on the input interval [a,b]')

    #Step 4:Find the solution through iteration (A for loop)
    for i = 1:iterations
        xns = (f(b)*a-f(a)*b)/(f(b)-f(a))
        if f(xns)*f(a) > 0
            if b - xns < tolerance
                return print(msg1.format(b)
            elif
                b = f(xns)
        elif f(xns)*f(b) < 0
            if a - xns < tolerance
                return print(msg1.format(a)
            elif
                a = f(xns)
        #Step 5: Check iterations
        if i = iterations
                return print("Error: Convergence was not achieved in 100 iterations")
