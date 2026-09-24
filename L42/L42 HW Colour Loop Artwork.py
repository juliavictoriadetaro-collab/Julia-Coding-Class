import turtle

# PART 1 - SET UP THE CANVAS
paper = turtle.Screen()
paper.bgcolor("black")
paper.title("Colour Loop Artwork")

# PART 2 - CREATE THE TURTLE
pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()
pen.pensize(2)

# PART 3 - DRAW A FILLED PETAL
def draw_petal(size, colour):
    pen.color(colour)
    pen.begin_fill()

    for _ in range(2):
        pen.circle(size, 60)
        pen.left(120)

    pen.end_fill()

# PART 4 - CREATE THE COLOUR LOOP ARTWORK
colours = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

for i in range(36):
    draw_petal(90, colours[i % len(colours)])
    pen.right(10)
