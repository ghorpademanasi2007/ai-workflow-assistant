def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F", "G"],
    "F": ["C", "E"],
    "G": ["E"]
}

print("DFS Traversal:")
dfs(graph, "A")
print()
