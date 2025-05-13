import pygame
import random

class Snake:

    def __init__(self, start_pos, r, g, b):
        # Initialize snake's body, base color, and growth flag
        self.body = [start_pos]
        self.color = (r, g, b)
        self.grow = False

    def move(self, direction):
        # Compute new head based on direction
        x, y = self.body[0]
        if direction == "UP":
            new_head = (x, y - 1)
        elif direction == "DOWN":
            new_head = (x, y + 1)
        elif direction == "LEFT":
            new_head = (x - 1, y)
        elif direction == "RIGHT":
            new_head = (x + 1, y)
        else:
            return

        # Insert new head
        self.body.insert(0, new_head)

        # Remove tail unless we're growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        # Draw the head with full color and the body segments with a darker shade
        for index, segment in enumerate(self.body):
            # Calculate rectangle position
            rect = pygame.Rect(
                segment[0] * 25 + 189,
                segment[1] * 25 + 189,
                23, 23
            )
            if index == 0:
                # Draw head with full color
                pygame.draw.rect(screen, self.color, rect)
            else:
                # Draw body segment with 80% brightness
                r, g, b = self.color
                dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
                pygame.draw.rect(screen, dark_color, rect)

    def check_collision(self, min_coord, max_coord):
        # Check wall collision for head
        head = self.body[0]
        if head[0] < min_coord or head[0] > max_coord or head[1] < min_coord or head[1] > max_coord:
            return True
        # Check self-collision
        if head in self.body[1:]:
            return True
        return False

    def eats(self, fruit_pos):
        # Check if head is on fruit
        if self.body[0] == fruit_pos:
            self.grow = True
            return True
        return False


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
    grid = 11

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

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # map key to direction
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

                # only update if not opposite to current direction
                if new_dir and not is_opposite(direction, new_dir):
                    direction = new_dir


        # always move in current direction
        snake.move(direction)

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

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
 