def bipartite_check_dfs(graph):

    """Check whether an undirected graph is bipartite using DFS.
    
    Preconditions:
    Input is a symmetric adjacency dictionary with every vertex as a
    key, including isolated vertices. Vertex labels must be hashable.
    
    Result:
    Return a boolean. Disconnected and empty graphs are supported;
    a self-loop makes the graph non-bipartite.
    """
    color = {}
    for node in graph:
        color[node] = 0

    def dfs(node):
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                color[neighbor] = 3 - color[node]
                if not dfs(neighbor):
                    return False
            if color[neighbor] == color[node]:
                return False
        return True
            
    for node in graph:
        if color[node] == 0:
            color[node] = 1
            if not dfs(node):
                return False

    return True
