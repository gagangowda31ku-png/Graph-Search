class Graph:
    def __init__(self , num_nodes , edges):
        self.num_nodes = num_nodes
        self.data = [[] for i in range(num_nodes)]
        for n1 , n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def display(self):
        return [f"{n}: {nieghbor}" for n , nieghbor in enumerate(self.data)]

edges = [(0,1),(0,4) , (1,2) , (1,3), (1,4) , (2,3) , (3,4)]
graph = Graph(5 , edges)
graph.display()
print(graph.num_nodes)


def bfs(graph , root):
    discovered = [False] * graph.num_nodes
    queue = []

    queue.append(root)
    discovered[root] = True

    index = 0
    while index < len(queue):
        current = queue[index]
        index += 1

        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)

    return queue , discovered


result , discovered = bfs(graph , 3)
print(result)
print(discovered)







