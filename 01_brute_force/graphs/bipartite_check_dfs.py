def bipartite_check_dfs(graph):

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
