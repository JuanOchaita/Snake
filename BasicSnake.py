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

def death_moves(history: QueueStack):
    inverse = Stack(history.Max)
    inverse_opposite = Stack(history.Max)

    opposites = {
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
        "UP": "DOWN",
        "DOWN": "UP"
    }

    # Copiamos los elementos directamente sin tocar el stack original
    original_elements = history.Elements.copy()

    # Recorremos en orden inverso
    for i in range(history.Max - 1, -1, -1):
        move = original_elements[i]
        inverse.Push(move)
        if move in opposites:
            inverse_opposite.Push(opposites[move])
        else:
            inverse_opposite.Push(None)

    return inverse, inverse_opposite


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

    movement_history = QueueStack(10)

    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0),
    pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
    pygame.display.flip()

    direction = None

    while True:
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
            ghost_moves, back_to_past_moves = death_moves(movement_history)
            print(movement_history)
            print(ghost_moves)
            print(back_to_past_moves)

            # Back Time
            snake.reverse()



            break

        if direction:
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
