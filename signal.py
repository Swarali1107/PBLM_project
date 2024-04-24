import time

# Define the windows or canvas objects (redwin, yellowwin, greenwin)
# assuming they are created elsewhere in your code.

# Function to control the traffic signals based on lane densities
def control_traffic(densities):
    max_density_index = densities.index(max(densities))
    
    for i, density in enumerate(densities):
        if i == max_density_index:
            green(10)  # Assuming 10 signals for high density
        else:
            yellow(5)  # Show yellow for 5 signals
            time.sleep(2)  # Wait for 2 seconds before showing red
            red(3)  # Assuming 3 signals for low density

# Red function
def red(a):
    for i in range(a):
        redwin.create_oval(3, 5, 10, 10, fill="red")
        th.update()
        time.sleep(0.15)

# Yellow function
def yellow(a):
    for i in range(a):
        yellowwin.create_oval(3, 55, 50, 100, fill="yellow")
        th.update()
        time.sleep(0.5)  # Show yellow for 0.5 seconds

# Green function
def green(a):
    for i in range(a):
        greenwin.create_oval(3, 105, 10, 150, fill="green")
        th.update()

# Example usage
lane_densities = [50, 30, 20, 40]  # Example densities for four lanes
control_traffic(lane_densities)
