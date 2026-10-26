def topological_sort_kahn(graph):
    """Order a directed graph using source removal.
    
    Preconditions:
    Input is an adjacency dictionary containing every vertex as a key,
    including sinks and isolated vertices. A full ordering exists only
    for an acyclic graph.
    
    Result:
    Return a vertex ordering for a DAG. On a cycle, print a message
    and return 1. An empty graph returns [].
    """
    in_degree = {}
    for node in graph:
        in_degree[node] = 0
    for node in graph:
        for adjacent in graph[node]:
            in_degree[adjacent] += 1

    source = []
    for node in graph:
        if(in_degree[node] == 0):
            source.append(node)

    order = []
    while len(source) != 0:
        node = source.pop()
        order.append(node)

        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if(in_degree[adjacent] == 0):
                source.append(adjacent)

    if(len(order) < len(graph)):
        print("Graph is cyclic")
        return 1
    else:
        return order