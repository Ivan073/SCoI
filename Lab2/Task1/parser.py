import re


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
