import matplotlib.pyplot as plt

def f(x): # Define the function
    return x**2 - 3*x + 2
def f_prime(x): # Define the derivative
    return 2*x - 3

def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    errors = []  # To store iteration data
    x = x0  # sets the initial guess as `x`
    for i in range(max_iter):
        x_new = x - f(x) / f_prime(x)  # The Newton-Raphson formula
        abs_error = abs(x_new - x)  # Here we calculate absolute error
        rel_error = abs_error / abs(x_new) if x_new != 0 else 0  # Calculating the relative error avoid dividing by zero
        errors.append((i+1, x_new, abs_error, rel_error)) # it is a tuple with 4 elements
        if abs_error < tol:  # If the error is within tolerance, it will stop iterating
            break
        x = x_new # Updating the current guess
    return errors

x0 = 2.5 # Initial guess
errors = newton_raphson(f, f_prime, x0) # Finding the root using the Newton-Raphson method

# Display the table
print("Iteration | Current Guess | Absolute Error | Relative Error")
for e in errors:
    print(f"{e[0]}        | {e[1]:.6f}     | {e[2]:.6f}        | {e[3]:.6f}")

# Plotting the convergence graph
iterations = [e[0] for e in errors]
abs_errors = [e[2] for e in errors]
plt.plot(iterations, abs_errors, marker='o')
plt.yscale('log')  # This log scale is just for better visualization of convergence
plt.xlabel("Iteration Number")
plt.ylabel("Absolute Error (Log Scale)")
plt.title("Convergence of the Newton-Raphson Method")
plt.grid(True)
plt.show()