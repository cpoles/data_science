def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]

def is_anagram(word, candidate):
    w = word.lower()
    c = candidate.lower()
    return w != c and sorted(w) == sorted(c)