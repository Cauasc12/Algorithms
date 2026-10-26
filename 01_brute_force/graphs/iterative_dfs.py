def iterative_dfs(graph):

    """Traverse all graph components with an explicit DFS stack.
    
    Preconditions:
    Input is an adjacency dictionary containing every vertex as a key.
    Neighbor lists are ordered; vertex labels must be hashable.
    Directed and undirected graphs are supported.
    
    Result:
    Return each vertex once in DFS preorder. The LIFO stack explores
    neighbors in reverse adjacency-list order. An empty graph returns [].
    """
    stack = []
    visit = {}
    for node in graph:
        visit[node] = 0
    traversal_order = []
    
    for node in graph:
        if visit[node] == 0:
            stack.append(node)

            while len(stack) != 0:
                top = stack.pop()

                if visit[top] == 1:
                    continue
                
                traversal_order.append(top)
                visit[top] = 1

                for neighbor in graph[top]:
                    if visit[neighbor] == 0:
                        stack.append(neighbor)  

    return traversal_order