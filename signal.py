mport turtle
import time

# Create the window
wn = turtle.Screen()
wn.title("Stoplight")
wn.bgcolor("black")

# Create the stoplight box
pin = turtle.Turtle()
pin.pensize(3)
pin.penup()
pin.goto(-60, 90)  # Adjusted coordinates for a larger box
pin.pendown()
pin.pencolor("yellow")
for _ in range(4):
    pin.forward(120)  # Adjusted length of the sides
    pin.right(90)
pin.hideturtle()


# Function to control the traffic signals based on lane densities
def control_traffic(densities):
    max_density_index = densities.index(max(densities))

    for i, density in enumerate(densities):
        if i == max_density_index:
            green_light.color("green")
            red_light.color("gray")
        else:
            yellow_light.color("yellow")
            time.sleep(2)  # Wait for 2 seconds before showing red
            red_light.color("red")
            yellow_light.color("gray")

red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("gray")
red_light.penup()
red_light.goto(0, 75)  # Adjusted coordinates for light positions

yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("gray")
yellow_light.penup()
yellow_light.goto(0, 30)  # Adjusted coordinates for light positions

green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("gray")
green_light.penup()
green_light.goto(0, -15)  # Adjusted coordinates for light positions

# Example usage
lane_densities = [50, 30, 20, 40]  # Example densities for four lanes
control_traffic(lane_densities)

# Keeps the window open until closed by the user
wn.mainloop()
