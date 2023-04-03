import re


def count_sentences(text: str) -> int:
    """Amount of sentences in the processed text"""

    if text[len(text) - 1] != '.' and text[len(text) - 1] != '!' and text[len(text) - 1] != '?':
        text += '.'
    declarative = len(re.findall(r'\.+|(?<=[^?])!+(?=[^?])', text))
    question = len(re.findall(r'\?', text))
    return declarative + question
