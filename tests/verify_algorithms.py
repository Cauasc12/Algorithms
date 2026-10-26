"""Run deterministic correctness checks: python tests/verify_algorithms.py.

Uses only the standard library and loads source without creating bytecode files.
Checks small exhaustive inputs against independent reference results. A failing
check is reported without stopping the remaining algorithm checks.
"""

import ast
from collections import Counter
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations, product
import io
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTIONS = {}
COUNTS = Counter()
FAILURES = []


def check(name, condition, example=None):
    COUNTS[name] += 1
    if not condition:
        FAILURES.append((name, example))


def load_algorithms():
    for chapter in sorted(ROOT.glob('[0-9][0-9]_*')):
        for path in sorted(chapter.rglob('*.py')):
            source = path.read_text(encoding='utf-8-sig')
            ast.parse(source)
            namespace = {}
            exec(compile(source, str(path), 'exec'), namespace)
            FUNCTIONS[path.stem] = namespace[path.stem]


def sorting_and_selection():
    for n in range(7):
        for values in product(range(3), repeat=n):
            for name in ('bubble_sort', 'selection_sort', 'insertion_sort', 'pancake_sort'):
                array = list(values)
                result = FUNCTIONS[name](array)
                expected_return = array if name == 'pancake_sort' else None
                check(name, array == sorted(values) and result == expected_return, values)
            for k in range(1, n + 1):
                for name in ('quickselect', 'iterative_quickselect'):
                    answer = FUNCTIONS[name](list(values), 0, n - 1, k)
                    check(name, answer == sorted(values)[k - 1], (values, k, answer))
    for name in ('quickselect', 'iterative_quickselect'):
        for values in product(range(3), repeat=4):
            for left, right in ((0, 2), (1, 3), (1, 2)):
                for index in range(left, right + 1):
                    array = list(values)
                    answer = FUNCTIONS[name](array, left, right, index + 1)
                    check(name, answer == sorted(values[left:right + 1])[index - left]
                          and array[:left] == list(values[:left])
                          and array[right + 1:] == list(values[right + 1:]),
                          (values, left, right, index, answer))


def numeric_searches():
    for n in range(7):
        for values in combinations_with_replacement(range(-2, 4), n):
            for target in range(-3, 5):
                for name in ('binary_search', 'interpolation_search'):
                    index = FUNCTIONS[name](values, target)
                    good = (index == -1 and target not in values) or (
                        0 <= index < n and values[index] == target)
                    check(name, good, (values, target, index))
            if n:
                index = FUNCTIONS['minimizing_maximum_distance'](values)
                actual = max(abs(values[index] - x) for x in values)
                best = min(max(abs(y - x) for x in values) for y in values)
                check('minimizing_maximum_distance', actual == best, (values, index))
    for n in range(1, 101):
        for missing in range(1, n + 1):
            values = [x for x in range(1, n + 1) if x != missing]
            check('missing_number', FUNCTIONS['missing_number'](values) == missing)
    for n in range(1, 41):
        for fake in range(n):
            coins = [(i, 9 if i == fake else 10) for i in range(n)]
            for name in ('fake_coin_binary', 'fake_coin_ternary'):
                check(name, FUNCTIONS[name](coins) == coins[fake], (n, fake))
    for n in range(51):
        for m in range(-20, 21):
            check('russian_peasant_multiplication',
                  FUNCTIONS['russian_peasant_multiplication'](n, m) == n * m)
    for n in range(4):
        for cells in product(range(3), repeat=n * n):
            matrix = [cells[i * n:(i + 1) * n] for i in range(n)]
            if any(matrix[i][j] > matrix[i][j + 1]
                   for i in range(n) for j in range(n - 1)):
                continue
            if any(matrix[i][j] > matrix[i + 1][j]
                   for i in range(n - 1) for j in range(n)):
                continue
            for target in range(-1, 4):
                answer = FUNCTIONS['matrix_search'](matrix, target)
                good = (answer == -1 and target not in cells) or (
                    answer != -1 and matrix[answer[0]][answer[1]] == target)
                check('matrix_search', good, (matrix, target, answer))
    for n in range(1, 5):
        for coefficients in product(range(-2, 3), repeat=n):
            for x in range(-2, 3):
                answer = FUNCTIONS['polynomial_evaluation'](coefficients, x)
                check('polynomial_evaluation', answer == sum(
                    c * x ** i for i, c in enumerate(coefficients)))


def string_algorithms():
    strings = [''.join(p) for n in range(5) for p in product('ab', repeat=n)]
    for text in strings:
        for pattern in strings:
            check('string_matching', FUNCTIONS['string_matching'](text, pattern)
                  == text.find(pattern), (text, pattern))
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1))
    words = [w for w in strings if w]
    for rows, cols in ((1, 1), (1, 3), (2, 2), (2, 3), (3, 1)):
        for cells in product('ab', repeat=rows * cols):
            grid = [''.join(cells[i * cols:(i + 1) * cols]) for i in range(rows)]
            expected = []
            for word in words:
                matches = []
                for row, col in product(range(rows), range(cols)):
                    for dr, dc in directions:
                        ray = ''.join(grid[(row + k * dr) % rows][(col + k * dc) % cols]
                                      for k in range(len(word)))
                        if ray == word:
                            matches.append((word, (row, col), (dr, dc)))
                if matches:
                    expected.append(matches[0])
            with redirect_stdout(io.StringIO()):
                actual = FUNCTIONS['word_search'](grid, words)
            check('word_search', actual == expected, grid)


def geometry():
    points = list(product(range(3), repeat=2))
    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    def reference_hull(values):
        ordered = sorted(values)
        lower, upper = [], []
        for p in ordered:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        for p in reversed(ordered):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        vertices = lower[:-1] + upper[:-1]
        return {frozenset((vertices[i], vertices[(i + 1) % len(vertices)]))
                for i in range(len(vertices))}
    for n in range(1, 6):
        for values in combinations(points, n):
            check('extreme_points', FUNCTIONS['extreme_points'](values)
                  == (min(values), max(values)), values)
            if n >= 2:
                expected = min(math.dist(a, b) for a, b in combinations(values, 2))
                check('closest_pair', math.isclose(FUNCTIONS['closest_pair'](values), expected))
                if not any(cross(*triple) == 0 for triple in combinations(values, 3)):
                    actual = FUNCTIONS['convex_hull'](values)
                    edges = {frozenset(edge) for edge in actual}
                    check('convex_hull', len(edges) == len(actual)
                          and edges == reference_hull(values), values)
    check('closest_pair', FUNCTIONS['closest_pair']([(0, 0), (0, 0)]) == 0)
    check('extreme_points', FUNCTIONS['extreme_points']([(1, 2), (1, 2)])
          == ((1, 2), (1, 2)))
    for values in ([], [(1, 2)]):
        check('closest_pair', FUNCTIONS['closest_pair'](values) == float('inf'))


def graph_algorithms():
    for n in range(5):
        possible = list(combinations(range(n), 2)) + [(i, i) for i in range(n)]
        for bits in product((0, 1), repeat=len(possible)):
            graph = {i: [] for i in range(n)}
            for (u, v), bit in zip(possible, bits):
                if bit:
                    graph[u].append(v)
                    if u != v:
                        graph[v].append(u)
            bipartite = any(all(colors[u] != colors[v] for u in graph for v in graph[u])
                            for colors in product((0, 1), repeat=n))
            for name in ('bipartite_check_bfs', 'bipartite_check_dfs'):
                check(name, FUNCTIONS[name](graph) == bipartite, graph)
            seen, expected = set(), []
            def dfs(u):
                seen.add(u)
                expected.append(u)
                for v in reversed(graph[u]):
                    if v not in seen:
                        dfs(v)
            components = 0
            for u in graph:
                if u not in seen:
                    components += 1
                    dfs(u)
            check('connected_components_dfs',
                  FUNCTIONS['connected_components_dfs'](graph) == components, graph)
            check('iterative_dfs', FUNCTIONS['iterative_dfs'](graph) == expected, graph)
            loops = any(u in graph[u] for u in graph)
            edges = sum(sum(v != u for v in graph[u]) for u in graph) // 2
            check('cycle_detection_bfs', FUNCTIONS['cycle_detection_bfs'](graph)
                  == (loops or edges > n - components), graph)
    # None is a legal dictionary key but collides with the current parent sentinel.
    check('cycle_detection_bfs', FUNCTIONS['cycle_detection_bfs']({None: [None]}) is True,
          'Self-loop on vertex None is incorrectly reported as acyclic')
    for n in range(4):
        possible = list(product(range(n), repeat=2))
        for bits in product((0, 1), repeat=len(possible)):
            graph = {i: [] for i in range(n)}
            for (u, v), bit in zip(possible, bits):
                if bit:
                    graph[u].append(v)
            def valid(order):
                positions = {u: i for i, u in enumerate(order)}
                return all(positions[u] < positions[v] for u in graph for v in graph[u])
            dag = any(valid(p) for p in permutations(graph))
            for name, sentinel in (('topological_sort_kahn', 1), ('topological_search_dfs', None)):
                with redirect_stdout(io.StringIO()):
                    answer = FUNCTIONS[name](graph)
                good = (isinstance(answer, list) and len(answer) == n
                        and set(answer) == set(graph) and valid(answer)) if dag else answer == sentinel
                check(name, good, (graph, answer))


def combinatorics():
    for n in range(9):
        answer = FUNCTIONS['generate_power_set'](list(range(n)))
        expected = {tuple(i for i in range(n) if bits[i])
                    for bits in product((0, 1), repeat=n)}
        check('generate_power_set', len(answer) == 2 ** n
              and {tuple(a) for a in answer} == expected)
    for n in range(1, 9):
        expected = [format(i ^ (i >> 1), f'0{n}b') for i in range(2 ** n)]
        check('binary_reflected_gray_code', FUNCTIONS['binary_reflected_gray_code'](n) == expected)
    for n in range(7):
        expected = [list(p) for p in permutations(range(1, n + 1))]
        check('lexicographic_permutation', FUNCTIONS['lexicographic_permutation'](n) == expected)
    for values in combinations_with_replacement(range(3), 4):
        expected = [list(p) for p in sorted(set(permutations(values)))]
        check('lexicographic_permutation', FUNCTIONS['lexicographic_permutation'](values) == expected)
    for name in ('johnson_trotter_permutation', 'minimal_change_permutation'):
        for n in range(1, 7):
            answer = FUNCTIONS[name](n if name.startswith('johnson') else list(range(1, n + 1)))
            good = len(answer) == math.factorial(n) and {tuple(p) for p in answer} == set(
                permutations(range(1, n + 1)))
            for a, b in zip(answer, answer[1:]):
                changed = [i for i in range(n) if a[i] != b[i]]
                good = good and len(changed) == 2 and changed[1] == changed[0] + 1
            check(name, good, n)
    for values in ([2, 5, 9], [10, 20, 30, 40], []):
        answer = FUNCTIONS['johnson_trotter_permutation'](values)
        check('johnson_trotter_permutation', len(answer) == math.factorial(len(values))
              and {tuple(p) for p in answer} == set(permutations(values)))
    for n in range(9):
        for bits in product((False, True), repeat=n):
            buttons = [[i, b] for i, b in enumerate(bits)]
            check('lights_on', FUNCTIONS['lights_on'](buttons) is True
                  and all(b[1] for b in buttons))


def games():
    @lru_cache(None)
    def wins(size, limit):
        return any(not wins(size - take, limit)
                   for take in range(1, min(size, limit) + 1))
    for size in range(1, 61):
        for limit in range(1, 11):
            for name, args in (('one_pile_nim', (size, limit)),
                               ('summation_game', (7, 7 + size, limit))):
                take = FUNCTIONS[name](*args)
                check(name, 1 <= take <= min(size, limit)
                      and (not wins(size, limit) or not wins(size - take, limit)))
    @lru_cache(None)
    def nim_wins(piles):
        for i, size in enumerate(piles):
            for take in range(1, size + 1):
                next_piles = list(piles)
                next_piles[i] -= take
                if not nim_wins(tuple(next_piles)):
                    return True
        return False
    for n in range(5):
        for piles in product(range(5), repeat=n):
            answer = FUNCTIONS['multi_pile_nim'](piles)
            if not any(piles):
                good = answer is None
            else:
                i, take = answer
                next_piles = list(piles)
                next_piles[i] -= take
                good = (0 <= i < n and 1 <= take <= piles[i]
                        and (not nim_wins(piles) or not nim_wins(tuple(next_piles))))
            check('multi_pile_nim', good, piles)


def main():
    load_algorithms()
    for group in (sorting_and_selection, numeric_searches, string_algorithms,
                  geometry, graph_algorithms, combinatorics, games):
        group()
    assert set(COUNTS) == set(FUNCTIONS), 'Missing algorithm coverage'
    failed_counts = Counter(name for name, _ in FAILURES)
    for name in sorted(COUNTS):
        print(f'{name}: {COUNTS[name]} checks, {failed_counts[name]} failures')
    print(f'Total: {sum(COUNTS.values())} checks; {len(COUNTS)} algorithms; '
          f'{len(FAILURES)} failures')
    for name, example in FAILURES[:10]:
        print(f'FAIL {name}: {example}')
    return bool(FAILURES)


if __name__ == '__main__':
    raise SystemExit(main())
