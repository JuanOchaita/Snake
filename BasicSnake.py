import turtle
import random

# Configuración
cell_size = 20
grid_size = 21
snake_speed = 100  # Aumenté la velocidad para un juego más dinámico

# Cálculos automáticos
grid_length = cell_size * grid_size
start_x = -grid_length // 2
start_y = grid_length // 2
valid_positions = [
    (start_x + col * cell_size, start_y - row * cell_size)
    for row in range(grid_size)
    for col in range(grid_size)
]

# Setup de pantalla y tortugas
screen = turtle.Screen()
screen.bgcolor("#1e1e2e")
screen.title("Snake Grid")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
turtle.tracer(0, 0)

snake_pen = turtle.Turtle()
snake_pen.hideturtle()
snake_pen.speed(0)
snake_pen.penup()

food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()
food.hideturtle()
food_pos = None

# Dibujar cuadrícula (una sola vez)
def draw_grid():
    pen.color("#232332")
    pen.pensize(1)
    square_color = "#181825"
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

    # Marco
    pen.pensize(2)
    pen.color("#1e1e2e")
    pen.goto(start_x, start_y)  # Esquina superior izquierda
    pen.pendown()
    pen.goto(start_x + grid_length, start_y)  # Borde superior (ajustado)
    pen.goto(start_x + grid_length, start_y - grid_length)  # Borde inferior (ajustado)
    pen.goto(start_x, start_y - grid_length)  # Esquina inferior izquierda
    pen.goto(start_x, start_y)  # Volver al inicio
    pen.penup()

# Snake
snake = [valid_positions[len(valid_positions) // 2]]
snake_dir = (0, -cell_size)

def draw_snake():
    snake_pen.clear()
    for i, (x, y) in enumerate(snake):
        snake_pen.goto(x, y)
        snake_pen.fillcolor("#FFFFFF" if i == 0 else "#e1e1e1")
        snake_pen.begin_fill()
        for _ in range(4):
            snake_pen.pendown()
            snake_pen.forward(cell_size)
            snake_pen.right(90)
        snake_pen.end_fill()
        snake_pen.penup()

def move_snake():
    head_x, head_y = snake[0]
    dx, dy = snake_dir
    new_x = head_x + dx
    new_y = head_y + dy

    # Colisión con los bordes
    if new_x < start_x or new_x >= start_x + grid_length or new_y < start_y + 1 - grid_length or new_y >= start_y + 1:
        game_over()
    new_head = (new_x, new_y)
    
    # Colisión con el cuerpo de la serpiente
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    if food_pos and new_head == food_pos:
        spawn_food()
    else:
        snake.pop()

# Controles
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

# Comida
def spawn_food():
    global food_pos
    possible = [pos for pos in valid_positions if pos not in snake]
    food_pos = random.choice(possible)
    fx = food_pos[0] + cell_size // 2
    fy = food_pos[1] - cell_size // 2
    food.goto(fx, fy)
    food.showturtle()

# Fin del juego
def game_over():
    food.hideturtle()
    snake_pen.goto(0, 0)
    snake_pen.color("red")
    snake_pen.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    turtle.update()
    screen.bye()  # Cierra la ventana después de un juego terminado

# Bucle principal
def game_loop():
    move_snake()
    draw_snake()
    turtle.update()
    screen.ontimer(game_loop, snake_speed)

draw_grid()
spawn_food()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

game_loop()
screen.mainloop()
