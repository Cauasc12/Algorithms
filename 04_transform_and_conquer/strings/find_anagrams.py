def find_anagrams(dictionary):
    anagrams = {}

    for p in dictionary:
        key = ''.joing(sorted(p))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(p)

    result = []
    for group in anagrams.values():
        if len(group) > 1:
            result.append(group)

    return result