def connected_components_dfs(graph):
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
