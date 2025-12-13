import matplotlib.pyplot as plt
import numpy as np

# Parameter cd 
t = np.linspace(0, 2 * np.pi, 1000)

# Heart shape equations
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create figure
plt.figure(facecolor='white')

# Fill the heart with pink
plt.fill_between(x, y, color='#FFC0CB', alpha=0.6)

# Plot black outline (thick, behind)
plt.plot(x, y, color='black', linewidth=4)

# Plot red outline (slightly thinner, on top)
plt.plot(x, y, color='red', linewidth=2)

# Show grid for graph lines
plt.grid(True, linestyle='--', alpha=0.3)

# Equal aspect ratio
plt.axis('equal')
plt.title("Heart with Pink Fill & Red/Black Outline", fontsize=14, color='black')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
