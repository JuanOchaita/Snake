import pygame
import random
from Snake import Snake

def draw_scene(screen, grid_size, width, height):

    # Draw background and grid
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

    # Place fruit at random position not occupied by snake
    while True:
        pos = (random.randint(min_coord, max_coord),
               random.randint(min_coord, max_coord))
        if pos not in snake_body:
            return pos

def is_opposite(dir1, dir2):

    # Return True if dir1 and dir2 are opposites
    return (dir1 == "UP" and dir2 == "DOWN") or \
           (dir1 == "DOWN" and dir2 == "UP") or \
           (dir1 == "LEFT" and dir2 == "RIGHT") or \
           (dir1 == "RIGHT" and dir2 == "LEFT")

def main():

    pygame.init()
    width, height = 601, 601
    grid = 9

    min_coord = -(grid - 9) // 2
    max_coord = (grid - 1) + min_coord

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")

    snake = Snake((4, 4), 255, 255, 255)
    fruit = generate_fruit(snake.body, min_coord, max_coord)

    # initial draw
    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
    pygame.display.flip()

    direction = None
    running = True

    comandos = ["LEFT", "UP", "RIGHT", "RIGHT", "DOWN", "DOWN", "LEFT", "LEFT", "RIGHT", "RIGHT", "UP", "UP", "LEFT", "LEFT", "DOWN", "RIGHT"]

    while running:

        # always move in current direction
        for comand in comandos:
            snake.move(comand)

            # collision check
            if snake.check_collision(min_coord, max_coord):
                break

            # eating fruit
            if snake.eats(fruit):
                fruit = generate_fruit(snake.body, min_coord, max_coord)

            # redraw everything
            draw_scene(screen, grid, width, height)
            snake.draw(screen)
            pygame.draw.rect(screen, (255, 0, 0),
            pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
            pygame.display.flip()

            pygame.time.delay(500)

    pygame.quit()

if __name__ == "__main__":
    main()
 