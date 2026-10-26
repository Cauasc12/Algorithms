# 01 — Brute Force

Implementations and exercises grouped under this course chapter.

| Category | Algorithms |
| --- | --- |
| [Sorting](sorting/) | Bubble Sort and Selection Sort |
| [Strings](strings/) | String Matching and Word Search |
| [Geometry](geometry/) | Closest Pair, Convex Hull, and Extreme Points |
| [Graphs](graphs/) | Bipartite checks with BFS/DFS, connected components, cycle detection, iterative DFS, and [topological sorting with DFS](graphs/topological_search_dfs.py) |
| [Numerical Algorithms](numerical/) | Polynomial Evaluation |

## Input Conditions and Results

Inputs are assumed valid and are not automatically validated. Each main function has an English docstring describing its contract.

| Algorithm | Conditions and behavior |
| --- | --- |
| Bubble Sort and Selection Sort | Mutable lists of comparable values; sort in place and return `None`. Empty lists and duplicate values are supported. |
| String Matching | String text and pattern; returns the first zero-based match or `-1`. An empty pattern matches at index `0`. |
| Word Search | Nonempty rectangular grid with nonempty rows and nonempty words. Searches eight straight directions with circular boundaries, as allowed by the exercise. Wrapping may revisit cells. Returns the first occurrence per word as `(word, (row, column), (dr, dc))`, using row-major starting positions and the direction order in the code. Prints a message for absent words. |
| Closest Pair | Numeric `(x, y)` points with finite, sufficiently accurate distance arithmetic. Returns the minimum distance, not the pair. Duplicates are supported; fewer than two points return positive infinity. |
| Convex Hull | For the usual boundary-edge interpretation: distinct numeric points with no three collinear, with sufficiently accurate orientation arithmetic. Returns boundary segments without a cyclic vertex ordering. The implementation is intentionally unchanged: collinear inputs may yield overlapping segments and duplicate points may yield zero-length segments. |
| Extreme Points | Nonempty sequence of `(x, y)` points. Returns lexicographic minimum and maximum, prioritizing `x` and breaking ties by `y`; it does not return all four coordinate extrema. |
| Bipartite Check, BFS and DFS | Undirected graph represented by symmetric adjacency lists, with every vertex as a dictionary key. Returns a boolean; disconnected and empty graphs are supported, and self-loops invalidate bipartiteness. |
| Connected Components | Undirected graph with symmetric adjacency lists and every vertex as a dictionary key. Returns the component count; an empty graph has zero components. |
| Cycle Detection with BFS | Undirected graph with symmetric adjacency lists, every vertex as a key, and no repeated neighbors. Returns a boolean; self-loops are supported except for the known `None`-label issue below. |
| Iterative DFS | Directed or undirected adjacency dictionary with every vertex as a key. Visits each vertex once across all components, exploring neighbors in reverse adjacency-list order. Returns the DFS preorder. |
| Topological Sorting with DFS | Directed adjacency dictionary with every vertex as a key. Returns a topological ordering for a DAG; on a cycle, prints a message and returns `None`. Empty input returns `[]`. |
| Polynomial Evaluation | Nonempty coefficient sequence in increasing degree order, `[a0, a1, ..., an]`. Returns `a0 + a1*x + ... + an*x**n`. |

Graph labels must be hashable. Both topological implementations require every vertex, including sinks and isolated vertices, to appear as a key. Recursive implementations remain subject to Python's recursion limit.

## Correctness Review

The repository-wide checks are reproducible with `python tests/verify_algorithms.py` from the repository root. The review covers these 14 algorithms, including square-grid geometry samples without collinear triples, circular word search, graph self-loops, and cyclic directed graphs.

One boundary case remains: `cycle_detection_bfs({None: [None]})` returns `False` instead of `True`. The root-parent marker is also `None`, so that label collides with the marker. This issue is retained in the verification script as a failing regression check; integer-labeled graph cases passed. Use a unique object as the root-parent sentinel to support `None` labels correctly.

## Organization Notes

Graph exercises remain in this chapter to preserve the study material's grouping. BFS and DFS are graph traversal techniques; their placement follows the course organization and does not classify every application of these techniques as brute force.

[Back to the index](../README.md)
