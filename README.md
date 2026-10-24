# Algorithm Design and Analysis in Python

A study repository for an Algorithm Design and Analysis course, featuring Python implementations organized by design strategy and problem type.

## Chapters

Numbered directories follow the course chapters. Within each chapter, algorithms are grouped by problem type. Implementations that solve the same problem using different strategies belong in their respective chapters.

| Chapter | Strategy |
| --- | --- |
| 01 | [Brute Force](01_brute_force/README.md) |
| 02 | [Decrease and Conquer](02_decrease_and_conquer/README.md) |
| 03 | [Divide and Conquer](03_divide_and_conquer/README.md) |
| 04 | [Transform and Conquer](04_transform_and_conquer/README.md) |
| 05 | [Time–Space Tradeoffs](05_time_space_tradeoffs/README.md) |

## Index by Problem Type

| Type | Implementations | Chapter |
| --- | --- | --- |
| Sorting | [Bubble Sort](01_brute_force/sorting/bubble_sort.py), [Selection Sort](01_brute_force/sorting/selection_sort.py) | 01 |
| Strings | [String Matching](01_brute_force/strings/string_matching.py), [Word Search](01_brute_force/strings/word_search.py) | 01 |
| Geometry | [Closest Pair](01_brute_force/geometry/closest_pair.py), [Convex Hull](01_brute_force/geometry/convex_hull.py), [Extreme Points](01_brute_force/geometry/extreme_points.py) | 01 |
| Graphs | [Bipartite Check with BFS](01_brute_force/graphs/bipartite_check_bfs.py), [Bipartite Check with DFS](01_brute_force/graphs/bipartite_check_dfs.py), [Connected Components](01_brute_force/graphs/connected_components_dfs.py), [Cycle Detection with BFS](01_brute_force/graphs/cycle_detection_bfs.py), [Iterative DFS](01_brute_force/graphs/iterative_dfs.py) | 01 |
| Numerical Algorithms | [Polynomial Evaluation](01_brute_force/numerical/polynomial_evaluation.py) | 01 |
| Searching | [Minimizing the Maximum Distance](02_decrease_and_conquer/searching/minimizing_maximum_distance.py) | 02 |

## Conventions

- Use English for directory names, file names, identifiers, comments, and documentation.
- Use `snake_case` for directory and Python file names.
- Keep one algorithm or variant per file.
- Add problem categories as new implementations are introduced.
- Follow the course's teaching approach when assigning algorithms to chapters.

## Project Status

Work in progress. These implementations are study exercises and still require correctness reviews and automated tests.
