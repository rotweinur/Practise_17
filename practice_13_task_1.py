import sys
from collections import Counter

def get_words_sorted_by_frequency(text: str) -> list[str]:
    """
    Sorts words from the text by frequency in descending order.
    Args:
        text (str): Input string containing words.
    Returns:
        list[str]: List of words sorted by frequency.
    """
    words = text.split()
    counter = Counter(words)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [item[0] for item in sorted_items]

def solve_task_1() -> None:
    """
    Reads input and prints the result for Task 1.
    """
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        result = get_words_sorted_by_frequency(input_data)
        for word in result:
            print(word)
    except Exception:
        pass

if __name__ == "__main__":
    solve_task_1()