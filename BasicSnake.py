import pygame
import random
from Snake import Snake
from Stack import Stack
from QueueStack import QueueStack

def draw_scene(screen, grid_size, width, height):
    padding = 2
    cell = 23
    grid_w = grid_size * cell + (grid_size - 1) * padding
    grid_h = grid_size * cell + (grid_size - 1) * padding
    start_x = (width - grid_w) // 2
    start_y = (height - grid_h) // 2

    screen.fill((34, 39, 56))
    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * (cell + padding)
            y = start_y + row * (cell + padding)
            pygame.draw.rect(screen, (24, 24, 37), pygame.Rect(x, y, cell, cell))

def generate_fruit(snake_body, min_coord, max_coord):
    while True:
        pos = (random.randint(min_coord, max_coord),
               random.randint(min_coord, max_coord))
        if pos not in snake_body:
            return pos

def is_opposite(dir1, dir2):
    return (dir1 == "UP" and dir2 == "DOWN") or \
           (dir1 == "DOWN" and dir2 == "UP") or \
           (dir1 == "LEFT" and dir2 == "RIGHT") or \
           (dir1 == "RIGHT" and dir2 == "LEFT")

def handle_events(current_direction):
    new_direction = current_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None, True

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                new_dir = "UP"
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                new_dir = "DOWN"
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                new_dir = "LEFT"
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                new_dir = "RIGHT"
            else:
                new_dir = None

            if new_dir and not is_opposite(current_direction, new_dir):
                new_direction = new_dir
    return new_direction, False

def draw_fruit(screen, fruit):
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))

def show_replay(screen, grid, width, height, freames_histroy, snake, direction, opposites):
    snake.reverse(opposites[direction])

    last_frame = None  # Variable para guardar el último frame

    while freames_histroy.Top != -1:
        frame = freames_histroy.Pop()
        last_frame = frame  # Guardar el frame actual

        draw_scene(screen, grid, width, height)

        for index, segment in enumerate(frame):
            x = segment[0] * 25 + 189
            y = segment[1] * 25 + 189
            rect = pygame.Rect(x, y, 23, 23)

            if index == 0:
                pygame.draw.rect(screen, snake.color, rect)
            else:
                r, g, b = snake.color
                dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
                pygame.draw.rect(screen, dark_color, rect)

        pygame.display.flip()
        pygame.time.delay(100)

    return last_frame

def render_game(screen, grid, width, height, snake, fruit, show_fruit=True):
    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    if show_fruit:
        draw_fruit(screen, fruit)
    pygame.display.flip()

def main():
    opposites = {
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
        "UP": "DOWN",
        "DOWN": "UP"
    }

    pygame.init()
    width, height = 601, 601
    grid = 9

    min_coord = -(grid - 9) // 2
    max_coord = (grid - 1) + min_coord

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")

    snake = Snake((4, 4), 255, 255, 255)
    fruit = generate_fruit(snake.body, min_coord, max_coord)

    movement_history = QueueStack(10)
    freames_histroy = QueueStack(10)

    render_game(screen, grid, width, height, snake, fruit)

    direction = None
    running = True
    freames_histroy.Push(snake.body.copy())

    while running:
        direction, quit_signal = handle_events(direction)
        if quit_signal:
            running = False
            break

        if direction:
            snake.move(direction)

        if snake.check_collision(min_coord, max_coord):
            new_body = show_replay(screen, grid, width, height, freames_histroy, snake, direction, opposites)

            # Reiniciar la serpiente con el cuerpo del último frame del replay
            snake = Snake(new_body[0], 255, 255, 255)
            snake.body = new_body.copy()

            # Generar una nueva fruta
            fruit = generate_fruit(snake.body, min_coord, max_coord)

            # Limpiar historial y agregar el estado actual
            freames_histroy = QueueStack(10)
            movement_history = QueueStack(10)
            freames_histroy.Push(snake.body.copy())

            # Resetear dirección
            direction = None

            # Continuar jugando
            continue

        if direction:
            freames_histroy.Push(snake.body.copy())
            movement_history.Push(direction)

        if snake.eats(fruit):
            fruit = generate_fruit(snake.body, min_coord, max_coord)

        render_game(screen, grid, width, height, snake, fruit)

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
