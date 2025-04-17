import matplotlib.pyplot as plt
import numpy as np

# 1. Define gateway coordinates and observation angles (replace with your actual data)
x1, y1 = 1, 2  # Gateway A coordinates
x2, y2 = 6, 0  # Gateway B coordinates
theta1_deg = 30  # Observation angle from Gateway A (degrees)
theta2_deg = 120 # Observation angle from Gateway B (degrees)

# 2. Convert angles to radians
theta1_rad = np.deg2rad(theta1_deg)
theta2_rad = np.deg2rad(theta2_deg)

# 3. Calculate the slopes of the observation lines
m1 = np.tan(theta1_rad)
m2 = np.tan(theta2_rad)

# 4. Define the equations of the observation lines (as functions)
def line_a(x):
    return m1 * (x - x1) + y1

def line_b(x):
    return m2 * (x - x2) + y2

# 5. Calculate the intersection point (fire source location)
if np.isclose(m1, m2):
    print("The two lines are parallel, unable to determine a unique intersection point.")
else:
    x_intersect = (y2 - y1 + x1 * m1 - x2 * m2) / (m1 - m2)
    y_intersect = m1 * (x_intersect - x1) + y1
    print(f"Inferred fire source location: ({x_intersect:.2f}, {y_intersect:.2f})")

    # 6. Define the x-axis range for plotting the lines
    x_range = np.linspace(min(x1, x2, x_intersect) - 2, max(x1, x2, x_intersect) + 2, 100)
    y_range_a = line_a(x_range)
    y_range_b = line_b(x_range)

    # 7. Plot the gateways and observation lines
    plt.plot(x_range, y_range_a, label=f'Observation line from Gateway A (θ1 = {theta1_deg}°)')
    plt.plot(x_range, y_range_b, label=f'Observation line from Gateway B (θ2 = {theta2_deg}°)')

    # 8. Mark the gateway and fire source locations
    plt.scatter(x1, y1, color='blue', label='Gateway A')
    plt.scatter(x2, y2, color='green', label='Gateway B')
    plt.scatter(x_intersect, y_intersect, color='red', label='Inferred Fire Source')

    # 9. Add legend, labels, and title
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Fire Source Localization Based on Gateway Observation Angles')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box') # Set aspect ratio to be equal

    # 10. Show the plot
    plt.show()