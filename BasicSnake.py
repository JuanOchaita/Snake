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

    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
    pygame.display.flip()

    direction = None
    running = True
    freames_histroy.Push(snake.body.copy())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
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

                if new_dir and not is_opposite(direction, new_dir):
                    direction = new_dir

        if direction:
            snake.move(direction)

        if snake.check_collision(min_coord, max_coord):
            snake.reverse(opposites[direction])

            # Mostrar los últimos estados guardados visualmente (replay)
            while freames_histroy.Top != -1:
                frame = freames_histroy.Pop()
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
                pygame.time.delay(100)  # Velocidad del replay

            break  # Salir del bucle principal tras mostrar la animación

        if direction:
            freames_histroy.Push(snake.body.copy())
            movement_history.Push(direction)

        if snake.eats(fruit):
            fruit = generate_fruit(snake.body, min_coord, max_coord)

        draw_scene(screen, grid, width, height)
        snake.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
        pygame.display.flip()

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
