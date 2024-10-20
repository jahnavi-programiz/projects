import turtle

# Set up the screen
wn = turtle.Screen()
wn.setup(500, 500)

# Create a turtle named alex
alex = turtle.Turtle()
alex.shape("turtle")

# Draw concentric circles
for counter in range(1, 6):
    alex.circle(20 * counter)
    alex.penup()
    alex.goto(0, -20 * counter)
    alex.pendown()

# Hide the turtle and display the window
alex.hideturtle()
wn.mainloop()
