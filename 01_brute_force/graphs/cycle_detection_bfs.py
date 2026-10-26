from collections import deque

def cycle_detection_bfs(graph):

    """Detect cycles in an undirected graph using BFS parent tracking.
    
    Preconditions:
    Input is a symmetric adjacency dictionary with every vertex as a
    key and no repeated neighbors. Self-loops are supported for ordinary
    labels. Known limitation: None collides with the root-parent sentinel.
    
    Result:
    Return a boolean. A self-loop on a vertex labeled None is currently
    missed; use other labels until the sentinel is corrected.
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
