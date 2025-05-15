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

def show_replay(screen, grid, width, height, frames_history, snake, direction, opposites):
    # Hacemos una copia para no modificar el original
    temp_stack = QueueStack(frames_history.Max)
    # Pasamos los frames para mostrar (copiando)
    for i in range(frames_history.Top + 1):
        temp_stack.Push(frames_history.Elements[i])

    snake.reverse(opposites[direction])

    last_frame = None

    while temp_stack.Top != -1:
        frame = temp_stack.Pop()
        last_frame = frame

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
    min_coord = 0
    max_coord = grid - 1

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")

    snake = Snake((4, 4), 255, 255, 255)
    ghost = Snake(None, 100, 149, 237)

    fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)

    movement_history = QueueStack(10)
    frames_history = QueueStack(10)
    ghost_moves = Stack(10)

    direction = None
    ghost_visible = False

    render_game(screen, grid, width, height, snake, fruit)

    running = True
    frames_history.Push(snake.body.copy())

    while running:
        direction_input, quit_signal = handle_events(direction)
        if quit_signal:
            break
        if direction_input:
            direction = direction_input

        if direction:
            # Guardar antes de moverse
            movement_history.Push(direction)
            frames_history.Push(snake.body.copy())

            snake.move(direction)

            # Mover ghost si tiene movimientos
            next_move = ghost_moves.Pop()
            if next_move is not None:
                ghost.move(next_move)
                if ghost.check_collision(min_coord, max_coord):
                    ghost_visible = False
                else:
                    ghost_visible = True
            else:
                ghost_visible = False

            # Verificar colisión del snake
            if snake.check_collision(min_coord, max_coord):
                last_body = show_replay(screen, grid, width, height, frames_history, snake, direction, opposites)

                snake = Snake(last_body[0], 255, 255, 255)
                snake.body = last_body.copy()

                ghost = Snake(last_body[0], 100, 149, 237)
                ghost.body = last_body.copy()

                fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)

                # Copiar movimientos del snake al ghost
                ghost_moves = Stack(10)
                for i in range(movement_history.Top, -1, -1):
                    move = movement_history.Elements[i]
                    if move is not None:
                        ghost_moves.Push(move)

                movement_history = QueueStack(10)
                frames_history = QueueStack(10)
                frames_history.Push(snake.body.copy())
                direction = None
                ghost_visible = ghost_moves.Top != -1
                continue

        if snake.eats(fruit):
            fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)

        draw_scene(screen, grid, width, height)
        snake.draw(screen)
        if ghost_visible:
            ghost.draw(screen)
        draw_fruit(screen, fruit)
        pygame.display.flip()

        pygame.time.delay(100)

    pygame.quit()


















if __name__ == "__main__":
    main()