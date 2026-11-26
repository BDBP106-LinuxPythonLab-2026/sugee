import matplotlib.pyplot as plt
import numpy as np
import pandas as ps

# Step 1: Create the data
temps = np.arange(20, 71, 5)

activity = np.array([
    12, 20, 35, 52, 70, 85,
    92, 78, 45, 18, 5
])

# Step 2: Find optimum temperature
optimum = temps[np.argmax(activity)]

print("Optimum temperature:", optimum, "°C")

# Step 3: Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Step 4: Plot the graph
ax.plot(temps, activity, marker='o', color='blue')

# Step 5: Draw vertical dashed line
ax.axvline(optimum, color='red', linestyle='--',
           label='Optimum temperature')

# Step 6: Annotate the peak
ax.annotate(
    "Optimum temperature = 50°C",
    xy=(optimum, np.max(activity)),
    xytext=(53, 100),
    arrowprops=dict(arrowstyle='->')
)

# Step 7: Add labels and title
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Relative enzyme activity")
ax.set_title("Effect of Temperature on Enzyme Activity")

ax.legend()
ax.grid(alpha=0.3)

# Step 8: Display graph
plt.tight_layout()
plt.show()



