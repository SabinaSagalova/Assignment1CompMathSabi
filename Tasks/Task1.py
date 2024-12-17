# Here is the imported libraries, matplotlib.pyplot to plot the graph of the function, scipy.optimize.fsolve
# for solving non-linear equations, in our task it is used for exact root of the equation numerically
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x): # Here is defining of the function
    return x**3 - 2*x**2 - 5

# First, we should plot the graph, so we define the range for x
x = np.linspace(1, 4, 500) #It generates an array of 500 equally spaced values between 1 and 4
y = f(x)  # This computes f(x) for all x values

# Plot the graph part
plt.figure(figsize=(8, 6)) # this sets the size of the plot
plt.plot(x, y, label='f(x) = x³ - 2x² - 5', color='blue') #plots the function color as a blue curve
plt.axhline(0, color='red', linestyle='--', label='y = 0')  # Horizontal line for y = 0
plt.title('Graph of f(x) = x³ - 2x² - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend() #help to label and identify the different data in graph
plt.grid(True) #add the grid on the plot
plt.show() #displays the plot

# Looking at the graph I found Approximate root
approx_root = 2.6

# Here is Calculation of f(x) for the approximate root
approx_value = f(approx_root)
print(f"Approximate root: {approx_root}")
print(f"Value of f({approx_root}) = {approx_value}")

# It is Calculation of exact root using fsolve
exact_root = fsolve(f, approx_root)[0]  # Initial guess is the approximate root
print(f"Exact root: {exact_root}")

# Calculating the absolute error by comparing the approximate root (from the graph)
# and the exact root which we find by fsolve
absolute_error = abs(exact_root - approx_root)
print(f"Absolute error: {absolute_error}")
