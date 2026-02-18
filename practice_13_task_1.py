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
    
    sort_list = []
    for word, count in counter.items():
        sort_list.append((-count, word))
    
    sort_list.sort()
    
    result = []
    for _, word in sort_list:
        result.append(word)
        
    return result


if __name__ == "__main__":
    input_text = input()
    sorted_words = get_words_sorted_by_frequency(input_text)
    for w in sorted_words:
        print(w)
