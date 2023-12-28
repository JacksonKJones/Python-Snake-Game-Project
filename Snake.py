import turtle
import random

# Program constants
WIDTH = 500
HEIGHT = 500
DELAY = 120
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if direction != "down":
            snake_direction = "up"
    if direction == "down":
        if direction != "up":
            snake_direction = "down"
    if direction == "left":
        if direction != "right":
            snake_direction = "left"
    if direction == "right":
        if direction != "left":
            snake_direction = "right"
    

# Move the snake
def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
    
        screen.title(f"Snake Game ||| Score: {score} ||| High Score: {high_score}")
        screen.update()

        turtle.ontimer(game_loop, DELAY)

# checks food collision
def food_collision():
    global food_pos, score, high_score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        if high_score < score:
            high_score = score
            stamper.color("green")
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(int(- WIDTH / 2 + FOOD_SIZE), int(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(int(- HEIGHT / 2 + FOOD_SIZE), int(HEIGHT / 2 - FOOD_SIZE))
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    stamper.color("black")
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

# Drawing window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("pink")
screen.tracer(0)

# Event handling
screen.listen()
bind_direction_keys()

# Create turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Draw food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

high_score = 0
reset()

turtle.done()