import sys

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

def solve_task_3() -> None:
    """
    Reads input and prints the result for Task 3.
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        antonyms = {}
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if line:
                word1, word2 = line.split()
                antonyms[word1] = word2
                antonyms[word2] = word1
        target_word = sys.stdin.readline().strip()
        print(find_antonym(antonyms, target_word))
    except ValueError:
        pass

if __name__ == "__main__":
    solve_task_3()