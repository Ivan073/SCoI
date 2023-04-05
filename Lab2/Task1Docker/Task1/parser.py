import re

from helpers import get_sentence_list, get_word_list


def count_sentences(text: str) -> int:
    """Amount of sentences in the processed text"""
    if len(text) == 0:
        return 0

    if text[len(text) - 1] != '.' and text[len(text) - 1] != '!' and text[len(text) - 1] != '?':
        text += '.'
    text += " "
    declarative = len(re.findall(r'\.+(?=\s)', text))
    nondeclarative = len(re.findall(r'\?+(?=\s)|!+(?=\s)', text))
    return declarative + nondeclarative


def count_nondeclarative_sentences(text: str) -> int:
    """Amount of non-declarative sentences in the processed text"""

    if text[len(text) - 1] != '.' and text[len(text) - 1] != '!' and text[len(text) - 1] != '?':
        text += '.'
    text += " "
    nondeclarative = len(re.findall(r'\?+(?=\s)|!+(?=\s)', text))
    return nondeclarative


def count_average_length_of_sentences(text: str) -> int:
    """Average length of sentences in text"""

    sentences = get_sentence_list(text)
    words = get_word_list(text)
    return len(words)/len(sentences)


def count_average_length_of_words(text: str) -> int:
    """Average length of words in text"""
    words = get_word_list(text)
    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length/len(words)


def top_k_ngrams(text: str, k: int, n: int) -> int:
    words = get_word_list(text)
    ngrams = tuple(" ".join(words[i:i + n]) for i in range(len(words) - (n - 1)))
    sorted_unique_ngrams = sorted(set(ngrams), key=ngrams.count, reverse=True)
    return sorted_unique_ngrams[:k]
