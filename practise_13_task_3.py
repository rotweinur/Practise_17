def find_antonym(antonym_map: dict[str, str], word: str) -> str:
    """
    Finds the antonym for a given word using a bidirectional map.
    Args:
        antonym_map (dict[str, str]): Dictionary of antonyms.
        word (str): The word to find an antonym for.
    Returns:
        str: The antonym or the original word if not found.
    """
    return antonym_map.get(word, word)


if __name__ == "__main__":
    n = int(input())
    antonyms = {}
    for _ in range(n):
        line = input()
        word1, word2 = line.split()
        antonyms[word1] = word2
        antonyms[word2] = word1
        
    target_word = input()
    print(find_antonym(antonyms, target_word))
