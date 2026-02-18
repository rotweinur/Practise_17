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


if __name__ == "__main__":
    n = int(input())
    vocab = {}
    for _ in range(n):
        line = input()
        key, value = line.split()
        vocab[key] = value
        
    input_phrase = input()
    print(translate_phrase(vocab, input_phrase))
