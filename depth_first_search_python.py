graph = {
    'A': ['C', 'B', 'F'],
    'B': ['D', 'G'],
    'C': ['D'],
    'D': ['E'],
    'E': ['C'],
    'F': ['E'],
    'G': ['F', 'E']
}

def print_graph(_graph):
    for vertex in _graph:
        print("Vertex", vertex, end=" ")
        for i in _graph[vertex]:
            print("->", i, end=" ")
        print()

def DFS(_graph, start):
    stack = []
    # visited: 1, pending: 0, not visited: -1
    visited = {
        'A': -1,
        'B': -1,
        'C': -1,
        'D': -1,
        'E': -1,
        'F': -1,
        'G': -1
    }
    stack.append(start)
    print('DFS', end=" ")
    while(stack):
        now_vertex = stack.pop()
        print('->', now_vertex, end=" ")
        for i in _graph[now_vertex]:
            if visited[i] == -1:
                stack.append(i)
                visited[i] = 0
        visited[now_vertex] = 1


print_graph(graph)
DFS(graph, 'A')