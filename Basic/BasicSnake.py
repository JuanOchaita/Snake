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
    temp_stack = QueueStack(frames_history.Max)
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

def render_game(screen, grid, width, height, snake, ghost, ghost_visible, fruit, colisiones, score, font):
    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    if ghost_visible:
        ghost.draw(screen)
    draw_fruit(screen, fruit)

    # Mostrar contador colisiones y score
    col_text = font.render(f"Colisiones: {colisiones}", True, (255, 255, 255))
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    screen.blit(col_text, (10, 10))
    screen.blit(score_text, (10, 40))

    pygame.display.flip()

def draw_game_over_menu(screen, width, height, font, score, input_text):
    screen.fill((0, 0, 0))
    title = font.render("Has perdido", True, (255, 0, 0))
    score_text = font.render(f"Puntos finales: {score}", True, (255, 255, 255))
    prompt_text = font.render("Escribe tu nombre:", True, (255, 255, 255))
    name_text = font.render(input_text, True, (255, 255, 0))
    retry_text = font.render("Enter para guardar y reiniciar", True, (255, 255, 255))
    quit_text = font.render("Q para salir sin guardar", True, (255, 255, 255))

    screen.blit(title, (width//2 - title.get_width()//2, height//2 - 120))
    screen.blit(score_text, (width//2 - score_text.get_width()//2, height//2 - 80))
    screen.blit(prompt_text, (width//2 - prompt_text.get_width()//2, height//2 - 40))
    screen.blit(name_text, (width//2 - name_text.get_width()//2, height//2))
    screen.blit(retry_text, (width//2 - retry_text.get_width()//2, height//2 + 40))
    screen.blit(quit_text, (width//2 - quit_text.get_width()//2, height//2 + 80))
    pygame.display.flip()

def save_score(name, score, filename="scores.txt"):
    try:
        with open(filename, "a") as f:
            f.write(f"{name} {score}\n")
    except Exception as e:
        print(f"Error guardando la puntuación: {e}")

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

    font = pygame.font.SysFont("Arial", 24)

    snake = Snake((4, 4), 255, 255, 255)
    ghost = Snake(None, 100, 149, 237)

    fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)

    movement_history = QueueStack(10)
    frames_history = QueueStack(10)
    ghost_moves = Stack(10)

    direction = None
    ghost_visible = False
    replaying = False
    colisiones = 0
    score = 0

    game_over = False
    input_name = ""
    input_active = False

    frames_history.Push(snake.body.copy())

    while True:
        if game_over:
            if not input_active:
                input_active = True
                input_name = ""

            draw_game_over_menu(screen, width, height, font, score, input_name)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_name = input_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_name.strip() != "":
                            save_score(input_name.strip(), score)
                        # Reiniciar juego tras guardar o si nombre vacío
                        snake = Snake((4, 4), 255, 255, 255)
                        ghost = Snake(None, 100, 149, 237)
                        fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)
                        movement_history = QueueStack(10)
                        frames_history = QueueStack(10)
                        ghost_moves = Stack(10)
                        direction = None
                        ghost_visible = False
                        replaying = False
                        colisiones = 0
                        score = 0
                        game_over = False
                        input_active = False
                        frames_history.Push(snake.body.copy())
                        render_game(screen, grid, width, height, snake, ghost, ghost_visible, fruit, colisiones, score, font)
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        return
                    else:
                        if len(input_name) < 15 and event.unicode.isprintable():
                            input_name += event.unicode
            continue

        direction_input, quit_signal = (None, False) if replaying else handle_events(direction)
        if quit_signal:
            break
        if direction_input:
            direction = direction_input

        if direction:
            movement_history.Push(direction)
            frames_history.Push(snake.body.copy())

            snake.move(direction)

            next_move = ghost_moves.Pop()
            if next_move is not None:
                ghost.move(next_move)
                if ghost.check_collision(min_coord, max_coord, []):
                    ghost_visible = False
                else:
                    ghost_visible = True
            else:
                ghost_visible = False

            if snake.check_collision(min_coord, max_coord, ghost.body if ghost_visible else []):
                colisiones += 1

                if colisiones >= 2:
                    game_over = True
                    continue

                replaying = True
                last_body = show_replay(screen, grid, width, height, frames_history, snake, direction, opposites)
                replaying = False

                pygame.event.clear()

                fuera_de_limites = any(
                    x < min_coord or x > max_coord or y < min_coord or y > max_coord
                    for (x, y) in last_body
                )
                if fuera_de_limites:
                    last_body = [(grid // 2, grid // 2)]

                snake = Snake.from_data(last_body.copy(), (255, 255, 255))
                ghost = Snake.from_data(last_body.copy(), (100, 149, 237))
                
                fruit = generate_fruit(snake.body + ghost.body, min_coord, max_coord)

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
            score += 1  # Incrementar puntos al comer fruta

        render_game(screen, grid, width, height, snake, ghost, ghost_visible, fruit, colisiones, score, font)

        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()