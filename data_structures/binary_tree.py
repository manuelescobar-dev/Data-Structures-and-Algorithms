from collections import deque


class BinaryTree:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

        def __str__(self) -> str:
            return str({"value": self.value, "left": self.left, "right": self.right})

        def __repr__(self) -> str:
            return str({"value": self.value, "left": self.left, "right": self.right})

    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        return self.traverse(self.root)

    def populate(self, array):
        for i in array:
            self.insert(i)

    def insert(self, value):
        new = self.Node(value)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                if value < current.value:
                    # LEFT
                    if current.left is None:
                        current.left = new
                        break
                    else:
                        current = current.left
                else:
                    # RIGHT
                    if current.right is None:
                        current.right = new
                        break
                    else:
                        current = current.right

    def lookup(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        return None

    def remove(self, value):
        parent = None
        current = self.root
        last_right = None
        while current:
            if value == current.value:
                if parent is None:
                    self.root = current.right
                    return current.right
                else:
                    sucessor = None
                    # Option 1: Only right child
                    if current.left is None and current.right is not None:
                        sucessor = current.right
                    # Option 2: Only left child
                    elif current.left is not None and current.right is None:
                        sucessor = current.left
                    # Option 3: Left and right child
                    elif current.left is not None and current.right is not None:
                        prev = None
                        sucessor = current.right
                        while sucessor.left is not None:
                            prev = sucessor
                            sucessor = sucessor.left
                        if prev is not None:
                            prev.left = sucessor.right
                            sucessor.right = current.right
                        else:
                            sucessor.right = None
                        sucessor.left = current.left
                    # Assign to parent the new sucessor
                    if last_right:
                        parent.right = sucessor
                    else:
                        parent.left = sucessor
                    return sucessor
            elif value < current.value:
                parent = current
                last_right = False
                current = current.left
            elif value > current.value:
                parent = current
                last_right = True
                current = current.right
        return None

    def traverse(self, initial, level=0):
        level = level + 1
        if level > 1:
            space = "        " * (level)
        else:
            space = "       "
        if initial.left is None and initial.right is None:
            return self.node_format(initial.value)
        elif initial.left is None:
            return (
                self.node_format(initial.value)
                + "\n"
                + space
                + "|->"
                + self.traverse(initial.right, level)
            )
        elif initial.right is None:
            return (
                self.node_format(initial.value)
                + "-->"
                + self.traverse(initial.left, level)
                + "\n"
                + space
            )
        else:
            return (
                self.node_format(initial.value)
                + "-->"
                + self.traverse(initial.left, level)
                + "\n"
                + space
                + "|->"
                + self.traverse(initial.right, level)
            )

    def node_format(self, value):
        if value < 10:
            return " ( " + str(value) + " ) "
        elif value < 100:
            return " (" + str(value) + " ) "
        else:
            return "(" + str(value) + ")"

    def bfs(self):
        visited = []
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.popleft()
            visited.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return visited

    def recursive_bfs(self):
        queue = deque()
        queue.append(self.root)
        visited = []
        return self.recursive_internal_bfs(queue, visited)

    def recursive_internal_bfs(self, queue, visited):
        if len(queue) == 0:
            return visited
        current = queue.popleft()
        visited.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
        return self.recursive_internal_bfs(queue, visited)

    def dfs(self):
        visited = []
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop()
            visited.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return visited

    def recursive_dfs(self, order="PreOrder"):
        def recursive_inorder_dfs(current):
            if current.left is None and current.right is None:
                return [current.value]
            elif current.left is None and current.right is not None:
                return [current.value] + recursive_inorder_dfs(current.right)
            elif current.left is not None and current.right is None:
                return recursive_inorder_dfs(current.left) + [current.value]
            else:
                return (
                    recursive_inorder_dfs(current.left)
                    + [current.value]
                    + recursive_inorder_dfs(current.right)
                )

        def recursive_preorder_dfs(current):
            if current.left is None and current.right is None:
                return [current.value]
            elif current.left is None and current.right is not None:
                return [current.value] + recursive_preorder_dfs(current.right)
            elif current.left is not None and current.right is None:
                return [current.value] + recursive_preorder_dfs(current.left)
            else:
                return (
                    [current.value]
                    + recursive_preorder_dfs(current.left)
                    + recursive_preorder_dfs(current.right)
                )

        def recursive_postorder_dfs(current):
            if current.left is None and current.right is None:
                return [current.value]
            elif current.left is None and current.right is not None:
                return recursive_postorder_dfs(current.right) + [current.value]
            elif current.left is not None and current.right is None:
                return recursive_postorder_dfs(current.left) + [current.value]
            else:
                return (
                    recursive_postorder_dfs(current.left)
                    + recursive_postorder_dfs(current.right)
                    + [current.value]
                )

        if order == "PreOrder":
            return recursive_preorder_dfs(self.root)
        elif order == "InOrder":
            return recursive_inorder_dfs(self.root)
        elif order == "PostOrder":
            return recursive_postorder_dfs(self.root)
