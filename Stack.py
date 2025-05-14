
class Stack:
    
    def __init__(self, size: int):
        
        self.Top = -1
        self.Max = size
        self.Elements = [None] * size

    def __repr__(self):
        
        return f"Current stack: {self.Elements} | Top: {self.Top}"

    def Push(self, value: int) -> None:
        
        if self.Top == self.Max -1:
            print("OVERFLOW :/")
            return None
    
        self.Top += 1
        self.Elements[self.Top] = value

    def Pop(self) -> any:
        
        if self.Top == -1:
            print("Stack Underflow")
            return None
    
        value = self.Elements[self.Top]
        self.Elements[self.Top] = None
        self.Top -= 1
        return value

    def Peek(self) -> any:
        
        if self.Top == -1:
            print("Stack underflow")
            return None
        
        return self.Elements[self.Top]