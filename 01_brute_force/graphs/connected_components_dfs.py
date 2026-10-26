def connected_components_dfs(graph):
    """Count connected components in an undirected graph.
    
    Preconditions:
    Input is a symmetric adjacency dictionary with every vertex as a
    key, including isolated vertices. Vertex labels must be hashable.
    
    Result:
    Return the component count; an empty graph has zero components.
    """
    count = 0
    visit = {}
    for node in graph:
        visit[node] = 0

    def dfs(node):
        for neighbor in graph[node]:
            if visit[neighbor] == 0:
                visit[neighbor] =  1
                dfs(neighbor)

    for node in graph:
        if visit[node] == 0:
            visit[node] = 1
            dfs(node)
            count += 1

    return count
