import pygame

class Snake:

    def __init__(self, start_pos, r, g, b):
        # Si start_pos es None, crear cuerpo vacío
        if start_pos is None:
            self.body = []
        else:
            self.body = [start_pos]
        self.color = (r, g, b)
        self.grow = False

    @classmethod
    def from_data(cls, body, color, grow=False):
        # Crear instancia desde cuerpo completo y color
        snake = cls(start_pos=body[0], r=color[0], g=color[1], b=color[2])
        snake.body = body
        snake.grow = grow
        return snake

    def move(self, direction):
        # Calcular nueva cabeza según dirección
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

        # Insertar nueva cabeza al inicio del cuerpo
        self.body.insert(0, new_head)

        # Si no está creciendo, eliminar la cola
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        # Dibujar cabeza y cuerpo con distinto brillo
        for index, segment in enumerate(self.body):
            rect = pygame.Rect(
                segment[0] * 25 + 189,
                segment[1] * 25 + 189,
                23, 23
            )
            if index == 0:
                pygame.draw.rect(screen, self.color, rect)
            else:
                r, g, b = self.color
                dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
                pygame.draw.rect(screen, dark_color, rect)

    def check_collision(self, min_coord, max_coord):
        head = self.body[0]
        # Colisión con paredes
        if head[0] < min_coord or head[0] > max_coord or head[1] < min_coord or head[1] > max_coord:
            return True
        # Colisión consigo mismo
        if head in self.body[1:]:
            return True
        return False

    def eats(self, fruit_pos):
        # Verifica si la cabeza está sobre la fruta
        if self.body[0] == fruit_pos:
            self.grow = True
            return True
        return False

    def reverse(self, direction):
        # Obtener posición de cola
        x, y = self.body[-1]
        # Calcular nueva cola según dirección
        if direction == "UP":
            new_tail = (x, y - 1)
        elif direction == "DOWN":
            new_tail = (x, y + 1)
        elif direction == "LEFT":
            new_tail = (x - 1, y)
        elif direction == "RIGHT":
            new_tail = (x + 1, y)
        else:
            return

        # Agregar nueva cola al final
        self.body.append(new_tail)

        # Quitar cabeza a menos que crezca
        if not self.grow:
            self.body.pop(0)
        else:
            self.grow = False
