import turtle

# Program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400

# Move the snake
def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    snake.append(new_head)

    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
    
    screen.update()

    turtle.ontimer(move_snake, DELAY)

# Drawing window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

# Create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as list
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

move_snake()

turtle.done()