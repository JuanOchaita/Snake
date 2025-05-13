import pygame
import random

class Snake:

    def __init__(self, position, R, G, B):

        self.body = [position]
        self.color = (R, G, B)
        self.direction = None
        self.grow = False

    def move(self, dir_str):

        x, y = self.body[0]

        if dir_str == "UP": new_head = (x, y - 1)
        elif dir_str == "DOWN": new_head = (x, y + 1)
        elif dir_str == "LEFT": new_head = (x - 1, y)
        elif dir_str == "RIGHT": new_head = (x + 1, y)
        else: return

        self.body.insert(0, new_head)

        if not self.grow: self.body.pop()
        else: self.grow = False

    def draw(self, screen):
        
        for square in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(((square[0]) * 25) + 189, ((square[1]) * 25) + 189, 23, 23))

    def check_collision(self, min_map, max_map):

        x, y = self.body[0]
        if x < min_map or x > max_map or y < min_map or y > max_map: return True
        if self.body[0] in self.body[1:]: return True
        return False

    def eats(self, fruit_pos):

        if self.body[0] == fruit_pos:
            self.grow = True
            return True
        return False


def scene(screen, grid_size, width, height):

    padding = 2
    cell_size = 23

    grid_width = grid_size * cell_size + (grid_size - 1) * padding
    grid_height = grid_size * cell_size + (grid_size - 1) * padding
    start_x = (width - grid_width) // 2
    start_y = (height - grid_height) // 2
    screen.fill((34, 39, 56))

    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * (cell_size + padding)
            y = start_y + row * (cell_size + padding)
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (24, 24, 37), rect)

def generate_fruit(snake_body, min_map, max_map):

    while True:
        x = random.randint(min_map, max_map)
        y = random.randint(min_map, max_map)
        if (x, y) not in snake_body:
            return (x, y)

def main():

    pygame.init()
    width, height = 601, 601
    map_size = 11

    min_map = -(map_size - 9) // 2
    max_map = (map_size - 1) + min_map

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")

    snake = Snake((4, 4), 255, 255, 255)
    fruit = generate_fruit(snake.body, min_map, max_map)

    scene(screen, map_size, width, height)
    snake.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(((fruit[0]) * 25) + 189, ((fruit[1]) * 25) + 189, 23, 23))
    pygame.display.flip()

    direction = None
    running = True
    
    # Main Code 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP): direction = "UP"
                elif event.key in (pygame.K_s, pygame.K_DOWN): direction = "DOWN"
                elif event.key in (pygame.K_a, pygame.K_LEFT): direction = "LEFT"
                elif event.key in (pygame.K_d, pygame.K_RIGHT): direction = "RIGHT"

        if direction:
            snake.move(direction)

            if snake.check_collision(min_map, max_map):
                running = False
                break

            if snake.eats(fruit):
                fruit = generate_fruit(snake.body, min_map, max_map)

            scene(screen, map_size, width, height)
            snake.draw(screen)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(((fruit[0]) * 25) + 189, ((fruit[1]) * 25) + 189, 23, 23))
            pygame.display.flip()

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
