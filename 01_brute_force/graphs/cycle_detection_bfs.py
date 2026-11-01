from collections import deque

def cycle_detection_bfs(graph):

    """Detect cycles in an undirected graph using BFS parent tracking.
    
    Preconditions:
    Input is a symmetric adjacency dictionary with every vertex as a
    key and no repeated neighbors. Self-loops are cycles, including a
    self-loop on a vertex labeled None. The root parent is a unique
    sentinel object, so None remains a valid vertex label.
    
    Result:
    Return a boolean.
    """
    queue = deque()
    visit = {}
    for node in graph:
        visit[node] = 0
    parent = {}
    root_parent = object()
    for node in graph:
        parent[node] = root_parent

    def bfs(node):
        while len(queue) != 0:
            front = queue.popleft()
            for neighbor in graph[front]:
                if visit[neighbor] == 0:
                    visit[neighbor] = 1
                    parent[neighbor] = front
                    queue.append(neighbor)
                elif neighbor != parent[front]:
                    return  True
                
        return False
                    
    for node in graph:
        if visit[node] == 0:
            visit[node] = 1
            queue.append(node)
            if bfs(node):
                return True

    return False
