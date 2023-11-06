class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]
