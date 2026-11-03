def process_ancestry(tree, root=0):
    disc = {}
    finish = {}
    time = [0]

    def dfs(u):
        time[0] += 1
        disc[u] = time[0]
        for child in tree[u]:
            dfs(child)
        time[0] += 1
        finish[u] = time[0]

    dfs(root)
    return disc, finish

def is_ancestor(u, v, disc, finish):

    return (disc[u] <= disc[v]) and (disc[v] <= finish[u])