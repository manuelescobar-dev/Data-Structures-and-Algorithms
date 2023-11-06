class LinkedList:
    class Node:
        def __init__(self, value, link):
            self.value = value
            self.link = link

        def __repr__(self) -> str:
            return str({"value": self.value, "link": self.link})

        def __str__(self) -> str:
            return str({"value": self.value, "link": self.link})

    def __init__(self, value):
        self.head = self.Node(value, None)
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        out = ""
        entry = self.head
        while entry is not None:
            out += str(entry.value) + "->"
            entry = entry.link
        return out

    def append(self, value):
        newNode = self.Node(value, None)
        self.tail.link = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = self.Node(value, self.head)
        self.head = newNode
        self.length += 1

    def traverse(self, position):
        if position < 0 or position >= self.length:
            raise Exception("Invalid positions while traversing")
        entry = self.head
        for i in range(1, position + 1, 1):
            entry = entry.link
        return entry

    def insert(self, value, position):
        if position > self.length:
            raise Exception("Invalid position")
        elif position == self.length:
            self.append(value)
        elif position == 0:
            self.prepend(value)
        else:
            previous = self.traverse(position - 1)
            newNode = self.Node(value, previous.link)
            previous.link = newNode
        self.length += 1

    def remove(self, position):
        if position >= self.length:
            raise Exception("Invalid position")
        elif position == 0:
            self.head = self.head.link
        else:
            previous = self.traverse(position - 1)
            nxt = previous.link
            previous.link = nxt.link
            if position == self.length - 1:
                self.tail = previous
        self.length -= 1

    def reverse(self):
        prev = None
        current = self.head
        self.head, self.tail = self.tail, self.head
        for i in range(self.length - 1):
            current.link, current, prev = prev, current.link, current


class DoubleLinkedList:
    class Node:
        def __init__(self, value, plink, nlink):
            self.value = value
            self.plink = plink
            self.nlink = nlink

        def __repr__(self) -> str:
            return str({"value": self.value, "link": self.nlink})

        def __str__(self) -> str:
            return str({"value": self.value, "link": self.nlink})

    def __init__(self, value):
        self.head = self.Node(value, None, None)
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        out = ""
        entry = self.head
        while entry is not None:
            out += str(entry.value) + "<->"
            entry = entry.nlink
        return out

    def append(self, value):
        newNode = self.Node(value, self.tail, None)
        self.tail.nlink = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = self.Node(value, None, self.head)
        self.head.plink = newNode
        self.head = newNode
        self.length += 1

    def traverse_forward(self, position):
        if position < 0 or position >= self.length:
            raise Exception("Invalid positions while traversing")
        entry = self.head
        for i in range(0, position, 1):
            entry = entry.nlink
        return entry

    def traverse_backward(self, position):
        if position < 0 or position >= self.length:
            raise Exception("Invalid positions while traversing")
        entry = self.tail
        for i in range(self.length - 1, position, -1):
            entry = entry.plink
        return entry

    def insert(self, value, position):
        if position > self.length:
            raise Exception("Invalid position")
        elif position == self.length:
            self.append(value)
        elif position == 0:
            self.prepend(value)
        else:
            if position < self.length / 2:
                follower = self.traverse_forward(position)
            else:
                follower = self.traverse_backward(position)
            leading = follower.plink
            newNode = self.Node(value, leading, follower)
            leading.nlink = newNode
            follower.plink = newNode
        self.length += 1

    def remove(self, position):
        if position >= self.length:
            raise Exception("Invalid position")
        elif position == 0:
            self.head = self.head.nlink
            self.head.plink = None
        elif position == self.length - 1:
            self.tail = self.tail.plink
            self.tail.nlink = None
        else:
            if position < self.length / 2:
                element = self.traverse_forward(position)
            else:
                element = self.traverse_backward(position)
            follower = element.nlink
            leading = element.plink
            follower.plink = leading
            leading.nlink = follower
        self.length -= 1
