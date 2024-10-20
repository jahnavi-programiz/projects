import turtle

wn = turtle.Screen()
wn.setup(500, 500)

alex = turtle.Turtle()
alex.shape("turtle")

# Draw the pattern
#"green", "blue", "red"
for color in "green", "blue", "red":
    alex.color(color)
for radius in range(50, 90, 10):
    alex.circle(radius)
alex.right(120)

wn.mainloop()