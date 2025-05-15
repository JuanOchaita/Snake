import pygame
import random
from PSnake import Snake

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

        # Check if the position is not the same as the head or any of the segments
        if pos != snake_body.head and \
           pos != snake_body.seg1 and \
           pos != snake_body.seg2 and \
           pos != snake_body.seg3 and \
           pos != snake_body.seg4 and \
           pos != snake_body.seg5 and \
           pos != snake_body.seg6 and \
           pos != snake_body.seg7 and \
           pos != snake_body.seg8 and \
           pos != snake_body.seg9 and \
           pos != snake_body.seg10 and \
           pos != snake_body.seg11 and \
           pos != snake_body.seg12 and \
           pos != snake_body.seg13 and \
           pos != snake_body.seg14 and \
           pos != snake_body.seg15 and \
           pos != snake_body.seg16 and \
           pos != snake_body.seg17 and \
           pos != snake_body.seg18 and \
           pos != snake_body.seg19 and \
           pos != snake_body.seg20 and \
           pos != snake_body.seg21 and \
           pos != snake_body.seg22 and \
           pos != snake_body.seg23 and \
           pos != snake_body.seg24 and \
           pos != snake_body.seg25 and \
           pos != snake_body.seg26 and \
           pos != snake_body.seg27 and \
           pos != snake_body.seg28 and \
           pos != snake_body.seg29 and \
           pos != snake_body.seg30 and \
           pos != snake_body.seg31 and \
           pos != snake_body.seg32 and \
           pos != snake_body.seg33 and \
           pos != snake_body.seg34 and \
           pos != snake_body.seg35 and \
           pos != snake_body.seg36 and \
           pos != snake_body.seg37 and \
           pos != snake_body.seg38 and \
           pos != snake_body.seg39 and \
           pos != snake_body.seg40 and \
           pos != snake_body.seg41 and \
           pos != snake_body.seg42 and \
           pos != snake_body.seg43 and \
           pos != snake_body.seg44 and \
           pos != snake_body.seg45 and \
           pos != snake_body.seg46 and \
           pos != snake_body.seg47 and \
           pos != snake_body.seg48 and \
           pos != snake_body.seg49 and \
           pos != snake_body.seg50 and \
           pos != snake_body.seg51 and \
           pos != snake_body.seg52 and \
           pos != snake_body.seg53 and \
           pos != snake_body.seg54 and \
           pos != snake_body.seg55 and \
           pos != snake_body.seg56 and \
           pos != snake_body.seg57 and \
           pos != snake_body.seg58 and \
           pos != snake_body.seg59 and \
           pos != snake_body.seg60 and \
           pos != snake_body.seg61 and \
           pos != snake_body.seg62 and \
           pos != snake_body.seg63 and \
           pos != snake_body.seg64 and \
           pos != snake_body.seg65 and \
           pos != snake_body.seg66 and \
           pos != snake_body.seg67 and \
           pos != snake_body.seg68 and \
           pos != snake_body.seg69 and \
           pos != snake_body.seg70 and \
           pos != snake_body.seg71 and \
           pos != snake_body.seg72 and \
           pos != snake_body.seg73 and \
           pos != snake_body.seg74 and \
           pos != snake_body.seg75 and \
           pos != snake_body.seg76 and \
           pos != snake_body.seg77 and \
           pos != snake_body.seg78 and \
           pos != snake_body.seg79 and \
           pos != snake_body.seg80:
            return pos

def is_opposite(dir1, dir2):

    # Return True if dir1 and dir2 are opposites
    return (dir1 == "UP" and dir2 == "DOWN") or \
           (dir1 == "DOWN" and dir2 == "UP") or \
           (dir1 == "LEFT" and dir2 == "RIGHT") or \
           (dir1 == "RIGHT" and dir2 == "LEFT")

def show_game_over(screen, font, score):
    screen.fill((0, 0, 0))

    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    rewind_text = font.render("Press Z to rewind a frame", True, (200, 200, 200))
    restart_text = font.render("Press R to restart", True, (200, 200, 200))
    quit_text = font.render("Press Q to quit", True, (200, 200, 200))

    screen.blit(game_over_text, (200, 150))
    screen.blit(score_text, (200, 200))
    screen.blit(rewind_text, (180, 260))
    screen.blit(restart_text, (180, 300))
    screen.blit(quit_text, (180, 340))

    pygame.display.flip()


def getGhostMove(snake2, snake1):
    if snake2.head[0] - snake1.head[0] == 1:
        return "LEFT"
    elif snake2.head[0] - snake1.head[0] == -1:
        return "RIGHT"
    elif snake2.head[1] - snake1.head[1] == 1:
        return "UP"
    elif snake2.head[1] - snake1.head[1] == -1:
        return "DOWN"
    else:
        return


def main():
    score = 0
    rewind_mode = False
    rewind_count = 9
    gm = False
    # Variables for rewind and ghost
    rewind_steps_remaining = 0  # Tracks remaining rewind moves
    current_ghost_move = None   # Next move for ghost
    show_ghost_snake = False    # Controls ghost visibility
    change = False              # Tracks if player diverged from ghost path

    pygame.init()
    width, height = 601, 601
    grid = 9

    min_coord = -(grid - 9) // 2
    max_coord = (grid - 1) + min_coord

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("SNAKE")
    
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 28)

    snake = Snake((4, 4), 255, 255, 255)
    Bsnake0 = None
    Bsnake1 = None
    Bsnake2 = None
    Bsnake3 = None
    Bsnake4 = None
    Bsnake5 = None
    Bsnake6 = None
    Bsnake7 = None
    Bsnake8 = None
    Bsnake9 = None
    Ghost = None
    fruit = generate_fruit(snake, min_coord, max_coord)

    # Initial draw
    draw_scene(screen, grid, width, height)
    snake.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0),
        pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

    direction = None
    running = True

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
                    if rewind_mode:
                        rewind_mode = False  # Resume normal game

        # Movement: Normal mode
        if direction and not rewind_steps_remaining:
            snake.move(direction)
            
        # Movement: Rewind mode (ghost active)
        elif direction and rewind_steps_remaining:
            snake.move(direction)
            
            if current_ghost_move and Ghost:
                Ghost.move(current_ghost_move)
                
                # Check if player's path has diverged
                if snake.head != Ghost.head or direction != current_ghost_move:
                    change = True
                
                rewind_steps_remaining -= 1
                if rewind_steps_remaining > 0:
                    # Update ghost's next move
                    if rewind_steps_remaining == 9:
                        current_ghost_move = getGhostMove(Bsnake0, Bsnake1)
                    elif rewind_steps_remaining == 8:
                        current_ghost_move = getGhostMove(Bsnake1, Bsnake2)
                    elif rewind_steps_remaining == 7:
                        current_ghost_move = getGhostMove(Bsnake2, Bsnake3)
                    elif rewind_steps_remaining == 6:
                        current_ghost_move = getGhostMove(Bsnake3, Bsnake4)
                    elif rewind_steps_remaining == 5:
                        current_ghost_move = getGhostMove(Bsnake4, Bsnake5)
                    elif rewind_steps_remaining == 4:
                        current_ghost_move = getGhostMove(Bsnake5, Bsnake6)
                    elif rewind_steps_remaining == 3:
                        current_ghost_move = getGhostMove(Bsnake6, Bsnake7)
                    elif rewind_steps_remaining == 2:
                        current_ghost_move = getGhostMove(Bsnake7, Bsnake8)
                    elif rewind_steps_remaining == 1:
                        current_ghost_move = getGhostMove(Bsnake8, Bsnake9)
                else:
                    # Rewind complete: hide ghost
                    show_ghost_snake = False
                    current_ghost_move = None
                    Ghost = None  # Clean up Ghost reference
                    change = False  # Reset change flag

        # Collision check
        ghost_collision = False
        if show_ghost_snake and Ghost and change:
            # Check if snake's head collides with any part of ghost
            if snake.head == Ghost.head or \
               snake.head == Ghost.seg1 or \
               snake.head == Ghost.seg2 or \
               snake.head == Ghost.seg3 or \
               snake.head == Ghost.seg4 or \
               snake.head == Ghost.seg5 or \
               snake.head == Ghost.seg6 or \
               snake.head == Ghost.seg7 or \
               snake.head == Ghost.seg8 or \
               snake.head == Ghost.seg9 or \
               snake.head == Ghost.seg10 or \
               snake.head == Ghost.seg11 or \
               snake.head == Ghost.seg12 or \
               snake.head == Ghost.seg13 or \
               snake.head == Ghost.seg14 or \
               snake.head == Ghost.seg15 or \
               snake.head == Ghost.seg16 or \
               snake.head == Ghost.seg17 or \
               snake.head == Ghost.seg18 or \
               snake.head == Ghost.seg19 or \
               snake.head == Ghost.seg20 or \
               snake.head == Ghost.seg21 or \
               snake.head == Ghost.seg22 or \
               snake.head == Ghost.seg23 or \
               snake.head == Ghost.seg24 or \
               snake.head == Ghost.seg25 or \
               snake.head == Ghost.seg26 or \
               snake.head == Ghost.seg27 or \
               snake.head == Ghost.seg28 or \
               snake.head == Ghost.seg29 or \
               snake.head == Ghost.seg30 or \
               snake.head == Ghost.seg31 or \
               snake.head == Ghost.seg32 or \
               snake.head == Ghost.seg33 or \
               snake.head == Ghost.seg34 or \
               snake.head == Ghost.seg35 or \
               snake.head == Ghost.seg36 or \
               snake.head == Ghost.seg37 or \
               snake.head == Ghost.seg38 or \
               snake.head == Ghost.seg39 or \
               snake.head == Ghost.seg40 or \
               snake.head == Ghost.seg41 or \
               snake.head == Ghost.seg42 or \
               snake.head == Ghost.seg43 or \
               snake.head == Ghost.seg44 or \
               snake.head == Ghost.seg45 or \
               snake.head == Ghost.seg46 or \
               snake.head == Ghost.seg47 or \
               snake.head == Ghost.seg48 or \
               snake.head == Ghost.seg49 or \
               snake.head == Ghost.seg50 or \
               snake.head == Ghost.seg51 or \
               snake.head == Ghost.seg52 or \
               snake.head == Ghost.seg53 or \
               snake.head == Ghost.seg54 or \
               snake.head == Ghost.seg55 or \
               snake.head == Ghost.seg56 or \
               snake.head == Ghost.seg57 or \
               snake.head == Ghost.seg58 or \
               snake.head == Ghost.seg59 or \
               snake.head == Ghost.seg60 or \
               snake.head == Ghost.seg61 or \
               snake.head == Ghost.seg62 or \
               snake.head == Ghost.seg63 or \
               snake.head == Ghost.seg64 or \
               snake.head == Ghost.seg65 or \
               snake.head == Ghost.seg66 or \
               snake.head == Ghost.seg67 or \
               snake.head == Ghost.seg68 or \
               snake.head == Ghost.seg69 or \
               snake.head == Ghost.seg70 or \
               snake.head == Ghost.seg71 or \
               snake.head == Ghost.seg72 or \
               snake.head == Ghost.seg73 or \
               snake.head == Ghost.seg74 or \
               snake.head == Ghost.seg75 or \
               snake.head == Ghost.seg76 or \
               snake.head == Ghost.seg77 or \
               snake.head == Ghost.seg78 or \
               snake.head == Ghost.seg79 or \
               snake.head == Ghost.seg80:
                ghost_collision = True

        if snake.check_collision(min_coord, max_coord) or ghost_collision:
            show_game_over(screen, font, score)
            gm = True
            
            while gm:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            return
                        elif event.key == pygame.K_r:
                            # Reset undo stack
                            Bsnake0 = None
                            Bsnake1 = None
                            Bsnake2 = None
                            Bsnake3 = None
                            Bsnake4 = None
                            Bsnake5 = None
                            Bsnake6 = None
                            Bsnake7 = None
                            Bsnake8 = None
                            Bsnake9 = None
                            main()  # Restart game
                            return
                        elif event.key == pygame.K_z:
                            if Bsnake9:
                                snake = Bsnake9.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake8:
                                snake = Bsnake8.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake7:
                                snake = Bsnake7.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake6:
                                snake = Bsnake6.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake5:
                                snake = Bsnake5.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake4:
                                snake = Bsnake4.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake3:
                                snake = Bsnake3.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake2:
                                snake = Bsnake2.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake1:
                                snake = Bsnake1.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)

                            if Bsnake0:
                                snake = Bsnake0.clone()
                                draw_scene(screen, grid, width, height)
                                snake.draw(screen)
                                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))
                                screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
                                pygame.display.flip()
                                pygame.time.delay(500)
                            
                            rewind_steps_remaining = 10
                            snake = Bsnake0.clone()
                            Ghost = Bsnake0.clone()
                            Ghost.color = (100, 149, 237)  # Light blue for ghost
                            show_ghost_snake = True
                            current_ghost_move = getGhostMove(Bsnake0, Bsnake1)
                            change = False  # Initialize change flag
                            gm = False
                            direction = None  # Reset direction

                pygame.time.delay(100)

        # Eating fruit
        if snake.eats(fruit):
            fruit = generate_fruit(snake, min_coord, max_coord)
            score += 1

        # Shift saved states (rewind memory) unless in rewind
        if not rewind_steps_remaining:
            if Bsnake9:
                Bsnake0 = Bsnake1
                Bsnake1 = Bsnake2
                Bsnake2 = Bsnake3
                Bsnake3 = Bsnake4
                Bsnake4 = Bsnake5
                Bsnake5 = Bsnake6
                Bsnake6 = Bsnake7
                Bsnake7 = Bsnake8
                Bsnake8 = Bsnake9
                Bsnake9 = snake.clone()
            else:
                # Fill from None upward
                if Bsnake0 is None: Bsnake0 = snake.clone()
                elif Bsnake1 is None: Bsnake1 = snake.clone()
                elif Bsnake2 is None: Bsnake2 = snake.clone()
                elif Bsnake3 is None: Bsnake3 = snake.clone()
                elif Bsnake4 is None: Bsnake4 = snake.clone()
                elif Bsnake5 is None: Bsnake5 = snake.clone()
                elif Bsnake6 is None: Bsnake6 = snake.clone()
                elif Bsnake7 is None: Bsnake7 = snake.clone()
                elif Bsnake8 is None: Bsnake8 = snake.clone()
                elif Bsnake9 is None: Bsnake9 = snake.clone()

        # Drawing block
        draw_scene(screen, grid, width, height)
        snake.draw(screen)
        if show_ghost_snake and Ghost:
            Ghost.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0),
            pygame.Rect(fruit[0]*25+189, fruit[1]*25+189, 23, 23))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()