import pygame

def main():
    
    grid_size = 9
    
    # Inicializa Pygame
    pygame.init()

    # Define dimensiones de la ventana
    width, height = 601, 601

    # Crea la ventana
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")

    # Parámetros de la cuadrícula
    cell_size = 23  # tamaño de cada celda
    padding = 2     # espacio entre celdas

    # Calcula el tamaño total de la cuadrícula
    grid_width = grid_size * cell_size + (grid_size - 1) * padding
    grid_height = grid_size * cell_size + (grid_size - 1) * padding

    # Calcula la posición inicial para centrar la cuadrícula
    start_x = (width - grid_width) // 2
    start_y = (height - grid_height) // 2

    # Rellena la pantalla con color negro
    screen.fill((34, 39, 56))

    # Dibuja la cuadrícula 5x5 centrada
    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * (cell_size + padding)
            y = start_y + row * (cell_size + padding)
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (24, 24, 37), rect)
                        
    # Bucle principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualiza la pantalla
        pygame.display.flip()

    # Finaliza Pygame
    pygame.quit()

def draw_score(screen, score, width):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width // 2, 30))
    screen.blit(score_text, score_rect)

if __name__ == "__main__":
    main()