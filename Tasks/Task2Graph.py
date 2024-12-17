import numpy as np
import matplotlib.pyplot as plt
import math
def f(x):
    return math.exp(x) - 2 * x - 3

# Here is generating x values for the plot, from 0 to 2 with 400 points
x_vals = np.linspace(0, 2, 400)
# Then calculate corresponding y values by applying the function to each x
y_vals = [f(x) for x in x_vals]
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$f(x) = e^x - 2x - 3$', color='blue')

#Adding horizontal and vertical lines at x and y equal to 0
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
