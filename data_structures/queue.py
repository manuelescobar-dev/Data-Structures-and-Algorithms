class Queue:
    class Node:
        def __init__(self, value, link) -> None:
            self.value = value
            self.link = link

    def __init__(self) -> None:
        self.last = None
        self.first = None
        self.length = 0

    def __str__(self) -> str:
        out = "first"
        entry = self.first
        while entry is not None:
            out += " -> " + str(entry.value)
            entry = entry.link
        return out + " -> last"

    def enqueue(self, value):
        newNode = self.Node(value, None)
        if self.length == 0:
            self.first = newNode
        else:
            self.last.link = newNode
        self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception("Empty Stack!")
        else:
            self.first = self.first.link
            if self.length == 1:
                self.last = None
            self.length -= 1

    def peek(self):
        if self.first is None:
            return None
        else:
            return self.first.value
