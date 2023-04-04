import re

from Lab2.Task1.helpers import get_sentence_list, get_word_list


def count_sentences(text: str) -> int:
    """Amount of sentences in the processed text"""

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
    nondeclarative = len(re.findall(r'\?+(?=\s)|!+(?=\s)', text))
    return nondeclarative


def count_average_length_of_sentences(text: str) -> int:
    """Average length of sentences in text"""

    sentences = get_sentence_list(text)
    words = get_word_list(text)
    return len(words)/len(sentences)
