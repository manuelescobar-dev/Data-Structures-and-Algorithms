class Graph:
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        if node in self.adjacentList:
            raise Exception("Vertex already exists!")
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adjacentList and node2 not in self.adjacentList:
            raise Exception("One of the two vertexes do not exist!")
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def show_connections(self):
        for i in self.adjacentList:
            print(i + " ---> " + str(self.adjacentList[i]))
