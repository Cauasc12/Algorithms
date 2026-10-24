def iterative_dfs(graph):

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