import turtle

# Program constants
WIDTH = 500
HEIGHT = 500
DELAY = 300

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

# Move the snake
def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

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

# Event handling
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")



# Create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as list
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# Draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

move_snake()

turtle.done()