from collections import deque

def cycle_detection_bfs(graph):

    queue = deque()
    visit = {}
    for node in graph:
        visit[node] = 0
    parent = {}
    for node in graph:
        parent[node] = None

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
