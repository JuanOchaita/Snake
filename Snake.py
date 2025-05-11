# snake.py

class Snake:
    def __init__(self, start_position, up, down, right, left, color, block_size, play_area_rect):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.direction = right
        self.head_pos = list(start_position)
        self.body = [list(start_position),
                     [start_position[0] - block_size, start_position[1]],
                     [start_position[0] - 2 * block_size, start_position[1]]]
        self.score = 0
        self.color = color
        self.alive = True
        self.block_size = block_size    
        self.play_area_rect = play_area_rect


    def update_direction(self, change_to):
        if change_to == self.up and self.direction != self.down:
            self.direction = self.up
        elif change_to == self.down and self.direction != self.up:
            self.direction = self.down
        elif change_to == self.left and self.direction != self.right:
            self.direction = self.left
        elif change_to == self.right and self.direction != self.left:
            self.direction = self.right

    def move(self):
        if self.direction == self.up:
            self.head_pos[1] -= self.block_size
        elif self.direction == self.down:
            self.head_pos[1] += self.block_size
        elif self.direction == self.left:
            self.head_pos[0] -= self.block_size
        elif self.direction == self.right:
            self.head_pos[0] += self.block_size
        self.body.insert(0, list(self.head_pos))

    def check_food_collision(self, food_pos):
        if self.head_pos == food_pos:
            self.score += 1
            return True
        else:
            self.body.pop()
            return False

    def check_self_collision(self):
        return self.head_pos in self.body[1:]

    def check_border_collision(self):
        return not self.play_area_rect.collidepoint(self.head_pos)


    def get_head_position(self):
        return self.head_pos

    def get_body(self):
        return self.body

    def get_score(self):
        return self.score

    def draw(self, surface, pygame):
        for block in self.body:
            pygame.draw.rect(surface, self.color, pygame.Rect(block[0], block[1], self.block_size, self.block_size))
