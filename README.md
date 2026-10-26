# Algorithm Design and Analysis in Python

A study repository for an Algorithm Design and Analysis course, featuring Python implementations organized by design strategy and problem type.

## Related Repository

This project complements my [Data Structures repository](https://github.com/Cauasc12/Data-Structure). Together, they connect the study of how data is organized with the strategies used to design and analyze algorithms.

Use both repositories to explore how the choice of data structures affects algorithm design, execution time, and memory usage.

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
| Graphs | [Bipartite Check with BFS](01_brute_force/graphs/bipartite_check_bfs.py), [Bipartite Check with DFS](01_brute_force/graphs/bipartite_check_dfs.py), [Connected Components](01_brute_force/graphs/connected_components_dfs.py), [Cycle Detection with BFS](01_brute_force/graphs/cycle_detection_bfs.py), [Iterative DFS](01_brute_force/graphs/iterative_dfs.py), [Topological Sorting with DFS](01_brute_force/graphs/topological_search_dfs.py) | 01 |
| Numerical Algorithms | [Polynomial Evaluation](01_brute_force/numerical/polynomial_evaluation.py) | 01 |
| Sorting | [Insertion Sort](02_decrease_and_conquer/sorting/insertion_sort.py), [Pancake Sort](02_decrease_and_conquer/sorting/pancake_sort.py) | 02 |
| Searching | [Binary Search](02_decrease_and_conquer/searching/binary_search.py), [Interpolation Search](02_decrease_and_conquer/searching/interpolation_search.py), [Matrix Search (Square Matrix)](02_decrease_and_conquer/searching/matrix_search.py), [Missing Number](02_decrease_and_conquer/searching/missing_number.py), [Minimizing the Maximum Distance](02_decrease_and_conquer/searching/minimizing_maximum_distance.py), [Fake Coin (Binary Reduction)](02_decrease_and_conquer/searching/fake_coin_binary.py), [Fake Coin (Ternary Reduction)](02_decrease_and_conquer/searching/fake_coin_ternary.py) | 02 |
| Selection | [Quickselect](02_decrease_and_conquer/selection/quickselect.py), [Iterative Quickselect](02_decrease_and_conquer/selection/iterative_quickselect.py) | 02 |
| Graphs | [Topological Sort (Kahn's Algorithm)](02_decrease_and_conquer/graphs/topological_sort_kahn.py) | 02 |
| Combinatorics | [Binary Reflected Gray Code](02_decrease_and_conquer/combinatorics/binary_reflected_gray_code.py), [Power Set Generation](02_decrease_and_conquer/combinatorics/generate_power_set.py), [Johnson–Trotter Permutations](02_decrease_and_conquer/combinatorics/johnson_trotter_permutation.py), [Lexicographic Permutations](02_decrease_and_conquer/combinatorics/lexicographic_permutation.py), [Minimal-Change Permutations](02_decrease_and_conquer/combinatorics/minimal_change_permutation.py), [Lights On](02_decrease_and_conquer/combinatorics/lights_on.py) | 02 |
| Numerical Algorithms | [Russian Peasant Multiplication](02_decrease_and_conquer/numerical/russian_peasant_multiplication.py) | 02 |
| Games | [One-Pile Nim](02_decrease_and_conquer/games/one_pile_nim.py), [Multi-Pile Nim](02_decrease_and_conquer/games/multi_pile_nim.py), [Summation Game](02_decrease_and_conquer/games/summation_game.py) | 02 |

## Conventions

- Use English for directory names, file names, identifiers, comments, and documentation.
- Use `snake_case` for directory and Python file names.
- Keep one algorithm or variant per file.
- Add problem categories as new implementations are introduced.
- Follow the course's teaching approach when assigning algorithms to chapters.

## Project Status

Work in progress. Chapters 01 and 02 contain 36 algorithm implementations; chapters 03 through 05 have no implementations yet. Supported inputs and return conventions are documented in the chapter READMEs and function docstrings. Some earlier implementations still use Portuguese local variable names; the English naming convention remains the target for those identifiers.

## Verification

Run the deterministic standard-library checks from the repository root:

```bash
python tests/verify_algorithms.py
```

The review on October 26, 2026 ran 58,219 checks covering all 36 algorithms. All chapter 02 checks passed, including Kahn's corrected cycle detection. One chapter 01 boundary case remains: BFS cycle detection misses a self-loop on a vertex labeled `None`, because that label collides with its parent marker. The script reports this case and exits with a nonzero status until it is corrected.

Tests use exhaustive small inputs and independent reference results for sorting, searching, permutations, geometry, graphs, and game states. They support correctness within the documented contracts, rather than proving correctness for every possible input. The square-matrix restriction and circular word-search rules follow their exercise statements; the convex-hull implementation is retained with its documented collinearity behavior.

For precise preconditions and the remaining issue, see [chapter 01](01_brute_force/README.md) and [chapter 02](02_decrease_and_conquer/README.md).
