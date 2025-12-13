import matplotlib.pyplot as plt
import numpy as np

# Snowflake parameters
arms = 6
arm_length = 1
branch_length = 0.3
branch_angle = np.pi/6  # 30 degrees

# Colors for arms and branches
colors = ['#1E90FF', '#00BFFF', '#87CEFA', '#ADD8E6']

# Create figure with black background
fig = plt.figure(figsize=(6,6), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')
plt.axis('off')
ax.set_aspect('equal')

# Draw arms with small branches
for i in range(arms):
    angle = i * (2*np.pi / arms)
    
    # Main arm
    x_main = [0, arm_length * np.cos(angle)]
    y_main = [0, arm_length * np.sin(angle)]
    plt.plot(x_main, y_main, color=colors[i % len(colors)], linewidth=3)
    
    # Branches along the arm
    for b in [0.3, 0.6, 0.9]:
        # branch on one side
        branch_angle1 = angle + branch_angle
        x_branch = [b * np.cos(angle), b * np.cos(angle) + branch_length * np.cos(branch_angle1)]
        y_branch = [b * np.sin(angle), b * np.sin(angle) + branch_length * np.sin(branch_angle1)]
        plt.plot(x_branch, y_branch, color=colors[i % len(colors)], linewidth=2)
        
        # branch on other side
        branch_angle2 = angle - branch_angle
        x_branch2 = [b * np.cos(angle), b * np.cos(angle) + branch_length * np.cos(branch_angle2)]
        y_branch2 = [b * np.sin(angle), b * np.sin(angle) + branch_length * np.sin(branch_angle2)]
        plt.plot(x_branch2, y_branch2, color=colors[i % len(colors)], linewidth=2)

# Show snowflake
plt.show()
