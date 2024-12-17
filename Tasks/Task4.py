import cmath
def f(x):
    return x**3 + x**2 + x + 1
def mullers_method(f, x0, x1, x2, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        h0 = x1 - x0 # difference between initial guesses
        h1 = x2 - x1
        f0 = f(x0) # function values at this point
        f1 = f(x1)
        f2 = f(x2)
        # b0, b1 are approximations to the derivative of f(over) intervals
        b0 = (f1 - f0) / h0 # average slope of the secant line
        b1 = (f2 - f1) / h1
        d = (b1 - b0) / (h1 + h0) # it is the rate of change of the slopes

        discriminant = cmath.sqrt(b1**2 - 4 * f2 * d)
        #To avoid division by a small number we choose denominator
        if abs(b1 + discriminant) > abs(b1 - discriminant):
            denominator = b1 + discriminant
        else:
            denominator = b1 - discriminant
        x3 = x2 - (2 * f2) / denominator # Formula that calculates new approximation
        if abs(x3 - x2) < tol and abs(f(x3)) < tol: # Check for convergence
            return x3  # Return the root if it converges
        x0, x1, x2 = x1, x2, x3
    print("The method did not converge within the specified number of iterations.")
    return None

x0 = -1
x1 = 0
x2 = 1
root = mullers_method(f, x0, x1, x2)
if root is not None:
    print(f"Root found using Muller's method: x ≈ {root:.18f}")
    f_value = f(root)
    print(f"Value of the function at the root: f({root:.18f}) = {f_value:.18f}")
    # Calculate the absolute error
    error_abs = abs(f_value)
    print(f"Absolute error: {error_abs:.18f}")
