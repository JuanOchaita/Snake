import pygame

def snake(grid_size, padding, cell_size):
    pass

def map_area():
    pass

def scene(screen, grid_size, width, height):

    padding = 2     # espacio entre celdas
    cell_size = 23  # tamaño de cada celda

    grid_width = grid_size * cell_size + (grid_size - 1) * padding
    grid_height = grid_size * cell_size + (grid_size - 1) * padding
    start_x = (width - grid_width) // 2
    start_y = (height - grid_height) // 2
    screen.fill((34, 39, 56))

    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * (cell_size + padding)
            y = start_y + row * (cell_size + padding)
            print(x, y, cell_size, cell_size)
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (24, 24, 37), rect)

def print_body(screen, snake):
    for square in snake:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(((square[0]) * 25) + 189, ((square[1]) * 25) + 189, 23, 23))
    pass

def main():

    pygame.init()
    width, height = 601, 601
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")
    scene(screen, 9, 601, 601)

    Snake = [(4, 4)]
    scene(screen, 9, 601, 601)
    print_body(screen, Snake)

    # Main 
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:

                # Movements
                if event.key == pygame.K_w: Head = (Snake[0][0], Snake[0][1] - 1)
                elif event.key == pygame.K_s: Head = (Snake[0][0], Snake[0][1] + 1)
                elif event.key == pygame.K_a: Head = (Snake[0][0] - 1, Snake[0][1])
                elif event.key == pygame.K_d: Head = (Snake[0][0] + 1, Snake[0][1])
                elif event.key == pygame.K_UP: Head = (Snake[0][0], Snake[0][1] - 1)
                elif event.key == pygame.K_DOWN: Head = (Snake[0][0], Snake[0][1] + 1)
                elif event.key == pygame.K_LEFT: Head = (Snake[0][0] - 1, Snake[0][1])
                elif event.key == pygame.K_RIGHT: Head = (Snake[0][0] + 1, Snake[0][1])
                Snake.insert(0, Head)

                if Snake[0][0] < 0 or  8 < Snake[0][0]:
                    running = False
                    break

                print_body(screen, Snake)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
