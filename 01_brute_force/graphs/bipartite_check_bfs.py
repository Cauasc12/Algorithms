from collections import deque

def bipartite_check_bfs(graph):

    """Check whether an undirected graph is bipartite using BFS.
    
    Preconditions:
    Input is a symmetric adjacency dictionary with every vertex as a
    key, including isolated vertices. Vertex labels must be hashable.
    
    Result:
    Return a boolean. Disconnected and empty graphs are supported;
    a self-loop makes the graph non-bipartite.
    """
    queue = deque()   
    color = {}
    for node in graph:
        color[node] = 0

    def bfs(node):
        while len(queue) != 0:
            front = queue.popleft()
            for neighbor in graph[front]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - color[front]
                    queue.append(neighbor)
                if color[neighbor] == color[front]:
                    return False
        return True

    for node in graph:
        if color[node] == 0:
            color[node] = 1
            queue.append(node)
            if not bfs(node):
                return False

    return True
