def topological_search_dfs(graph):
    """Find a topological ordering through DFS finishing times.
    
    Preconditions:
    Input is a directed adjacency dictionary containing every vertex
    as a key, including sinks and isolated vertices.
    
    Result:
    Return an ordering for a DAG. On a cycle, print a message and
    return None. An empty graph returns [].
    """
    n = len(graph)
    order = [None] * n
    count = n-1
    
    visits = {}
    for node in graph:
        visits[node] = 0

    cyclic = False

    def dfs(node):
        nonlocal count, cyclic

        for adjacent in graph[node]:
            if(visits[adjacent] == 1):
                cyclic = True
                return cyclic
            
            if(visits[adjacent] == 0):
                visits[adjacent] = 1
                dfs(adjacent)
                if(cyclic):
                    return

        order[count] = node
        count -= 1
        visits[node] = 2

    for node in graph:
        if(visits[node] == 0):
            dfs(node)
            if(cyclic):
                print("Graph is cyclic")
                return None

    return order
