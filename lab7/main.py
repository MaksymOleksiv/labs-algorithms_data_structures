def build_dfa(needle: str) -> list[dict]:
    """
    Function to build a Deterministic Finite Automaton (DFA) for a given string (needle).
    :param needle: str: The string for which the DFA is built.
    :return: list[dict]: A list of dictionaries representing the DFA.
    """
    M = len(needle)
    alphabet = needle
    dfa = [{} for _ in range(M + 1)]

    for state in range(M + 1):
        for char in alphabet:
            prefix = needle[:state] + char
            k = min(M, state + 1)
            while k > 0 and needle[:k] != prefix[-k:]:
                k -= 1
            dfa[state][char] = k

    return dfa


def search_dfa(haystack: str, needle: str) -> list:
    """
    Function to search for a string (needle) in another string (haystack) using a DFA.
    :param haystack: str: The string in which to search.
    :param needle: str: The string to search for.
    :return: list: A list of starting indices where the needle is found in the haystack.
    """
    table = build_dfa(needle)
    state = 0
    result = []

    if not needle:
        return result

    for i, char in enumerate(haystack):
        if char in table[state]:
            state = table[state][char]
        else:
            state = 0

        if state == len(needle):
            result.append(i - len(needle) + 1)

    return result
