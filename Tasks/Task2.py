import math
def f(x): #Defining the function we want to find the root
    return math.exp(x) - 2 * x - 3
def bisection(f, a, b, tol): #Bisection method to find the root of the function in the interval [a, b]
    if f(a) * f(b) >= 0: #Exception, to guarantee that root exists in the interval
        raise ValueError("f(a) and f(b) must have different signs.")

    n_iterations = 0 #to count the iterations
    while (b - a) / 2.0 > tol: #we use loop for until the interval size is smaller than the specified tolerance
        midpoint = (a + b) / 2.0
        f_mid = f(midpoint)  # Calculate f(midpoint) only once to avoid redundant calls
        n_iterations += 1
        if f_mid == 0:  #Then it founds exact root and exit
            break
        if f_mid * f(a) < 0: #checks if the function changes signs between
        #if f_mid and f(a) have opposite signs, the root must lie between a and mid
        #if the signs are opposite it updates the upper bound of the interval:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2.0, n_iterations

def secant(f, x0, x1, tol, max_iter=100): #Secant method approximates the root by using two initial guesses x0,x1
    n_iterations = 0 #to count the iterations
    while abs(x1 - x0) > tol and n_iterations < max_iter:
        #condition checks whether the difference between the two guesses is greater than the tolerance
        n_iterations += 1
        f_x0, f_x1 = f(x0), f(x1)  # Calculate f(x0) and f(x1) once
        if f_x1 - f_x0 == 0:  # Exception, to avoid division by zero
            raise ValueError("Division by zero in the secant method.")
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0) #Formula uses two most recent guesses and their function values
        x0, x1 = x1, x_next #here is updating the guesses

    return x1, n_iterations

a = 0 # It is given parameters for the methods
b = 2
tolerance = 1e-6
root_bisection, iterations_bisection = bisection(f, a, b, tolerance) # Usage of Bisection Method
x0 = 0.0
x1 = 2.0
root_secant, iterations_secant = secant(f, x0, x1, tolerance) # Usage of Secant Method
exact_root = 1.925 #I found it from graph
relative_error_bisection = abs((root_bisection - exact_root) / exact_root)
relative_error_secant = abs((root_secant - exact_root) / exact_root)

print("Bisection Method:")
print(f"Root: {root_bisection:.6f}, Iterations: {iterations_bisection}, Relative Error: {relative_error_bisection:.10f}")
print("\nSecant Method:")
print(f"Root: {root_secant:.6f}, Iterations: {iterations_secant}, Relative Error: {relative_error_secant:.10f}")
