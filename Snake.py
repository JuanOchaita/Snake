
import pygame

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
    
    def reverse(self, ):
        pass