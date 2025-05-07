import turtle

cell_size = 20
grid_size = 7
grid_length = cell_size * grid_size

screen = turtle.Screen()
screen.bgcolor("#1e1e2e")  # Fondo general
screen.title("Cuadrícula 21x21")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1)
pen.penup()

turtle.tracer(0, 0)

start_x = -grid_length / 2
start_y = grid_length / 2

# Dibujar los cuadrados blancos suaves
square_color = "#181825"  # Blanco suave

for row in range(grid_size):
    for col in range(grid_size):
        x = start_x + col * cell_size
        y = start_y - row * cell_size
        pen.goto(x, y)
        pen.pendown()
        pen.fillcolor(square_color)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(cell_size)
            pen.right(90)
        pen.end_fill()
        pen.penup()

# Dibujar líneas horizontales
pen.color("#232332")  # Color de las líneas
for i in range(grid_size + 1):
    y = start_y - i * cell_size
    pen.goto(start_x, y)
    pen.pendown()
    pen.goto(start_x + grid_length, y)
    pen.penup()

# Dibujar líneas verticales
for i in range(grid_size + 1):
    x = start_x + i * cell_size
    pen.goto(x, start_y)
    pen.pendown()
    pen.goto(x, start_y - grid_length)
    pen.penup()

# Dibujar el marco alrededor de la cuadrícula
pen.pensize(2)
pen.color("#1e1e2e")  # Color del marco
pen.goto(start_x, start_y)
pen.pendown()
pen.goto(start_x + grid_length, start_y)
pen.goto(start_x + grid_length, start_y - grid_length)
pen.goto(start_x, start_y - grid_length)
pen.goto(start_x, start_y)
pen.penup()

turtle.update()
turtle.done()
