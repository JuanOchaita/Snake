import turtle
import random

cell_size = 20
grid_size = 7
grid_length = cell_size * grid_size

screen = turtle.Screen()
screen.bgcolor("#1e1e2e")
screen.title("Snake Grid")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

turtle.tracer(0, 0)

start_x = -grid_length / 2
start_y = grid_length / 2

# Crear lista de posiciones válidas alineadas con la cuadrícula
valid_positions = []
for row in range(grid_size):
    for col in range(grid_size):
        x = int(start_x + col * cell_size)
        y = int(start_y - row * cell_size)
        valid_positions.append((x, y))

def draw_grid():
    square_color = "#181825"
    pen.color("#232332")
    pen.pensize(1)
    for x, y in valid_positions:
        pen.goto(x, y)
        pen.fillcolor(square_color)
        pen.begin_fill()
        for _ in range(4):
            pen.pendown()
            pen.forward(cell_size)
            pen.right(90)
        pen.end_fill()
        pen.penup()

    # Dibujar el marco
    pen.pensize(2)
    pen.color("#1e1e2e")
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.goto(start_x + grid_length, start_y)
    pen.goto(start_x + grid_length, start_y - grid_length)
    pen.goto(start_x, start_y - grid_length)
    pen.goto(start_x, start_y)
    pen.penup()

# --- Snake setup ---
snake = [valid_positions[grid_size * grid_size // 2]]
snake_dir = (0, -cell_size)

def draw_snake():
    for i, (x, y) in enumerate(snake):
        pen.goto(x, y)
        pen.fillcolor("#FFFFFF" if i == 0 else "#e1e1e1")
        pen.begin_fill()
        for _ in range(4):
            pen.pendown()
            pen.forward(cell_size)
            pen.right(90)
        pen.end_fill()
        pen.penup()

# --- Movement and wrapping ---
def move_snake():
    head_x, head_y = snake[0]
    dx, dy = snake_dir
    new_x = head_x + dx
    new_y = head_y + dy

    # Warp en los bordes
    if new_x < start_x:
        new_x = start_x + (grid_size - 1) * cell_size
    elif new_x > start_x + (grid_size - 1) * cell_size:
        new_x = start_x
    if new_y < start_y - (grid_size - 1) * cell_size:
        new_y = start_y
    elif new_y > start_y:
        new_y = start_y - (grid_size - 1) * cell_size

    new_head = (new_x, new_y)
    snake.insert(0, new_head)

    # Comer
    if food_pos and new_head == food_pos:
        spawn_food()
    else:
        snake.pop()

# --- Input ---
def go_up():
    global snake_dir
    if snake_dir != (0, -cell_size):
        snake_dir = (0, cell_size)

def go_down():
    global snake_dir
    if snake_dir != (0, cell_size):
        snake_dir = (0, -cell_size)

def go_left():
    global snake_dir
    if snake_dir != (cell_size, 0):
        snake_dir = (-cell_size, 0)

def go_right():
    global snake_dir
    if snake_dir != (-cell_size, 0):
        snake_dir = (cell_size, 0)

# --- Food ---
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.hideturtle()
food_pos = None

# --- Setup ---
draw_grid()


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Game loop ---
while True:
    move_snake()
    draw_grid()
    draw_snake()
    turtle.update()
    turtle.delay(150)
