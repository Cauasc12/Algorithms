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
| Selection | [Mode](01_brute_force/selection/mode.py) | 01 |
| Sets | [Set Intersection](01_brute_force/sets/set_intersection.py) | 01 |
| Sorting | [Insertion Sort](02_decrease_and_conquer/sorting/insertion_sort.py), [Pancake Sort](02_decrease_and_conquer/sorting/pancake_sort.py) | 02 |
| Searching | [Binary Search](02_decrease_and_conquer/searching/binary_search.py), [Interpolation Search](02_decrease_and_conquer/searching/interpolation_search.py), [Matrix Search (Square Matrix)](02_decrease_and_conquer/searching/matrix_search.py), [Missing Number](02_decrease_and_conquer/searching/missing_number.py), [Minimizing the Maximum Distance](02_decrease_and_conquer/searching/minimizing_maximum_distance.py), [Fake Coin (Binary Reduction)](02_decrease_and_conquer/searching/fake_coin_binary.py), [Fake Coin (Ternary Reduction)](02_decrease_and_conquer/searching/fake_coin_ternary.py) | 02 |
| Selection | [Quickselect](02_decrease_and_conquer/selection/quickselect.py), [Iterative Quickselect](02_decrease_and_conquer/selection/iterative_quickselect.py) | 02 |
| Graphs | [Topological Sort (Kahn's Algorithm)](02_decrease_and_conquer/graphs/topological_sort_kahn.py) | 02 |
| Combinatorics | [Binary Reflected Gray Code](02_decrease_and_conquer/combinatorics/binary_reflected_gray_code.py), [Power Set Generation](02_decrease_and_conquer/combinatorics/generate_power_set.py), [Johnson–Trotter Permutations](02_decrease_and_conquer/combinatorics/johnson_trotter_permutation.py), [Lexicographic Permutations](02_decrease_and_conquer/combinatorics/lexicographic_permutation.py), [Minimal-Change Permutations](02_decrease_and_conquer/combinatorics/minimal_change_permutation.py), [Lights On](02_decrease_and_conquer/combinatorics/lights_on.py) | 02 |
| Numerical Algorithms | [Russian Peasant Multiplication](02_decrease_and_conquer/numerical/russian_peasant_multiplication.py), [Polynomial Resolution](02_decrease_and_conquer/numerical/polynon_resolution.py) | 02 |
| Games | [One-Pile Nim](02_decrease_and_conquer/games/one_pile_nim.py), [Multi-Pile Nim](02_decrease_and_conquer/games/multi_pile_nim.py), [Summation Game](02_decrease_and_conquer/games/summation_game.py) | 02 |
| Sorting | [Mergesort](03_divide_and_conquer/sorting/mergesort.py), [Quicksort](03_divide_and_conquer/sorting/quicksort.py), [Inversion Count](03_divide_and_conquer/sorting/inversion_quantity.py) | 03 |
| Geometry | [Closest Pair](03_divide_and_conquer/geometry/closest_pair.py) | 03 |
| Tiling | [Tromino Tiling](03_divide_and_conquer/tiling/tromino_tile.py) | 03 |
| Sorting | [Heapsort](04_transform_and_conquer/sorting/heapsort.py) | 04 |
| Selection | [Mode](04_transform_and_conquer/selection/mode.py), [Extreme Elements](04_transform_and_conquer/selection/extreme_elements.py) | 04 |
| Searching | [Sum Check](04_transform_and_conquer/searching/is_sum.py), [Count Larger Heap Entries](04_transform_and_conquer/searching/count_biggers.py) | 04 |
| Geometry | [Closest Pair](04_transform_and_conquer/geometry/closest_pair.py), [Maximal Points](04_transform_and_conquer/geometry/max_points.py), [Simple Polygon](04_transform_and_conquer/geometry/simple_polygon.py) | 04 |
| Strings | [Find Anagrams](04_transform_and_conquer/strings/find_anagrams.py) | 04 |
| Sets | [Set Intersection](04_transform_and_conquer/sets/set_intersection.py), [Element Uniqueness](04_transform_and_conquer/sets/element_uniquiness.py), [Telephone Bills](04_transform_and_conquer/sets/telephone_bills.py) | 04 |
| Intervals | [Maximum Interval Overlap](04_transform_and_conquer/intervals/max_overlap_intervals.py) | 04 |
| Combinatorics | [Number Placement](04_transform_and_conquer/combinatorics/number_placement.py) | 04 |
| Numerical Algorithms | [Gaussian Elimination](04_transform_and_conquer/numerical/gaussian_elimination.py), [Horner's Rule](04_transform_and_conquer/numerical/horner_rule.py), [Left-to-Right Binary Exponentiation](04_transform_and_conquer/numerical/left_right_binary_exponentitation.py), [Right-to-Left Binary Exponentiation](04_transform_and_conquer/numerical/right_left_binary_exponentitation.py), [Right-to-Left Exponentiation](04_transform_and_conquer/numerical/righ_left_exponentitation.py) | 04 |

## Files Created but Not Implemented

These files have been created and contain no code. Chapters 01 and 02 have no files in this state. Chapter 05 has no algorithm files yet.

| Algorithm | File | Chapter |
| --- | --- | --- |
| Median-of-Three Quicksort | [medianofthree_quicksort.py](03_divide_and_conquer/sorting/medianofthree_quicksort.py) | 03 |
| Randomized Quicksort | [randomized_quicksort.py](03_divide_and_conquer/sorting/randomized_quicksort.py) | 03 |
| Quickhull | [quickhull.py](03_divide_and_conquer/geometry/quickhull.py) | 03 |
| Large-Integer Multiplication | [big_number_multiplication.py](03_divide_and_conquer/numerical/big_number_multiplication.py) | 03 |
| Strassen Matrix Multiplication | [strassen_matrix_multiplication.py](03_divide_and_conquer/numerical/strassen_matrix_multiplication.py) | 03 |
| Determinant | [determinant.py](04_transform_and_conquer/numerical/determinant.py) | 04 |
| Inverse Matrix | [inverse_matrix.py](04_transform_and_conquer/numerical/inverse_matrix.py) | 04 |
| LU Decomposition | [lu_decomposition.py](04_transform_and_conquer/numerical/lu_decomposition.py) | 04 |

## Conventions

- Use English for directory names, file names, identifiers, comments, and documentation.
- Use `snake_case` for directory and Python file names.
- Keep one algorithm or variant per file.
- Add problem categories as new implementations are introduced.
- Follow the course's teaching approach when assigning algorithms to chapters.

## Project Status

Work in progress. Algorithms sit in problem-type folders inside each strategy chapter. The index lists implemented algorithms. Eight files in chapters 03 and 04 exist without code; they are listed separately below the index. Chapter 05 has no algorithm files yet. Supported inputs and return conventions for the reviewed chapter 01 and 02 algorithms are documented in those chapter READMEs and function docstrings. Some earlier implementations still use Portuguese local variable names; the English naming convention remains the target for those identifiers.

## Verification

Run the deterministic standard-library checks from the repository root:

```bash
python tests/verify_algorithms.py
```

On October 31, 2026, the 36 algorithms indexed above were checked again: 58,219 checks and 0 failures. BFS cycle detection now uses a unique root-parent sentinel, and `cycle_detection_bfs({None: [None]})` returns `True`. Kahn's cycle check in chapter 02 also passed.

`python tests/verify_algorithms.py` loads every Python file under the numbered chapters and expects each file to define a function of the same name. It currently stops on empty files and on files whose function name differs from the file name. `closest_pair`, `mode`, and `set_intersection` occur in more than one chapter, and the loader keeps only the last definition of each name.

Tests use exhaustive small inputs and independent reference results for sorting, searching, permutations, geometry, graphs, and game states. They support correctness within the documented contracts, rather than proving correctness for every possible input. The square-matrix restriction and circular word-search rules follow their exercise statements; the convex-hull implementation is retained with its documented collinearity behavior.

For precise preconditions, see [chapter 01](01_brute_force/README.md) and [chapter 02](02_decrease_and_conquer/README.md).
