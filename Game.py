import pygame, sys, time, random
from Snake import Snake

# Configuración
difficulty = 5
frame_size_x = 601
frame_size_y = 601
block_size = 25

# Tamaño del área jugable (cuadrado centrado)
play_area_size = 25*9
play_area_x = (frame_size_x - play_area_size) // 2
play_area_y = (frame_size_y - play_area_size) // 2
play_area_rect = pygame.Rect(play_area_x, play_area_y, play_area_size, play_area_size)

pygame.init()
pygame.display.set_caption('Snake 2 Players')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
fps_controller = pygame.time.Clock()

# Colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Mostrar puntajes
def show_score(snake1, snake2):
    font = pygame.font.SysFont('consolas', 20)
    s1 = font.render('P1 Score: ' + str(snake1.get_score()), True, green)
    s2 = font.render('P2 Score: ' + str(snake2.get_score()), True, blue)
    game_window.blit(s1, (10, 10))
    game_window.blit(s2, (frame_size_x - 150, 10))

# Game Over
def game_over():
    font = pygame.font.SysFont('times new roman', 80)
    surface = font.render('GAME OVER', True, red)
    rect = surface.get_rect(center=(frame_size_x // 2, frame_size_y // 2))
    game_window.blit(surface, rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Crear jugadores dentro del área de juego
snake1 = Snake([play_area_x + 50, play_area_y + 50], 'W', 'S', 'D', 'A', green, block_size, play_area_rect)
snake2 = Snake([play_area_x + 100, play_area_y + 100], 'UP', 'DOWN', 'RIGHT', 'LEFT', blue, block_size, play_area_rect)

# Comida dentro del marco
def spawn_food():
    max_blocks = play_area_size // block_size
    food_x = play_area_x + random.randint(0, max_blocks - 1) * block_size
    food_y = play_area_y + random.randint(0, max_blocks - 1) * block_size
    return [food_x, food_y]

food_pos = spawn_food()
food_spawn = True

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: snake1.update_direction('W')
            elif event.key == pygame.K_s: snake1.update_direction('S')
            elif event.key == pygame.K_a: snake1.update_direction('A')
            elif event.key == pygame.K_d: snake1.update_direction('D')
            elif event.key == pygame.K_UP: snake2.update_direction('UP')
            elif event.key == pygame.K_DOWN: snake2.update_direction('DOWN')
            elif event.key == pygame.K_LEFT: snake2.update_direction('LEFT')
            elif event.key == pygame.K_RIGHT: snake2.update_direction('RIGHT')

    game_window.fill(black)

    # Dibujar marco
    pygame.draw.rect(game_window, white, play_area_rect, 2)

    # Mover serpientes
    for snake in [snake1, snake2]:
        if snake.alive:
            snake.move()
            if snake.check_food_collision(food_pos):
                food_spawn = False

    if not food_spawn:
        food_pos = spawn_food()
    food_spawn = True

    # Dibujar comida
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

    # Verificar colisiones
    for snake in [snake1, snake2]:
        if not snake.alive:
            continue
        if snake.check_self_collision() or not play_area_rect.collidepoint(snake.get_head_position()):
            snake.alive = False
        other = snake2 if snake == snake1 else snake1
        if snake.get_head_position() in other.get_body():
            snake.alive = False

    # Dibujar serpientes y puntaje
    snake1.draw(game_window, pygame)
    snake2.draw(game_window, pygame)
    show_score(snake1, snake2)

    pygame.display.update()

    if not snake1.alive and not snake2.alive:
        game_over()

    fps_controller.tick(difficulty)
