import matplotlib.pyplot as plt
import numpy as np

# Generate a sequence of numbers (from 0 to 10 with 100 steps in between)
x = np.linspace(0, 10, 100)

# Compute the sine of these numbers
y = np.sin(x)

# Create a plot with x (horizontal axis) and y (vertical axis)
plt.plot(x, y)

# Title of the plot
plt.title("Sine Wave")

# Labels for x and y axes
plt.xlabel("x")
plt.ylabel("sin(x)")

# Show the plot
plt.show()