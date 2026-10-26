# 02 — Decrease and Conquer

Strategies that solve a problem by reducing it to a smaller instance and using that instance's solution. Depending on the algorithm, the instance shrinks by a constant amount, a constant factor, or a variable amount.

## Algorithms by Problem Type

### Sorting

- [Insertion Sort](sorting/insertion_sort.py)
- [Pancake Sort](sorting/pancake_sort.py)

### Searching

- [Binary Search](searching/binary_search.py)
- [Interpolation Search](searching/interpolation_search.py)
- [Matrix Search (Square Matrix)](searching/matrix_search.py)
- [Missing Number](searching/missing_number.py)
- [Minimizing the Maximum Distance](searching/minimizing_maximum_distance.py)
- [Fake Coin (Binary Reduction)](searching/fake_coin_binary.py)
- [Fake Coin (Ternary Reduction)](searching/fake_coin_ternary.py)

### Selection

- [Quickselect](selection/quickselect.py)
- [Iterative Quickselect](selection/iterative_quickselect.py)

### Graphs

- [Topological Sort (Kahn's Algorithm)](graphs/topological_sort_kahn.py)

### Combinatorics

- [Binary Reflected Gray Code](combinatorics/binary_reflected_gray_code.py)
- [Power Set Generation](combinatorics/generate_power_set.py)
- [Johnson–Trotter Permutations](combinatorics/johnson_trotter_permutation.py)
- [Lexicographic Permutations](combinatorics/lexicographic_permutation.py)
- [Minimal-Change Permutations](combinatorics/minimal_change_permutation.py)
- [Lights On](combinatorics/lights_on.py)

### Numerical Algorithms

- [Russian Peasant Multiplication](numerical/russian_peasant_multiplication.py)

### Games

- [One-Pile Nim](games/one_pile_nim.py)
- [Multi-Pile Nim](games/multi_pile_nim.py)
- [Summation Game](games/summation_game.py)

## Input Conditions and Results

These contracts describe the supported inputs of the current implementations. The square-matrix restriction comes from the Matrix Search exercise statement; the other conditions follow from the code and the problem interpretations used in the review. Each main function also documents its preconditions and result in an English docstring. Inputs are assumed valid and are not automatically validated.

| Algorithm | Conditions and behavior |
| --- | --- |
| Insertion Sort | Mutable list of comparable values; sorts in place and returns `None`. Empty lists and duplicates are allowed. |
| Pancake Sort | Mutable list of comparable values; sorts in place and returns the list. Empty lists and duplicates are allowed. |
| Binary Search | Sequence sorted in nondecreasing order; returns a matching zero-based index or `-1`. |
| Interpolation Search | Integer sequence sorted in nondecreasing order and integer target; returns an index or `-1`. Uniform distribution is not required for correctness. |
| Matrix Search | **Square n-by-n matrix**, as required by the exercise, with each row and column sorted in nondecreasing order. Returns `(row, column)` or `-1`; the empty matrix returns `-1`. Rectangular matrices are outside the exercise contract. |
| Missing Number | Sorted distinct integers from `1` through `N`, with exactly one missing; returns that value. Empty input represents the missing value `1`. |
| Minimizing the Maximum Distance | Nonempty sorted numeric sequence; returns the index of an input element minimizing its maximum distance to the others. Arithmetic must preserve midpoint comparisons; any optimum is acceptable on ties. |
| Fake Coin, both variants | Nonempty list of `(identifier, weight)` records; exactly one coin is lighter and all genuine coins have equal weight. Returns the counterfeit record. |
| Quickselect, both variants | Nonempty mutable list of comparable values; duplicates allowed. For the whole list use `l = 0`, `r = len(array) - 1`, and one-based `k` in `1..len(array)`. Returns the kth smallest value and modifies the list. For restricted intervals, `k - 1` is an absolute array index. |
| Kahn's Topological Sort | Directed adjacency dictionary containing every vertex as a key. A full ordering exists only for a DAG. Returns an ordering for a DAG; on a cycle, prints a message and returns `1`. Empty input returns `[]`. |
| Binary Reflected Gray Code | Positive integer bit count; returns all binary reflected Gray code words of that length. Zero bits are not supported by the current base case. |
| Power Set Generation | List of distinct elements; returns all subsets as lists. Empty input is supported. |
| Johnson–Trotter Permutations | Nonnegative integer `n`, or an increasingly sorted list of distinct positive numbers; generates all permutations through adjacent swaps. |
| Lexicographic Permutations | Nonnegative integer `n`, or a list of comparable values. A supplied list must start sorted to enumerate every permutation; otherwise enumeration begins at that arrangement. Duplicates are supported. |
| Minimal-Change Permutations | Nonempty list of distinct elements; generates every permutation through adjacent swaps. |
| Lights On | Mutable `[identifier, boolean_state]` records; each switch affects only its own light. Mutates states and returns `True` when all lights are on, including empty input. |
| Russian Peasant Multiplication | First operand is a nonnegative integer; second operand is any integer. Returns their product. |
| One-Pile Nim | Positive integer pile size and removal limit; remove `1..max_take` without exceeding the pile. Taking the last object wins. Returns a winning move when possible, otherwise `1`. |
| Multi-Pile Nim | Nonnegative integer pile sizes; remove objects from one pile per turn, and taking the last object wins. Returns a winning `(pile_index, removal_count)` when possible, otherwise a legal fallback; returns `None` when no move remains. |
| Summation Game | Integer current sum strictly below the target and positive integer increment limit. Add `1..max_sum` without exceeding the target; reaching it wins. Returns a winning increment when possible, otherwise `1`. |

## Correctness Review

All 22 implementations passed the latest repository-wide verification within the contracts above. Checks include repeated values, exhaustive small inputs, full-list and restricted-interval selection, permutation coverage and adjacent swaps, square matrices, counterfeit-coin positions, and game moves compared with exhaustive game-state evaluation.

Kahn's final check now correctly compares `len(order) < len(graph)`; both DAGs and cyclic graphs passed. Its cycle result is `1`, whereas the DFS-based topological implementation in chapter 01 returns `None` on a cycle. Both print a message. These are different documented return conventions.

Run `python tests/verify_algorithms.py` from the repository root to repeat the review. The script also covers chapter 01, where a separate graph-label boundary issue remains. Finite tests support these contracts; they do not replace a general proof of correctness.

Recursive implementations remain subject to Python's recursion limit; exhaustive generators require time and memory proportional to the generated output.

## Organization Notes

- Recursive and iterative selection algorithms are kept together for comparison.
- The two fake-coin implementations are named after their binary and ternary reduction strategies.
- Lights On is grouped under combinatorics because it explores switch configurations through single-bit changes.
- Games remain in this chapter to follow the course material.

These are study implementations. Review results and supported inputs are documented above; behavior outside those contracts has not been validated.

[Back to the index](../README.md)
