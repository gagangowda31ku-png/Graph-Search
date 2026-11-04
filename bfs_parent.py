class Graph:
    def __init__(self , num_nodes , edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.data = [[] for _ in range(num_nodes)]
    def display(self):
        for n1 , n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def report(self):
        return [f'{n} : {neighbour}' for n , neighbour in enumerate(self.data)]

edges = [(0,1),(0,4) , (1,2) , (1,3), (1,4) , (2,3) , (3,4)]

graph = Graph(5 , edges)
graph.display()
def bfs(graph , root):
    queue = []
    discovered = [False]* len(graph.data)
    distance = [None]*len(graph.data)
    parent = [None]*len(graph.data)

    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1

        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current

                discovered[node] = True
                queue.append(node)
    return discovered , distance , parent
print(bfs(graph , 3))     



