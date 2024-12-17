def fixed_point_iteration(g, x0, true_root, max_iter=10, tol=1e-6):
    x = x0  # Initial approximation
    errors_abs = []  # List to store errors
    print("Iteration", "x_n", "Absolute Error")

    for i in range(1, max_iter + 1):
        x_next = g(x)  # this computes the next approximation using the function g(x)
        error_abs = abs(true_root - x_next) #Calculate absolute error comparing with true root
        errors_abs.append(error_abs)  # saves the absolute error at each iteration
        print(f"{i:<10}{x_next:<15.10f}{error_abs:<20.10f}")

        if abs(x_next - x) < tol: # Checking convergence
            print(f"Convergence reached after {i} iterations.")
            return x_next, errors_abs
        x = x_next  # Updating x for the next iteration
    return x, errors_abs
def g(x):
    return (x ** 2 + 5) / 6  # Transformed equation x = g(x)

true_root = 1  # True Root Calculated by quadratic formula
x0 = 0.5  # Initial guess
final_root, absolute_errors = fixed_point_iteration(g, x0, true_root)  # Performing Method

print(f"\nApproximated Root after 10 iterations: {final_root}")
print(f"The Last Absolute Error: {absolute_errors[-1]}")
