import matplotlib.pyplot as plt
def f(x):
    return x ** 2 - 2 ** x
def false_position_method(f, a, b, max_iter=100, tol=1e-6):
    iterations = 0
    errors_abs = []  # List to store errors
    errors_rel = []  # List to store errors

    while iterations < max_iter:
        c = b - f(b) * (b - a) / (f(b) - f(a)) # False Position Formula
        # Here is calculating of absolute error
        if iterations > 0:
            error_abs = abs(c - b)  # the difference between successive approximations
            error_rel = abs((c - b) / c)  # Relative error
        else:
            error_abs = abs(c - b)  # For the first iteration, we use the initial error
            error_rel = 0  # No relative error for the first iteration, cause there is not previous approximation

        errors_abs.append(error_abs) #Store the errors
        errors_rel.append(error_rel)
        print(f"Iteration {iterations + 1}: Absolute Error = {error_abs}, Relative Error = {error_rel}")

        if error_abs < tol: # Checks for convergence
            break
        if f(c) * f(a) < 0: # Updates the points for the next iteration
            b = c # if the root lies between a and c
        else: # otherwise we set
            a = c
        iterations += 1
    return c, iterations, errors_abs, errors_rel

# Initial guesses found by substitution where the sign changes
a = -1
b = 0.5
root, iter_count, errors_abs, errors_rel = false_position_method(f, a, b)

print(f"\nRoot: {root}")
print(f"Number of iterations: {iter_count}")
print(f"Final Absolute Error: {errors_abs[-1]}")

# Plotting the Graphs
plt.figure(1)
plt.plot(range(iter_count), errors_abs[:iter_count], marker='o', linestyle='-', color='b')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')
plt.title('Absolute Error vs Iteration (False Position Method) - Linear Scale')
plt.grid(True)

plt.figure(2)
plt.plot(range(iter_count), errors_abs[:iter_count], marker='o', linestyle='-', color='r')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')
plt.title('Absolute Error vs Iteration (False Position Method) - Log Scale')
plt.grid(True)
plt.yscale('log')
plt.show()





