import sys

def translate_phrase(dictionary: dict[str, str], phrase: str) -> str:
    """
    Translates a phrase using the provided dictionary.
    Args:
        dictionary (dict[str, str]): Dictionary mapping source words to target words.
        phrase (str): The sentence to translate.
    Returns:
        str: Translated sentence.
    """
    words = phrase.split()
    translated_words = []
    for word in words:
        translated_words.append(dictionary.get(word, word))
    return " ".join(translated_words)

def solve_task_2() -> None:
    """
    Reads input and prints the result for Task 2.
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        vocab = {}
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if line:
                key, value = line.split()
                vocab[key] = value
        phrase = sys.stdin.readline().strip()
        print(translate_phrase(vocab, phrase))
    except ValueError:
        pass

if __name__ == "__main__":
    solve_task_2()