def cycle_length_3(G):

    neighbors = {}
    for u, adj in G.items():
        neighbors[u] = set(adj)

    for u in G:
        for v in G[u]:  
            if u < v:
                if len(G[u]) < len(G[v]):
                    smaller, larger = u, v
                else:
                    smaller, larger = v, u

                for w in G[smaller]:
                    if w != larger and w in neighbors[larger]: 
                        return True

    return False
