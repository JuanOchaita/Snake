class QueueStack:
    
    def __init__(self, size: int):
        self.Top = -1
        self.Max = size
        self.Elements = [None] * size

    def __repr__(self):
        return f"Current stack: {self.Elements} | Top: {self.Top}"

    def Push(self, value: int) -> None:

        if value is None:
            return  # Ignorar valores None

        if self.Top == self.Max - 1:
            # Realizar un desplazamiento hacia la izquierda
            for i in range(1, self.Max):
                self.Elements[i - 1] = self.Elements[i]
            
            # Colocar el nuevo valor en la última posición
            self.Elements[self.Max - 1] = value
        else:
            # Si hay espacio, simplemente agregar el valor al final
            self.Top += 1
            self.Elements[self.Top] = value

    def Pop(self) -> any:
        # Buscar el último valor no None en el stack
        for i in range(self.Top, -1, -1):
            if self.Elements[i] is not None:
                value = self.Elements[i]
                self.Elements[i] = None  # Eliminar el valor del stack
                self.Top = i - 1  # Ajustar el índice de Top
                return value
        return None

    def Peek(self) -> any:
        # Buscar el último valor no None en el stack
        for i in range(self.Top, -1, -1):
            if self.Elements[i] is not None:
                return self.Elements[i]
        return None
